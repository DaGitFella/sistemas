from flask import Flask
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "123"
app.permanent_session_lifetime = timedelta(minutes=5) #defines how much time the data will be stored in the session

from app.controllers import Default