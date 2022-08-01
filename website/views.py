from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("Table.htm", user=current_user)

@views.route('/index',methods=['GET','POST'])
@login_required
def index():
    return render_template("index.html",user=current_user)
