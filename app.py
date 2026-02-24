from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
import os

app = Flask(__name__)
# Enable CORS so the frontend can send data to this backend
CORS(app) 

# The endpoint that matches the fetch() URL in your JavaScript
@app.route('/save-location', methods=['POST'])
def save_location():
    # Get the JSON data sent from the frontend
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data received"}), 400

    lat = data.get('lat')
    lon = data.get('lon')
    timestamp = data.get('timestamp')

    print(f"Received Location -> Lat: {lat}, Lon: {lon} at {timestamp}")

    # Save the data to a CSV file
    file_exists = os.path.isfile('student_locations.csv')
    
    with open('student_locations.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write headers if the file is being created for the first time
        if not file_exists:
            writer.writerow(['Timestamp', 'Latitude', 'Longitude'])
            
        writer.writerow([lat, lon])

    # Send a success response back to the browser
    return jsonify({"message": "Location securely saved."}), 200

if __name__ == '__main__':
    # Run the server on port 5001
    app.run(debug=True, port=5001)