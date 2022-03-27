from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from forms.mensajecrear import OrderCreateForm
from utils.db import db
from models.order import Order
from models.orderdetail import OrderDetail

orders = Blueprint("orders", __name__, url_prefix="/orders")


@orders.route("/")
@login_required
def ordersMain():
    return render_template("orders/main.html")


@orders.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = OrderCreateForm()
    return render_template("orders/create.html", form=form)
