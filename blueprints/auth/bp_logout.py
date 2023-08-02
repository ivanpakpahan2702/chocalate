from flask import Flask, Blueprint, redirect, url_for, render_template,request,flash, session
from database.class_connection import db_connection
from blueprints.auth._if_session_ import if_session

bp_logout = Blueprint('bp_logout', __name__)

@bp_logout.route('/logout', methods=['GET','POST'])
def logout():
    if request.method == 'POST':
            session.clear()
            return redirect(url_for('bp_login.login'))
    return redirect(url_for('bp_login.login'))

