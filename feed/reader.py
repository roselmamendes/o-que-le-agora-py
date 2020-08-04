import feedparser


def get_rss_feed_for(url, feed_parser=feedparser):
    return feed_parser.parse(url)