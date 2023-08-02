from flask import Flask, session, request, Blueprint, render_template
from flask_mysqldb import MySQL
from flask_wtf import CSRFProtect
import MySQLdb.cursors
import re
from datetime import timedelta

# Config App
app = Flask('__name__')
app.config['SECRET_KEY'] = '270200Looper002072'
csrf = CSRFProtect(app)

# Initialize Blueprint
# User Side
from blueprints.user.bp_dashboard import bp_user_dashboard
app.register_blueprint(bp_user_dashboard)

# Admin Side
from blueprints.admin.bp_dashboard import bp_admin_dashboard
app.register_blueprint(bp_admin_dashboard)

# Auth
from blueprints.auth.bp_register import bp_register
app.register_blueprint(bp_register)

from blueprints.auth.bp_login import bp_login
app.register_blueprint(bp_login)

from blueprints.auth.bp_forgot_password import bp_forgot_password
app.register_blueprint(bp_forgot_password)

from blueprints.auth.bp_reset_form import bp_reset_form
app.register_blueprint(bp_reset_form)

from blueprints.auth.bp_reset_password import bp_reset_password
app.register_blueprint(bp_reset_password)

from blueprints.auth.bp_logout import bp_logout
app.register_blueprint(bp_logout)

# 403
from blueprints.bp_403 import bp_403
app.register_blueprint(bp_403)


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=120)

app.run(debug=True)