from flask import Flask
from flask_restful import Api
from urls.email_urls import api_blueprint
from common.utils.common_error_handler import common_error_handler

app = Flask(__name__)


api = Api(app)
app.register_blueprint(api_blueprint)


@app.errorhandler(Exception)
def handle_error(error):
    return common_error_handler(error)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
