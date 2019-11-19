import views
import contact
import db
import admin
from flask import Flask


def create_app():
    app = Flask(__name__)

    # configurar extensoes
    db.configure(app)

    views.configure(app)

    contact.configure(app)

    admin.configure(app)

    # configurar variaveis
    app.config['SECRET_KEY'] = 'dhuoel3nbjfop9dh@fmsdkfsml1'

    return app
