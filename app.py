from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder="templates")  # ✅ Ensures templates are served

@app.route('/')
def home():
    return render_template("index.html")  # ✅ This serves the frontend

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

@app.route('/bfhl', methods=['POST'])
def post_data():
    if not request.json or "data" not in request.json:
        return jsonify({"error": "Invalid request"}), 400

    data = request.json.get("data", [])
    numbers = [x for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]
    highest_alphabet = max(alphabets, key=str.lower) if alphabets else []

    response = {
        "is_success": True,
        "user_id": "22BCS13692",
        "email": "22BCS13692@CUCHD.IN",
        "roll_number": "13692",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": [highest_alphabet] if highest_alphabet else []
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
