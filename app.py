from flask import Flask, jsonify, request
from o_que_le_agora.post_use_case import get_post_list
from o_que_le_agora.rss_feed_use_case import save_feed_url

app = Flask(__name__)


@app.route('/posts/<feed_identifier>')
def get_posts(feed_identifier):
    posts = get_post_list(feed_identifier)
    return jsonify(posts)

@app.route('/feed', methods=['POST'])
def add_site_feed():
    payload = request.get_json()
    result = save_feed_url(payload)

    return ({}, 201) if not result else ({'error': result}, 400)

if __name__ == "__main__":
    app.run(host="0.0.0.0")