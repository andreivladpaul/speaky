# Text to Speech Converter

This project is a simple web application that converts text into downloadable MP3 audio files using Amazon Polly. Users can input text, select a voice, and download the generated audio.

## Features
- Convert text to speech using Amazon Polly.
- Choose from multiple voice options.
- Download the generated MP3 file.

## Prerequisites
- **Python 3.7+** installed on your system.
- **AWS Account** with access to Amazon Polly.
- **AWS CLI** installed and configured (optional for testing).
- **Flask** and **Boto3** Python libraries installed.

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/text-to-speech-converter.git
cd text-to-speech-converter
```

### 2. Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### 3. Configure AWS Credentials
Create a file named `aws_credentials.json` in the project root and add your AWS credentials:
```json
{
  "aws_access_key_id": "your_access_key_id",
  "aws_secret_access_key": "your_secret_access_key",
  "region_name": "us-east-1"
}
```

### 4. Run the Application
Start the Flask development server:
```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`.

## Usage
1. Open the application in your browser.
2. Enter the text you want to convert into the text area.
3. Select a voice from the dropdown menu.
4. Click the "Convert to MP3" button.
5. Download the generated MP3 file.

## Testing AWS Polly
To verify your AWS Polly setup, you can use the AWS CLI:
```bash
aws polly list-voices --region us-east-1
```

## Project Structure
```
text-to-speech-converter/
├── app.py                 # Main application file
├── aws_credentials.json   # AWS credentials file (not included in the repo)
├── requirements.txt       # Python dependencies
├── static/
│   └── style.css          # CSS for the application
├── templates/
│   └── index.html         # HTML template for the application
└── README.md              # Project documentation
```

## Notes
- Keep your `aws_credentials.json` file secure and do not share it publicly.
- If you lose your AWS Secret Access Key, you will need to generate a new one in the AWS Management Console.

## License
This project is licensed under the MIT License.
