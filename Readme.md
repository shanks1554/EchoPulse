# EchoPulse

## Overview
This project focuses on analyzing the sentiment of tweets using natural language processing (NLP) techniques. It classifies tweets into categories such as positive, negative, or neutral, providing insights into public opinion on various topics.

## Features
- Preprocessing of tweet data (removal of stop words, hashtags, mentions, etc.)
- Sentiment classification using machine learning or deep learning models
- Visualization of sentiment trends

## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/EchoPulse.git
    ```

2. Navigate to the project directory:

    ```bash
    cd twitter-sentiment-analysis
    ```

3. Create Virtual Environment:

    ```bash
    conda create -n EchoPulse python=3.11 
    ```

4. Activate Environment:

    ```bash
    conda activate EchoPulse
    ```

5. Install and setup Spacy Library:

    ```bash
    conda install -c conda-forge spacy
    python -m spacy download en_core_web_sm
    ```

6. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Steps to Run the Project


1. **Run data_preprocessing.ipynb to create the processed data and LabelEncoder.**

2. **Run model_creation.ipynb to create the classifier model.**
    
3. **Run the Stremlit script:**
    ```bash
    streamlit app.py
    ```

## Project Structure
- `data/`: Contains datasets for training, testing and validation

- `models/`: Pre-trained or custom models for sentiment analysis

- `requirements.txt`: List of dependencies

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- [spaCy](https://spacy.io/)

- [Scikit-learn](https://scikit-learn.org/)

- [Streamlit](https://streamlit.io/)