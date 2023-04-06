# SMS Classifier

A simple web app that classifies SMS messages as spam or ham (not spam).

## Getting Started

### Prerequisites

- Python 3.6+
- Flask
- Scikit-learn
- NLTK

### Installing

1. Clone the repository: `[git clone https://github.com/yourusername/sms-classifier.git](https://github.com/pChitral/SMS-Spam-Classifier.git)`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python app.py`

The app will be available at http://localhost:5000.

### Deployment

The app is currently deployed on Heroku at 'https://chitralpatil-spam-classifier.herokuapp.com/'.

To deploy your own instance of the app on Heroku:

1. Create a Heroku account and install the Heroku CLI.
2. Log in to Heroku using the CLI: `heroku login`.
3. Create a new Heroku app: `heroku create`.
4. Push the code to the Heroku remote: `git push heroku master`.
5. Scale the web process: `heroku ps:scale web=1`.
6. Open the app in your browser: `heroku open`.

## Usage

Enter a message into the text box and click the "Classify" button to classify it as spam or ham.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
