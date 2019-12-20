from dotenv import dotenv_values
from flask import Flask

app = Flask(__name__)
app.config.from_mapping(dotenv_values())
