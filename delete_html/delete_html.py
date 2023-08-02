html = """
<html>
<body>
これは<a href="http://example.com">Example</a>です。
</body>
</html>"""
from bs4 import BeautifulSoup
def clean_html(html, strip=False):
  soup = BeautifulSoup(html, 'html.parser')
  text = soup.get_text(strip=strip)
  return text
clean_html(html)