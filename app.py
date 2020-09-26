from flask import Flask, jsonify, request
from o_que_le_agora.rss_feed_use_case import save_feed_url, get_posts_from_feed

app = Flask(__name__)


@app.route('/posts/<feed_identifier>')
def get_feed_posts(feed_identifier):
    posts = get_posts_from_feed(feed_identifier)
    print(f'app.py - 200 - get_posts - For {feed_identifier} got {len(posts)} posts')
    return jsonify(posts)

@app.route('/feed', methods=['POST'])
def add_site_feed():
    payload = request.get_json()
    result = save_feed_url(payload)
    if (not result):
        print(f'app.py - 201 - add_site_feed - Added {payload["feed_identifier"]}')
        return {}, 201
    else:
        print(f'app.py - 400 - add_site_feed - {result}')
        return {'error': result}, 400

if __name__ == "__main__":
    app.run(host="0.0.0.0")