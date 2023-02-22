from flask import Flask, template_rendered

app = Flask(__name__)

def home():
    return template_rendered("index.html")

if __name__ == "__main__":
    app.run(debug=True)