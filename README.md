# Twitter Sentiment Analysis

#### Warning

_The Wikipedia API might not work all the time depending on the entered search term._
<br>

![App](https://user-images.githubusercontent.com/29514438/59224071-1eb0f600-8beb-11e9-9d93-b648441af4d2.PNG)

This is a web app which can be used to **analyze users' sentiments across Twitter hashtags**. Its created using React and Django and uses an LSTM model trained on the [Kaggle Sentiment140 dataset](https://www.kaggle.com/kazanova/sentiment140) and served as a REST API to the ReactJS frontend.

The server pulls tweets using **tweepy** and performs inference using Keras. It also pulls data from the **Wikipedia API** based the hashtag chosen to display a short description. As part of the analysis, I also added few examples of the tweets and their predicted sentiments. A kernel for another sentiment classification using a CNN + 1D pooling can be found [here](https://www.kaggle.com/thatawkwardguy/twitter-sentiment-classification-using-cnns)

![Untitled Diagram (6)](https://user-images.githubusercontent.com/29514438/59569258-5f55b700-90a4-11e9-8167-60f53a765c02.jpg)

## How to Use

### Running the application

1. Download the [trained model](https://drive.google.com/file/d/1ckK5m4JysFKtBuC9yCnEaHe6cxOgXlG8/view?usp=sharing) and put into the `server/main` folder <br>(**Note:** _This is the CNN model. f you want use the LSTM model, you'll need to follow the training steps below and put the saved model in `server/main`. Also, don't forget to change the loaded model name in `server/main/init.py`_ )

2. Run `python -m venv venv` in the terminal from the `server` folder to create a Python virtual environment <br> (**Note:** _Ensure that you have Python version 3.7 or higher_)

3. Run `venv/scripts/activate` and `pip install -r requirements.txt` while still being in `server` folder to switch to virtual env & install all the required packages

4. Start the Flask server by running `python app.py`

5. Open `http://localhost:8000` in your browser to access the app

### Updating front-end app

1. Run `npm install` in `client` folder to download all the dependent noad modules

2. Make the changes in `client/src` folder as required

3. Check the front-end related changes by running `npm start` & open `http://localhost:5000` in your browser

4. Run `npm run build` after all the changes are made to create optimized production build

### Training the model

1. Download the [Kaggle Sentiment140 dataset](https://www.kaggle.com/kazanova/sentiment140) and put it in the root folder as `sentiment140.csv`.
2. Run the code blocks given in the Jupyter Notebook
