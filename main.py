from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/ipinfo')
def index():
    # Get the user's IP address from the request object
    user_ip = request.remote_addr

    # Make a request to the ipinfo.io API to get geolocation information
    api_url = f'https://ipinfo.io/{user_ip}/json'
    response = requests.get(api_url)

    # Parse the JSON response
    data = response.json()

    # Extract relevant information (you can customize this based on your needs)
    ip = data.get('ip', 'N/A')
    city = data.get('city', 'N/A')
    region = data.get('region', 'N/A')
    country = data.get('country', 'N/A')
    location = data.get('loc', 'N/A')

    # Display the information
    result = {
        'IP': ip,
        'City': city,
        'Region': region,
        'Country': country,
        'Location': location
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
