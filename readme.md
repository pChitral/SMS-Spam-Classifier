# SMS Classifier

A machine learning model that classifies text messages as either "spam" or "ham" using natural language processing techniques. This repository contains the code for training the model, as well as a web app that allows users to input text messages and receive a classification.

The web app is deployed on Heroku and can be accessed at [INSERT HEROKU APP URL HERE].

## Table of Contents

- [SMS Classifier](#sms-classifier)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
  - [Installation](#installation)
  - [Model Training](#model-training)
  - [Technologies Used](#technologies-used)
  - [Contributing](#contributing)
  - [License](#license)

## Usage

To use the web app, simply navigate to [INSERT HEROKU APP URL HERE]. Input a text message and click "Classify". The app will return a classification of either "spam" or "ham".

## Installation

To install and run the web app locally, follow these steps:

1. Clone this repository: `git clone [INSERT REPO URL HERE]`
2. Navigate into the repository: `cd sms-classifier`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the app: `python app.py`
5. Navigate to `http://localhost:5000` in your web browser to use the app.

Note: The app requires a trained machine learning model to classify text messages. By default, the app will use a pre-trained model that is included in the repository. However, if you wish to train your own model, follow the instructions in the "Model Training" section below.

## Model Training

To train a new machine learning model, follow these steps:

1. Ensure that the training data is in the correct format (see `data/spam.csv` for an example)
2. Run the `train_model.py` script to train the model: `python train_model.py`
3. The trained model will be saved as a `.pkl` file in the `models/` directory.

Note: The `train_model.py` script uses scikit-learn's `Pipeline` and `GridSearchCV` classes to optimize the model's hyperparameters. You may wish to modify these classes to further optimize the model.

## Technologies Used

- Python
- Flask
- Heroku
- scikit-learn
- pandas
- numpy

## Contributing

If you would like to contribute to this project, feel free to submit a pull request. However, please note that we have a code of conduct, which you can find in the `CODE_OF_CONDUCT.md` file.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.