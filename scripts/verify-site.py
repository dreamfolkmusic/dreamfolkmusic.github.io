"""Verify the redesign's preservation requirements without third-party packages."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = '94e2ae6c1db342be1cf951a1754a3234092bcb35'
class Page(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.tags = []
        self.stack = []
        self.errors = []
        self.feed(html)
        assert not self.stack, self.stack
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))
        if tag not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}:
            self.stack.append(tag)
    def handle_endtag(self, tag):
        assert self.stack and self.stack.pop() == tag, f'Unbalanced closing {tag}'

def original(path):
    return subprocess.check_output(['git', 'show', f'{BASE}:{path}'], cwd=ROOT, text=True)

html = (ROOT / 'index.html').read_text()
page = Page(html)
before = Page(original('index.html'))
ids = [attrs['id'] for _, attrs in page.tags if 'id' in attrs]
assert len(ids) == len(set(ids)), 'Duplicate IDs'
assert sum(tag == 'h1' for tag, _ in page.tags) == 1
assert sum(tag == 'main' for tag, _ in page.tags) == 1
for tag, attrs in page.tags:
    for key in ('href', 'src', 'srcset'):
        url = attrs.get(key, '')
        if url.startswith('#'):
            assert url[1:] in ids, f'Missing target: {url}'
        elif url and not url.startswith(('https:', 'mailto:')):
            assert (ROOT / url).is_file(), f'Missing asset: {url}'
    if tag == 'img':
        assert 'alt' in attrs, 'Image missing alt attribute'
    for key in ('aria-labelledby',):
        for target in attrs.get(key, '').split():
            assert target in ids, f'Missing accessible label: {target}'

def external_links(p):
    return Counter(a['href'] for t, a in p.tags if t == 'a' and a.get('href', '').startswith(('https:', 'mailto:')))
assert set(external_links(page)) == set(external_links(before)), 'Changed official links'
assert all(external_links(page)[url] >= count for url, count in external_links(before).items()), 'Removed original link'
old_beacon = re.search(r'<!-- Cloudflare Web Analytics -->.*?<!-- End Cloudflare Web Analytics -->', original('index.html'), re.S).group()
assert html.count(old_beacon) == 1
assert html.count('static.cloudflareinsights.com/beacon.min.js') == 1
assert html.split(old_beacon)[1].strip() == '</body></html>'
meta = lambda p: [a for t, a in p.tags if t in ('meta','link') and a.get('name') != 'theme-color']
assert meta(page) == meta(before), 'SEO metadata changed'
extract_schema = lambda h: json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S).group(1))
assert extract_schema(html) == extract_schema(original('index.html'))
for file in ('CNAME','robots.txt','sitemap.xml','assets/favicon.svg'):
    assert (ROOT / file).read_text() == original(file), f'Changed {file}'
ET.parse(ROOT / 'sitemap.xml')
assert 'Debut single coming soon' in html and 'No release date announced' in html
assert not re.search(r'Perfect Strangers|spotify\.com|music\.apple\.com|<audio|<form', html, re.I)
for asset in re.findall(r"url\(['\"]?([^)'\"]+)", (ROOT / 'styles.css').read_text()):
    if asset.startswith('#'):
        assert asset[1:] in ids, f'Missing CSS filter: {asset}'
    else:
        assert (ROOT / asset).is_file(), f'Missing CSS resource: {asset}'
print('PASS: balanced HTML; unique IDs; one h1/main; local assets; anchors/labels; unchanged music/social/contact URLs; exact analytics; preserved SEO/JSON-LD/domain files; no fabricated release links/title/audio/signup.')
