from flask import Flask, Blueprint, redirect, url_for, render_template,request,flash, session
from database.class_connection import db_connection
import hashlib
from blueprints.auth._if_session_ import if_session

bp_login = Blueprint('bp_login', __name__)

@bp_login.route('/login', methods=['GET','POST'])
def login():
    url = if_session()
    if url:
        return redirect(url_for(url))
    else:
        session['username'] = None
        # Check if "username" and "password" POST requests exist (user submitted form)
        if request.method == 'POST':
            # Create variables for easy access
            username = request.form['username']
            password = request.form['password']
            md5 = hashlib.md5()
            md5.update(password.encode("ascii"))
            new_password = md5.hexdigest()
            # Check if account exists using MySQL
            conn = db_connection()
            account = conn.select_data(coloumn_names='*',table_name='tbl_accounts',statement={'Username':username,'Password':new_password}) 
            # If account exists in accounts table in out database
            if len(account)>0:
                account = account[0]
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = account[0]
                session['username'] = account[3]
                session['role'] = account[5]
                # Redirect to home page
                if account[5] == 'Admin':
                    return redirect(url_for('bp_admin_dashboard.admin_dashboard'))
                elif account[5] == 'User':
                    return redirect(url_for('bp_user_dashboard.user_dashboard'))
            else:
                # Account doesnt exist or username/password incorrect
                flash("Incorrect username/password!", "danger")
                return render_template('auth/login.html',username = username, password=password)
    return render_template('auth/login.html')
