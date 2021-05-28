from main import app
from flask import Flask

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)