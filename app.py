from flask import Flask, request, jsonify
from match_data import get_match_data as generate_match_poster_by_id

app = Flask(__name__)

@app.route('/generate_poster', methods=['POST'])
def generate_poster():
    data = request.json
    match_id = data.get('match_id')
    if not match_id:
        return jsonify({'error': 'match_id is required'}), 400
    
    try:
        result = generate_match_poster_by_id(match_id)
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
