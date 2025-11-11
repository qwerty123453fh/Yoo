from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = 'YOUR_API_KEY'

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': user_input}]
    )
    return jsonify({'response': response.choices[0].message['content']})

if __name__ == '__main__':
    app.run(debug=True)