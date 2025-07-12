from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur Render avec Flask !"
#test

if __name__ == '__main__':
    app.run()
