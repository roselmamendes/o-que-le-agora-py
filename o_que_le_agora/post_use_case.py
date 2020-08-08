from feed.reader import get_rss_feed_for
from store import store


def get_post_list(feed_identifier):
    posts = []
    url = store.get_feed_url(feed_identifier)
    if(url):
        rss_feed = get_rss_feed_for(url)
        posts = rss_feed['entries']
    return posts