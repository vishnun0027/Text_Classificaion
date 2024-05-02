from flask import Flask, request, jsonify
from text_classificaion import classify_text
import time

app = Flask(__name__)

@app.route('/classify', methods=['POST'])

def classify():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided', "status": False}), 400
    start_time = time.time()
    try:
        label = classify_text(text)
    except Exception as e:
        return jsonify({'error': str(e), "status": False}), 500
    end_time = time.time()
    processing_time = round((end_time - start_time),2)
    return jsonify({'label': label, "processing_time":processing_time,"status": True})

if __name__ == '__main__':
    app.run(debug=True)

    