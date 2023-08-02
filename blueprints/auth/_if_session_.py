from flask import Flask, Blueprint,redirect, url_for, render_template, session

def if_session():
    if ('loggedin' in session) and (session['role']=='Admin'):
        return 'bp_admin_dashboard.admin_dashboard'
    elif ('loggedin' in session) and (session['role']=='User'):
        return 'bp_user_dashboard.user_dashboard'
    else:
        return None