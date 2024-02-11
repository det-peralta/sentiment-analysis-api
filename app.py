from flask import Flask, request, jsonify
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

app = Flask(__name__)

# Load model and tokenizer outside of request handling to improve performance
model_name = "ProsusAI/finbert"
model = AutoModelForSequenceClassification.from_pretrained(model_name).eval()  # Ensure model is in eval mode
tokenizer = AutoTokenizer.from_pretrained(model_name)

@app.route('/analyze', methods=['POST'])
def analyze():
    if not request.json or 'texts' not in request.json:
        return jsonify({"error": "Please provide a 'texts' field with a list of strings."}), 400

    texts = request.json['texts']
    if not isinstance(texts, list) or not all(isinstance(text, str) for text in texts):
        return jsonify({"error": "The 'texts' field must be a list of strings."}), 400

    try:
        inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            logits = model(**inputs).logits
        predictions = torch.softmax(logits, dim=-1).tolist()
        return jsonify(predictions)
    except Exception as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify({"error": "Failed to process request."}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
