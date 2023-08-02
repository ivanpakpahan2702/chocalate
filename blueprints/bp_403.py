from flask import Flask, Blueprint, redirect, url_for, render_template,request,flash, session
from database.class_connection import db_connection
import hashlib

bp_403 = Blueprint('bp_403',__name__)

@bp_403.route('/403')
def _403_():
    return render_template('403.html')