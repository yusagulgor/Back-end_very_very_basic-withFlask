from flask import Flask
from views import main

app = Flask(__name__, template_folder='templates')

app.register_blueprint(main,url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True,port=5500)

