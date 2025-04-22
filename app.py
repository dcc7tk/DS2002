from flask import Flask, jsonify, request
from datetime import datetime
import pytz

app = Flask(__name__)

# Token for authentication
API_TOKEN = "secret_token"

# Sample city-to-timezone mapping
CAPITAL_TIMEZONES = {
    "London": "Europe/London",
    "Paris": "Europe/Paris",
    "Tokyo": "Asia/Tokyo",
    "Ottawa": "America/Toronto",
    "Canberra": "Australia/Sydney",
    "New Delhi": "Asia/Kolkata",
    "Washington": "America/New_York",
    "Brasília": "America/Sao_Paulo"
}

# Token required decorator
def token_required(f):
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            if token == API_TOKEN:
                return f(*args, **kwargs)
        return jsonify({"error": "Unauthorized", "message": "Provide a valid Bearer token"}), 401
    decorator.__name__ = f.__name__
    return decorator

# Basic route
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, world!"})

# Protected data
@app.route('/api/secure-data', methods=['GET'])
@token_required
def secure_data():
    return jsonify({"secret": "This is protected info!"})

# Capital city time info
@app.route('/api/time', methods=['GET'])
@token_required
def get_time():
    capital = request.args.get('city')
    if not capital:
        return jsonify({"error": "Missing parameter", "message": "You must specify a capital city using ?city=..." }), 400

    timezone_name = CAPITAL_TIMEZONES.get(capital)
    if not timezone_name:
        return jsonify({"error": "City not found", "message": f"'{capital}' is not recognized. Try: {', '.join(CAPITAL_TIMEZONES.keys())}"}), 404

    tz = pytz.timezone(timezone_name)
    now = datetime.now(tz)
    utc_offset = now.strftime('%z')
    formatted_offset = f"UTC{'+' if int(utc_offset) >= 0 else '-'}{utc_offset[1:3]}:{utc_offset[3:]}"

    return jsonify({
        "city": capital,
        "current_time": now.strftime('%Y-%m-%d %H:%M:%S'),
        "utc_offset": formatted_offset
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)