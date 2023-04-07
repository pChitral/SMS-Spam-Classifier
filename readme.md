# SMS Classifier

A machine learning model that classifies text messages as either "spam" or "ham" using natural language processing techniques. This repository contains the code for training the model, as well as a web app that allows users to input text messages and receive a classification.

The web app is deployed on Heroku and can be accessed at [[ HEROKU APP](https://chitralpatil-spam-classifier.herokuapp.com/)].

## Table of Contents

- [SMS Classifier](#sms-classifier)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
  - [Installation](#installation)
  - [Model Training](#model-training)
  - [Technologies Used](#technologies-used)
  - [Contributing](#contributing)
  - [License](#license)
  - [Files](#files)

## Usage

To use the web app, simply navigate to [[HEROKU APP](https://chitralpatil-spam-classifier.herokuapp.com/)]. Input a text message and click "Predict". The app will return a classification of either "spam" or "ham" along with the probability of the prediction.

## Installation

To install and run the web app locally, follow these steps:

1. Clone this repository: `git clone https://github.com/pChitral/SMS-Spam-Classifier.git`
2. Navigate into the directory where the git clone was executed: `cd your_foldername`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the app: `sms_classifier.ipynb` to get the model in the pkl format.
5. Execute `streamlit run app.py` on your termial
6. Navigate to Local URL: `http://localhost:8501` in your web browser to use the app.

Note: The app which I've deployed on heroku uses a trained machine learning model to classify text messages. By default, the app will use a pre-trained model that is included in the repository. However, if you wish to train your own model, follow the instructions in the "Model Training" section below. 

## Model Training

To train a new machine learning model, follow these steps:

1. Ensure that the training data is in the correct format (see `data/spam.csv` for an example)
2. Run the desired model that you want.
3. The trained model will be saved as a `.pkl` file in the same directory.

You may wish to modify these classes to further optimize the model.

## Technologies Used

- Python
- Sreamlit
- Heroku
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn
- nltk


## Contributing

If you would like to contribute to this project, feel free to submit a pull request. However, please note that we have a code of conduct, which you can find in the `CODE_OF_CONDUCT.md` file.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Files

The following files are included in this repository:

- `CODE_OF_CONDUCT.md`: Guidelines for contributing to this project.
- `LICENSE.md`: The license under which this project is released.
- `Procfile`: A file for deploying the app to Heroku.
- `app.py`: The script that runs the web app.
- `data/`: A directory containing the dataset used for training the model.
- `logo.png`: A logo for the web app.
- `model.pkl`: A trained machine learning model used for classification.
- `nltk.txt`: A file containing necessary dependencies for NLP processing.
- `readme.md`: The documentation for the project.
- `requirements.txt`: A list of Python dependencies required for
