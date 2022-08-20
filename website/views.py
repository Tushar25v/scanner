from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Data,User

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    data = Data.query.all()
    return render_template("index.html", user=current_user, data=data)


# @views.route('/home',methods=['GET','POST'])
# @login_required
# def index():
#     data = Data.query.all()
#     return render_template("home.html",user=current_user,data=data)
