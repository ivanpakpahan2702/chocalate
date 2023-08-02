from flask import Flask, Blueprint,redirect, url_for, render_template, session

def role_required(Role):
    if ('loggedin' not in session):
        return 'bp_login.login'
    elif ('loggedin' in session) and (session['role']!=Role):
        return 'bp_403._403_'
    else:
        return None
    