from flask import Flask, jsonify, request
from o_que_le_agora import rss_use_case

app = Flask(__name__)


@app.route('/posts/<rss_identifier>')
def get_feed_posts(rss_identifier):
    posts = rss_use_case.get_posts_from_rss(rss_identifier)
    print(f'app.py - 200 - get_posts - For {rss_identifier} got {len(posts)} posts')
    return jsonify(posts)

@app.route('/rss', methods=['POST', 'GET'])
def rss():
    if request.method == 'POST':
        payload = request.get_json()
        result = rss_use_case.save_rss_url(payload)
        if (not result):
            print(f'app.py - 201 - add_site_feed - Added {payload["rss_identifier"]}')
            return {}, 201
        else:
            print(f'app.py - 400 - add_site_feed - {result}')
            return {'error': result}, 400
    if request.method == 'GET':
        result = rss_use_case.get_all_rss_identifier()
        print(f'app.py - 200 - /rss -  Got {len(result)} rss identifiers')
        return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")