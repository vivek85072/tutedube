'''
from flask import Flask

app = Flask (__name__)

@app.route('/')

def home() :
    
    return 'Hi there'  

if __name__ == '__main__':
    app.run(debug=True)
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    print("Home route accessed")
    return 'Hi there'

if __name__ == '__main__':
    app.run(debug=True)



