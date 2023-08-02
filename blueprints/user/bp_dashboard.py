from flask import Flask, Blueprint,redirect, url_for, render_template, session
from blueprints.user._role_required_ import role_required
bp_user_dashboard = Blueprint('bp_user_dashboard', __name__)

@bp_user_dashboard.route('/')
def user_dashboard():
    url = role_required('User')
    if url:
        return redirect(url_for(url))
    else:
        # Code Here
        return render_template('user/index.html', title='Dashboard')
    