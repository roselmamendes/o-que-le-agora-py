from store import store
from feed.reader import get_rss_feed_for

def save_rss_url(rss):
    if('rss_identifier' in rss.keys() and 'rss_url' in rss.keys()):
        store.save_rss_url(rss['rss_identifier'], rss['rss_url'])
    else:
        return 'Missing required fields'

def get_posts_from_rss(rss_identifier):
    posts = []
    url = store.get_rss_url(rss_identifier)
    if(url):
        rss_feed = get_rss_feed_for(url)
        posts = rss_feed['entries']
    return posts