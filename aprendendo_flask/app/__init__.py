from flask import Flask

app = Flask(__name__) #especifica o valor do arquivo na execução, como esse é o arquivo principal, ele recebe o nome de main.

from app.controllers import default