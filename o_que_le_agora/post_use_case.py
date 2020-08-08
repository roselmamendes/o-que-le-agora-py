from feed.reader import get_rss_feed_for
from store import store


def get_post_list(feedIdentifier):
    posts = []
    url = store.get_feed_url(feedIdentifier)
    if(url):
        rss_feed = get_rss_feed_for(url)
        posts = rss_feed['entries']
    return posts