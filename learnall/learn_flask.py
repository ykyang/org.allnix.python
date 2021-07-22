from flask import Flask
from learnall import app
import learnall.vtkservice

#app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello World!"

print(learnall.vtkservice.hellovtk())

if __name__ == '__main__':
    app.run()
