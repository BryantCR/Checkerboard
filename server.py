from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def checkerboard1():
    return render_template ( 'index.html', rwo = 8, column = 8, rowColor = "white", columnColor = "darkolivegreen")

@app.route('/4', methods = ['GET'])
def checkerboard2():
    return render_template ( 'index.html', rwo = 4, column = 8, rowColor = "white", columnColor = "darkolivegreen")

@app.route('/<row>/<column>', methods = ['GET'])
def checkerboard3(row, column):
    rwo = int(row)
    column = int(column)

    return render_template ( 'index.html', rwo = rwo, column = column, rowColor = "white", columnColor = "darkolivegreen")

@app.route('/<row>/<column>/<color1>/<color2>', methods = ['GET'])
def checkerboard4(row, column, color1, color2):
    rwo = int(row)
    column = int(column)
    rowColor = str(color1)
    columnColor = str(color2)

    return render_template ( 'index.html', rwo = rwo, column = column, rowColor = color1, columnColor = color2)


if __name__=="__main__":   
    app.run(debug=True)


