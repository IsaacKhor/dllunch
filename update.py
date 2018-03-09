import feedparser
from bs4 import BeautifulSoup

def _remove_attrs(soup):
    for tag in soup.findAll(True):
        tag.attrs = None
    return soup

feed_loc = 'https://us5.campaign-archive.com/feed?u=a38b89b5f3672bed6f0da3b14&id=a67ff49da0'
parsed_feed = feedparser.parse(feed_loc)
latest_content = parsed_feed.entries[0].content[0].value
soup = BeautifulSoup(latest_content, "html.parser")
pure = _remove_attrs(soup)

print(pure)