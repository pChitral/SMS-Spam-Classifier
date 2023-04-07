import streamlit as st
import pickle
import nltk
from nltk.stem.porter import PorterStemmer

# Load the trained model and vectorizer
stemmer = PorterStemmer()
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Define a function to preprocess the input text


def preprocess_text(text):
    import string

    # Convert text to lowercase and tokenize into words
    words = nltk.word_tokenize(text.lower())

    # Remove stopwords and punctuation
    stopwords_set = set(nltk.corpus.stopwords.words('english'))
    words = [
        w for w in words if w not in stopwords_set and w not in string.punctuation]

    # Stem words using PorterStemmer
    words = [stemmer.stem(w) for w in words]

    # Join the preprocessed words into a single string
    return " ".join(words)

# Define a function to make predictions


def predict_spam(input_text):
    # Preprocess the input text
    preprocessed_text = preprocess_text(input_text)

    # Vectorize the preprocessed text
    vector_input = tfidf.transform([preprocessed_text])

    # Make the prediction
    prediction = model.predict(vector_input)[0]

    # Get the prediction probability
    prediction_prob = model.predict_proba(vector_input)[0][1]

    return prediction, prediction_prob

# Define the Streamlit app


def app():
    # Set the app title and favicon
    st.set_page_config(page_title='Spam Classifier', page_icon=':envelope:')

    # Add a header with the app title
    st.write('# Spam Classifier')
    st.write('---')

    # Add a logo
    st.image('logo.png', width=200)

    # Add a text input field for the user to enter their message
    input_sms = st.text_input('Enter your message here:')

    # Add input validation
    if not input_sms:
        st.warning('Please enter a message.')
        st.stop()

    # Add instructions
    st.write('Please enter a message to predict if it is spam or not.')
    st.write('---')

    # Add a predict button
    if st.button('Predict'):
        # Add a loading spinner while the prediction is being made
        with st.spinner('Predicting...'):
            # Make the prediction
            prediction, prediction_prob = predict_spam(input_sms)

        # Display the prediction result
        if prediction == 1:
            st.error(
                f'This message is spam with a probability of {prediction_prob:.2f}.')
        else:
            st.success(
                f'This message is not spam with a probability of {1 - prediction_prob:.2f}.')

    # Add a reset button to clear the input field
    if st.button('Reset'):
        input_sms = ''
        st.warning('Input field cleared.')

    # Add a horizontal line to separate the sections
    st.write('---')

    # Add some styling to the footer
    st.markdown('<p style="font-size:10px; font-style:italic; text-align:center;">Built with Streamlit by Your Name</p>', unsafe_allow_html=True)


if __name__ == '__main__':
    app()
