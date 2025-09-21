from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is my Python app running on Azure!'

if __name__ == '__main__':
    app.run()