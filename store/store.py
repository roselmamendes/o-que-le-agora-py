import peewee

database = peewee.SqliteDatabase("o_que_le_agora.db")

class RSSFeed(peewee.Model):
    feed_identifier = peewee.CharField()
    feed_url = peewee.CharField()
    
    class Meta:
        database = database


def save_rss_url(feed_identifier, feed_url):
    rss_feed = RSSFeed(feed_identifier=feed_identifier, feed_url=feed_url)
    rss_feed.save()

def get_rss_url(rss_identifier):
    try:
        rss_feed = RSSFeed.select().where(RSSFeed.feed_identifier==rss_identifier).get()
    except peewee.DoesNotExist:
        return ''
    return rss_feed.feed_url        

def clear_database():
    RSSFeed.delete().execute()

try:
    RSSFeed.create_table()
except peewee.OperationalError:
    print("RSSFeed table already exists!")
    