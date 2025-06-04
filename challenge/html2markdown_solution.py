import re
test_html = "<p>This is <em>important</em> and   a <a href=\"https://example.com\">link</a></p>"

ITALICS = re.compile(r'<em>(.+?)</em>')
SPACES = re.compile(r'\s+')
PARAGRAPHS = re.compile(r'<p>(.+?)</p>')
URLS = re.compile(r'<a href="(.+?)">(.+?)</a>')

def html2markdown(html):
    '''Take in html text as input and return markdown'''
    markdown = ITALICS.sub(r'*\1*', html)
    markdown = SPACES.sub(r' ', markdown)
    markdown = PARAGRAPHS.sub(r'\1\n\n', markdown)
    markdown = URLS.sub(r'[\2](\1)', markdown)
    return markdown.strip()

# Test cases
print(html2markdown(test_html))  # Should return 'This is in italics. So is this'
