from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/send-data', methods=['POST'])
def send_data():
    data = request.json  # Get JSON data from the request
    print("Received data:", data)

    # Process the data here (e.g., save to database, perform calculations, etc.)

    response = {'message': 'Data received successfully', 'data': data}
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode