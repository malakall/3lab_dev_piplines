from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/format', methods=['POST'])
def format_text():
    data = request.json
    text = data.get("text", "")
    mode = data.get("mode", "upper")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    if mode == "upper":
        formatted_text = text.upper()
    elif mode == "lower":
        formatted_text = text.lower()
    elif mode == "capitalize":
        formatted_text = text.capitalize()
    else:
        return jsonify({"error": "Invalid mode"}), 400

    return jsonify({"formatted_text": formatted_text})


if __name__ == '__main__':
    app.run(debug=True)
