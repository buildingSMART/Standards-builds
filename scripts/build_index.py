"""Resolve index.html file URLs against the checkout; directories are assumed valid."""

import argparse
import html
from pathlib import Path
import re
from urllib.parse import quote, unquote, urlsplit, urlunsplit


URL_ATTRIBUTE = re.compile(r'\b(?:href|src)\s*=\s*([\'"])(.*?)\1', re.IGNORECASE)
HOST = "standards.buildingsmart.org"


def render(source: str, root: Path) -> str:
    errors = []
    checked = 0

    def replace(match):
        nonlocal checked
        url = urlsplit(html.unescape(match[2]))
        if url.netloc and url.netloc.lower() != HOST:
            return match[0]
        if url.scheme and url.scheme not in ("http", "https"):
            return match[0]
        path = unquote(url.path).lstrip("/")
        # Directory URLs (including extensionless HTML directories) stay intact.
        if not path or not Path(path).suffix:
            return match[0]
        if ".." in Path(path).parts:
            errors.append(f"Path escapes the site root: {path}")
            return match[0]
        matches = sorted(p for p in root.glob(path) if p.is_file())
        checked += 1
        if len(matches) != 1:
            errors.append(f"{path}: expected exactly one file, found {len(matches)}"
                          + "".join(f"\n  {p.relative_to(root).as_posix()}" for p in matches))
            return match[0]
        resolved = quote(matches[0].relative_to(root).as_posix(), safe="/")
        if url.path.startswith("/"):
            resolved = "/" + resolved
        new_url = urlunsplit((url.scheme, url.netloc, resolved, url.query, url.fragment))
        start, end = match.start(2) - match.start(), match.end(2) - match.start()
        return match[0][:start] + html.escape(new_url, quote=True) + match[0][end:]

    result = URL_ATTRIBUTE.sub(replace, source)
    if errors:
        raise ValueError("URL validation failed:\n" + "\n".join(errors))
    print(f"Validated {checked} file URLs (one match each).")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    if args.output.resolve() == root / "index.html":
        parser.error("output must differ from the source index.html")
    try:
        result = render((root / "index.html").read_text(encoding="utf-8"), root)
    except ValueError as error:
        parser.exit(1, f"{error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(result, encoding="utf-8")


if __name__ == "__main__":
    main()
