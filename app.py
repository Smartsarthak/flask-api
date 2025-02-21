@app.route('/bfhl', methods=['POST'])
def post_data():
    print("Received request:", request.json)  # Debug print
    if not request.json or "data" not in request.json:
        return jsonify({"error": "Invalid request"}), 400  # Handle missing data
    
    data = request.json.get("data", [])
    print("Processed Data:", data)  # Debug print

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
    print("Response Sent:", response)  # Debug print
    return jsonify(response), 200
