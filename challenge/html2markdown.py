
import re
test_html = "<p>This is <em>important</em> and a <a href=https://example.com>link</a>.</p>"

remove_italics = re.compile(r'<em>(.*?)</em>') #remove italics
remove_whitespace = re.compile(r'\t+|\s+') # global whitespace
remove_paragraphs = re.compile(r'<p>(.*?)</p>') #remove paragraphs
link_pattern = re.compile(r'<a\href="(.*?)">(.*?)</a>')

def html2markdown(html):
    '''Take in html text as input and return markdown'''
    replaced = remove_whitespace.sub(r'*\1*', html)
    replaced = remove_italics.sub(r'\1', replaced)    
    replaced = remove_paragraphs.sub(r'\1\n', replaced)
    replaced = link_pattern.sub(r'[\2](\1)', replaced)
    return replaced.stip() # Return the final markdown text without leading/trailing whitespace

# Test cases
print(html2markdown(test_html))  # Should return 'This is in italics. So is this'
