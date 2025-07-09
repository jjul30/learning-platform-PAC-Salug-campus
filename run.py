from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "PAC Salug Campus Learning Platform is live!"

if __name__ == "__main__":
    app.run()
