from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

@app.route('/bfhl', methods=['POST'])
def post_data():
    data = request.json.get("data", [])

    # Separate numbers and alphabets
    numbers = [x for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]
    
    # Find the highest alphabet (last in A-Z order, case-insensitive)
    highest_alphabet = max(alphabets, key=str.lower) if alphabets else []

    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": [highest_alphabet] if highest_alphabet else []
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
