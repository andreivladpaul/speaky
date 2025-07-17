from flask import Flask, render_template, request, send_file
import boto3
import os
import json
from io import open

app = Flask(__name__)

# Load AWS credentials from the secret file
with open('aws_credentials.json', 'r') as secret_file:
    secrets = json.load(secret_file)

polly_client = boto3.client(
    'polly',
    aws_access_key_id=secrets['aws_access_key_id'],
    aws_secret_access_key=secrets['aws_secret_access_key'],
    region_name=secrets['region_name']
)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_text_to_audio():
    text = request.form.get('text')
    voice_name = request.form.get('voice', 'Joanna')  # Default voice

    if not text:
        return "No text provided", 400

    # Call Amazon Polly to synthesize speech
    response = polly_client.synthesize_speech(
        Text=text,
        VoiceId=voice_name,
        OutputFormat='mp3'
    )

    # Save the audio stream to a file
    output_file = "output.mp3"
    with open(output_file, "wb") as out:
        out.write(response['AudioStream'].read())

    # Serve the file for download
    return send_file(output_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)