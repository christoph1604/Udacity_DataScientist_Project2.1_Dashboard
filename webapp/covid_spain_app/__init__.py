from flask import Flask

app = Flask(__name__)

from covid_spain_app import routes
