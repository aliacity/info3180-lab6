from flask import Flask
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='ebaf80aa3ba04c4ab977be6d14771cd2')

app = Flask(__name__)
from app import views