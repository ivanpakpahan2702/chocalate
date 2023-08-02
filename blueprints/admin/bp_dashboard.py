from flask import Flask, Blueprint,redirect, url_for, render_template, session
from blueprints.admin._role_required_ import role_required

bp_admin_dashboard = Blueprint('bp_admin_dashboard', __name__)

@bp_admin_dashboard.route('/admin')
def admin_dashboard():
    url = role_required('Admin')
    if url:
        return redirect(url_for(url))
    else:
        return render_template('admin/index.html', title='Dashboard')
    
    