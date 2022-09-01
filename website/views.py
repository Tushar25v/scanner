from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Data,User

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    data = Data.query.all()
    return render_template("index.html", user=current_user, data=data)


#FILTERS
@views.route('/filter/bullish', methods=['GET', 'POST'])
@login_required
def bullish():
    open = Data.query.all()
    return render_template("bullish.html", user=current_user, open=open)

@views.route('/filter/bearish', methods=['GET', 'POST'])
@login_required
def bearish():
    open = Data.query.all()
    return render_template("bearish.html", user=current_user, open=open)


@views.route('/filter/strong', methods=['GET', 'POST'])
@login_required
def strong():
    open = Data.query.all()
    return render_template("strong.html", user=current_user, open=open)


@views.route('/filter/weak', methods=['GET', 'POST'])
@login_required
def weak():
    open = Data.query.all()
    return render_template("weak.html", user=current_user, open=open)


@views.route('/filter/unchanged', methods=['GET', 'POST'])
@login_required
def unchanged():
    open = Data.query.all()
    return render_template("unchanged.html", user=current_user, open=open)

# @views.route('/home',methods=['GET','POST'])
# @login_required
# def index():
#     data = Data.query.all()
#     return render_template("home.html",user=current_user,data=data)
