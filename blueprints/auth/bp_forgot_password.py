from flask import Flask, Blueprint, redirect, url_for, render_template,request,flash, session
from database.class_connection import db_connection
import hashlib
from blueprints.auth._if_session_ import if_session

bp_forgot_password = Blueprint('bp_forgot_password', __name__)

@bp_forgot_password.route('/forgot-password', methods=['GET','POST'])
def forgot_password():
    url = if_session()
    if url:
        return redirect(url_for(url))
    else:
        if request.method == 'POST':
            # Create variables for easy access
            username = request.form['username']
            # Check if username account exists using MySQL
            conn = db_connection()
            account = conn.select_data(coloumn_names='*',table_name='tbl_accounts',statement={'Username':username})
            if len(account)<=0:
                flash("Username Not Found!", "danger")
                return render_template('auth/forgot-password.html',username=username)
            else:
                conn = db_connection()
                account = conn.select_data(coloumn_names='*',table_name='tbl_accounts',statement={'Username':username})
                question = account[0][6]
                if len(question)<=0:
                    flash("Sorry You Don't Have Any Validate Question", "warning")
                    return render_template('auth/forgot-password.html',username=username)
                else:
                    flash("Answer The Question", "danger")
                    return render_template('auth/forgot-password.html',username=username,question=question)
        
        return render_template('auth/forgot-password.html')