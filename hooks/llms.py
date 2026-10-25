from pathlib import Path
from urllib.parse import urljoin

_pages = []


def on_pre_build(config):
    _pages.clear()


def on_page_markdown(markdown, page, config, files):
    page_url = urljoin(config.site_url.rstrip("/") + "/", page.url)
    _pages.append((page.file.src_path, page.title, page_url, markdown.strip()))
    return markdown


def on_post_build(config):
    sections = [
        "# Dropsome Documentation\n\n"
        "This file contains the complete Dropsome documentation. "
        "Each section includes a link to its published page.\n"
    ]

    pages = sorted(_pages, key=lambda page: (page[0] != "index.md", page[0]))
    for _, title, page_url, markdown in pages:
        sections.append(f"\n---\n\n## {title}\n\nSource: {page_url}\n\n{markdown}\n")

    output_path = Path(config.site_dir) / "llms-full.txt"
    output_path.write_text("\n".join(sections), encoding="utf-8")
