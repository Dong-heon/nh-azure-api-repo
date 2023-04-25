from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# OpenAI API key
openai.api_key = "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"

# GPT-3 engine ID
model_engine = "text-davinci-003"

# ChatGPT function
def chat(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

#API test
@app.route('/')
def hello():
    return 'Hello, World!'

# API endpoint
@app.route('/api/chat', methods=['POST'])
def api_chat():
    # Get JSON request data
    request_data = request.get_json()

    # Get prompt from request data
    prompt = request_data['prompt']

    # Generate chat response using ChatGPT function
    response = chat(prompt)

    # Return response in JSON format
    return jsonify({'response': response})

# Run app
if __name__ == '__main__':
    app.run()
