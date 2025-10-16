#!/usr/bin/env python3
import os
import re
import sys
import time
import html
import urllib.request
import urllib.error
from urllib.parse import urlparse


BIBLIO_PATH = os.path.abspath(
    "/Users/jeffwhatcott/Library/Mobile Documents/com~apple~CloudDocs/Documents/JRW/APEX-SPARK-DELEGATE/6_GTM/AI Groundwork Substack/Articles/Published/the_great_refactor/great-refactor-data/sources/BIBLIOGRAPHY.md"
)

REPORT_PATH = os.path.join(os.path.dirname(BIBLIO_PATH), "bibliography_verification_report.md")


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


LINK_REGEX = re.compile(r"\[([^\]]+)\]\((https?://[^\)]+)\)")


def extract_entries(md_text: str):
    entries = []
    current_section = None
    current_item = None

    lines = md_text.splitlines()
    for i, line in enumerate(lines):
        # Section headers like '## Government and Official Sources'
        if line.startswith("## "):
            current_section = line[3:].strip()
            continue

        # Subsection headers like '### U.S. Department of Veterans Affairs'
        if line.startswith("### "):
            current_item = line[4:].strip()
            continue

        # Item title line like '- **VA AI Use Case Inventory** — ...'
        if line.lstrip().startswith("- **"):
            # Extract bold title inside ** **
            m = re.search(r"\*\*(.*?)\*\*", line)
            if m:
                current_item = m.group(1).strip()

        # Lines with 'URL:' or 'URLs:' containing markdown links
        if "URL:" in line or "URLs:" in line:
            for label, url in LINK_REGEX.findall(line):
                entries.append(
                    {
                        "section": current_section,
                        "item": current_item,
                        "label": label.strip(),
                        "url": url.strip(),
                        "line": i + 1,
                    }
                )

    return entries


def request_url(url: str, timeout: int = 20):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        )
    }

    # Try HEAD first
    try:
        req = urllib.request.Request(url, headers=headers, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = resp.getcode()
            content_type = resp.headers.get("Content-Type", "").lower()
            return status, content_type, b""
    except Exception:
        # Fallback: GET small range
        try:
            req = urllib.request.Request(url, headers=headers)
            req.add_header("Range", "bytes=0-16383")  # first 16KB
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                status = resp.getcode()
                content_type = resp.headers.get("Content-Type", "").lower()
                content = resp.read(16384)
                return status, content_type, content
        except urllib.error.HTTPError as e:
            return e.code, e.headers.get("Content-Type", "").lower() if e.headers else "", b""
        except Exception as e:
            return None, "", b""


STOPWORDS = {
    "the",
    "and",
    "of",
    "for",
    "to",
    "in",
    "on",
    "by",
    "with",
    "report",
    "press",
    "release",
    "company",
    "ai",
    "genai",
}


def significant_words(text: str):
    words = re.findall(r"[A-Za-z][A-Za-z\-]{2,}", text.lower())
    return [w for w in words if w not in STOPWORDS and len(w) >= 4]


def guess_expected_terms(entry) -> list:
    # Prefer label; fallback to item
    raw = entry.get("label") or entry.get("item") or ""
    # Remove punctuation and generic words
    words = significant_words(raw)
    # Keep up to first 6 significant words to avoid overfitting
    return words[:6]


def content_matches(expected_terms: list, content_sample: str) -> bool:
    if not expected_terms:
        return True
    text = content_sample.lower()
    # Require at least 2 distinct expected terms to be present for a match
    matches = sum(1 for term in set(expected_terms) if term in text)
    return matches >= 2 or (len(expected_terms) == 1 and expected_terms[0] in text)


def is_pdf_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.path.lower().endswith(".pdf")


def verify_entry(entry):
    url = entry["url"]
    status, content_type, content = request_url(url)
    reason = []
    ok = True

    if status is None:
        return False, "request failed (no response)"

    if not (200 <= int(status) < 400):
        ok = False
        reason.append(f"HTTP {status}")

    if is_pdf_url(url):
        if "pdf" not in content_type:
            ok = False
            reason.append(f"expected PDF, got '{content_type or 'unknown'}'")
        # content validation for PDFs is limited; rely on content-type
        return ok, "; ".join(reason) if reason else "ok"

    # For HTML/content pages, try to validate expected terms
    expected = guess_expected_terms(entry)

    sample_text = ""
    if content:
        try:
            sample_text = content.decode("utf-8", errors="ignore")
        except Exception:
            sample_text = ""

    if not sample_text:
        # Try a small GET without Range if we didn't get any body yet
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=20) as resp:
                sample_text = resp.read(24576).decode("utf-8", errors="ignore")
        except Exception:
            sample_text = ""

    if not content_matches(expected, sample_text):
        ok = False
        reason.append(
            "content does not appear to contain expected terms: "
            + ", ".join(expected) if expected else "<none>"
        )

    if "html" not in content_type and sample_text:
        # Some sites omit content-type; do not fail solely on this
        pass

    return ok, "; ".join(reason) if reason else "ok"


def main():
    md = read_file(BIBLIO_PATH)
    entries = extract_entries(md)
    results = []
    for entry in entries:
        ok, reason = verify_entry(entry)
        results.append({**entry, "ok": ok, "reason": reason})
        # Be polite to servers
        time.sleep(0.3)

    bogus = [r for r in results if not r["ok"]]

    # Write report
    lines = []
    lines.append("# Bibliography Link Verification Report\n")
    lines.append(f"Source file: {BIBLIO_PATH}\n")
    lines.append(f"Total links checked: {len(results)}\n")
    lines.append(f"Bogus links: {len(bogus)}\n")
    lines.append("")

    lines.append("## Bogus Links\n")
    if bogus:
        lines.append("| Section | Item | Label | URL | Reason | Line |\n")
        lines.append("|---|---|---|---|---|---|\n")
        for r in bogus:
            lines.append(
                f"| {r['section'] or ''} | {r['item'] or ''} | {r['label'] or ''} | {r['url']} | {r['reason']} | {r['line']} |"
            )
        lines.append("")
    else:
        lines.append("None\n")

    lines.append("## All Results\n")
    lines.append("| OK | Section | Item | Label | URL | Content-Type/Reason | Line |\n")
    lines.append("|---:|---|---|---|---|---|---:|\n")
    for r in results:
        lines.append(
            f"| {'yes' if r['ok'] else 'no'} | {r['section'] or ''} | {r['item'] or ''} | {r['label'] or ''} | {r['url']} | {r['reason']} | {r['line']} |"
        )

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Wrote report to {REPORT_PATH}")


if __name__ == "__main__":
    main()


