from flask import *
# from mart.forms import *
from mart.models import *
from flask_login import login_required, current_user, login_user, logout_user
from mart import *
from sqlalchemy import or_, and_
from mart.apis import *

def flash_message(message, category):
    flash(message, category)

# APP routes
def register_routes(app):

    @app.route('/')
    @app.route('/home')
    def home():
        return render_template('home.html')