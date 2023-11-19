from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

def generate_random_string():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

@app.route('/test')
def generate_json():
    random_strings = [generate_random_string() for _ in range(1000)]
    response_data = {'random_strings': random_strings}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
