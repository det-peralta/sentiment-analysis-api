# finbert sentiment analysis flask api

this project provides a flask api for sentiment analysis on financial texts using the finbert model, a bert-based model pre-trained on financial texts. it's designed to offer easy-to-use http endpoints for processing financial texts to detect sentiments, making it suitable for integrating sentiment analysis into financial applications.

## features

- sentiment analysis using the finbert model
- easy-to-use http post endpoint for analyzing lists of texts
- scalable and production-ready with docker deployment

## prerequisites

before you begin, ensure you have met the following requirements:

- docker and docker compose installed on your machine
- basic knowledge of docker and flask applications

## installation

to set up the project for development or deployment, follow these steps:

clone the repository:

```bash
git clone https://github.com/your-username/finbert-flask-analyzer.git
cd finbert-flask-analyzer
```

## build and run with docker

use docker compose to build and run the application:

```bash
docker-compose up --build
```

this command builds the docker image and starts the flask application inside a docker container, making it accessible on http://localhost:5000.

## usage

to use the api for sentiment analysis, send a post request to the `/analyze` endpoint with a json body containing a list of texts you want to analyze. example using curl:

```bash
curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d '{"texts": ["This company financial performance is outstanding.", "The market is facing a severe downturn."]}'
```

the api will return a json response with the sentiment analysis results.

## development

for local development, you can run the flask application outside docker by first installing the required python packages:

```bash
pip install -r requirements.txt
```

then, set the flask application environment variables and run the server:

```bash
export FLASK_APP=your_flask_app.py
export FLASK_ENV=development
flask run
```

## contributing

contributions to improve the project are welcome. please follow these steps to contribute:

- fork the repository
- create a new branch (`git checkout -b feature/amazingfeature`)
- commit your changes (`git commit -m 'add some amazingfeature'`)
- push to the branch (`git push origin feature/amazingfeature`)
- open a pull request

## license

distributed under the mit license. see license for more information.

## contact

det-peralta@outlook.com

project link: <https://github.com/det-peralta/sentiment-analysis-api>

