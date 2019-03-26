from flask import Flask
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='')

app = Flask(__name__)
from app import views