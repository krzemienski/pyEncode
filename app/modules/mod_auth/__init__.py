import hashlib

from flask.ext.babel import gettext as _
from flask.ext.login import LoginManager

# configure Flask-Login
from app import app, db, on_application_ready
from app.models.user import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "mod_auth.login"
login_manager.login_message = _("You have to log in to access this page!")
login_manager.login_message_category = "warning"
login_manager.localize_callback = _


def create_initial_user():
    # check if there is any user in the db
    if User.query.count() == 0:
        # create a user
        user = User(username="admin", password=hashlib.sha256("admin".encode("utf8")).hexdigest(),
                    email="webmaster@example.org")
        user.is_admin = True
        db.session.add(user)
        db.session.commit()


on_application_ready.append(create_initial_user)
