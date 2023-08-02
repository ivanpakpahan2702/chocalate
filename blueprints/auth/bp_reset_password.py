from flask import Flask, Blueprint, redirect, url_for, render_template,request,flash, session
from database.class_connection import db_connection
import hashlib
from blueprints.auth._if_session_ import if_session

bp_reset_password = Blueprint('bp_reset_password', __name__)

@bp_reset_password.route('/forgot-password/reset-password', methods=['GET','POST'])
def reset_password():
    try:
        if session['username']:
            username = session['username']
        else:
            username = ''
        url = if_session()
        if url:
            return redirect(url_for(url))
        else:
            if request.method == 'POST':
                # Create variables for easy access
                password = request.form['password']
                md5 = hashlib.md5()
                md5.update(password.encode("ascii"))
                new_password = md5.hexdigest()
                # Check if username account exists using MySQL
                conn = db_connection()
                res  = conn.update_data(table_name='tbl_accounts',data_field=('Password',),data=(new_password,),statement={"Username":username})
                if res == 'Successed':
                    session['username'] = None
                    flash("Password Successfull Updated To Database", "success")
                    return redirect(url_for('bp_login.login'))
                else:
                    flash("Password Failed Updated To Database", "danger")
                    return redirect(url_for('bp_login.login'))
    except:
        return redirect(url_for('bp_403._403_'))     
           
    return render_template('auth/reset-password.html')