# SaaS platform - Flask app.py
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='iot_logs.log', level=logging.INFO, format='%(asctime)s - %(message)s')

@app.route('/iot_logs', methods=['POST'])
def handle_iot_logs():
    """ Handle logs from IoT devices """
    try:
        log_data = request.get_json()
        # Log the message from the device
        logging.info(f"{log_data['device_id']} - {log_data['message']}")
        return jsonify({'message': 'Log received successfully'})
    except Exception as e:
        logging.error(f"Error processing log: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
