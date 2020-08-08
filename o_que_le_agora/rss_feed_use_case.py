from store import store


def save_feed_url(feed):
    if('feed_identifier' in feed.keys() and 'feed_url' in feed.keys()):
        store.save_feed_url(feed['feed_identifier'], feed['feed_url'])
    else:
        return 'Missing required fields'