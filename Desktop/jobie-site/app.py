from flask import Flask, jsonify, send_from_directory
from bs4 import BeautifulSoup
import os
import json

app = Flask(__name__, static_folder='assets')
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def home():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/<path:filename>')
def serve_static_pages(filename):
    if os.path.exists(os.path.join(BASE_DIR, filename)):
        return send_from_directory(BASE_DIR, filename)
    return "Page Not Found", 404

@app.route('/api/jobs', methods=['GET'])
def api_jobs():
    json_path = os.path.join(BASE_DIR, 'jobs_data.json')
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            jobs = json.load(f)
        return jsonify({"status": "success", "total_jobs": len(jobs), "jobs": jobs})
    return jsonify({"status": "error", "message": "No job data found"}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
