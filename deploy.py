from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)


@api.route('/language')
class Language(Resource):
    def get(self):
        return {'hey' : 'there'}


@app.route('/home')
def index():
    return "done!"

if __name__ == "__main__":
    app.run()

