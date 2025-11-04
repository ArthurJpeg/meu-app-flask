from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>🚀 Minha App Flask na Nuvem!</h1><p>Funcionando perfeitamente!</p>"

@app.route("/sobre")
def sobre():
    return "<h1>Sobre</h1><p>Esta é uma aplicação de exemplo hospedada na nuvem!</p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)