from flask import Flask, Blueprint, redirect, url_for, render_template,request,flash, session
from database.class_connection import db_connection
import hashlib
from blueprints.auth._if_session_ import if_session

bp_register = Blueprint('bp_register', __name__)

@bp_register.route('/register', methods=['GET','POST'])
def register():
    url = if_session()
    if url:
        return redirect(url_for(url))
    else:
        session.clear()
        if request.method == 'POST':
            # Create variables for easy access
            email    = request.form['email']
            username = request.form['username']
            password = request.form['password']
            question = request.form['question']
            answer = request.form['answer']
            md5 = hashlib.md5()
            md5.update(password.encode("ascii"))
            new_password = md5.hexdigest()

            # Check if username account exists using MySQL
            conn = db_connection()
            account = conn.select_data(coloumn_names='*',table_name='tbl_accounts',statement={'Username':username})
            if len(account)>0:
                flash("Username Already Exists", "danger")
                return render_template('auth/register.html',email=email,username=username,password=password,question=question,answer=answer)
            elif len(question)>0 and len(answer)<=0:
                flash("Please Fill The Answer Form", "danger")
                return render_template('auth/register.html',email=email,username=username,password=password,question=question,answer=answer)
            elif len(question)<=0 and len(answer)>0:
                flash("What Is The Question?!", "danger")
                return render_template('auth/register.html',email=email,username=username,password=password,question=question,answer=answer)
            else:
                conn = db_connection()
                res  = conn.add_data(table_name='tbl_accounts',data_field=('Email','Username','Password','Role','question','answer'),data=(email,username,new_password,'User',question,answer))
                if res == 'Successed':
                     flash("Account Successfull Added To Database", "success")
                else:
                     flash("Account Failed Added To Database", "danger")
                     return render_template('auth/register.html',email=email,username=username,password=password,question=question,answer=answer)
        
        return render_template('auth/register.html')