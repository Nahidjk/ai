# app.py
from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = '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'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']

    # Use OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=150
    )

    return response['choices'][0]['text']

if __name__ == '__main__':
    app.run(debug=True)
