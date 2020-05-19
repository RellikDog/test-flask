from math import sqrt
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('win-predictor.html')

@app.route('/solve', methods=['POST'])
def solve():
    user_data = request.json
    a1 = user_data['a1']
    a2 = user_data['a2']
    a3 = user_data['a3']
    a4 = user_data['a4']
    a5 = user_data['a5']
    b1 = user_data['b1']
    b2 = user_data['b2']
    b3 = user_data['b3']
    b4 = user_data['b4']
    b5 = user_data['b5']
    team_a = [a1, a2, a3, a4, a5]
    team_b = [b1, b2, b3, b4, b5]
    prediction = pred(team_a, team_b)
    return jsonify({'prediction': prediction})

def pred(a, b):
    print(a, b)
    return 'Team A wins!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

