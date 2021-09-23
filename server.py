from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def checkerboard1():
    return render_template ( 'index.html', numbers = 8)

if __name__=="__main__":   
    app.run(debug=True)


