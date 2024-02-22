from .. import app


@app.route('/') #aplica a função route em cima da função index. 
def index():
    return 'hello world'