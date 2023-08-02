from flask import Flask, Blueprint, redirect, url_for, render_template,request,flash, session
from database.class_connection import db_connection
import hashlib
from blueprints.auth._if_session_ import if_session

bp_reset_form = Blueprint('bp_reset_form', __name__)

@bp_reset_form.route('/forgot-password/reset-form', methods=['GET','POST'])
def reset_form():
    url = if_session()
    if url:
        return redirect(url_for(url))
    else:
        session.clear()
        if request.method == 'POST':
            # Create variables for easy access
            username = request.form['username']
            answer = request.form['answer']
            # Check if username account exists using MySQL
            conn = db_connection()
            account = conn.select_data(coloumn_names='*',table_name='tbl_accounts',statement={'Username':username})
            if account[0][7] == answer:
                flash("Please Fill The New Password","success")
                session['username']=username
                return redirect(url_for('bp_reset_password.reset_password'))
            else:
                flash("Sorry, Wrong Answer.","danger")
    return redirect(url_for('bp_forgot_password.forgot_password'))