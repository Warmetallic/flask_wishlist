from flask import Blueprint, render_template, redirect, url_for, request
from app import db
from app.models import WishlistItem
from app.forms import WishlistForm

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    items = WishlistItem.query.all()
    return render_template("index.html", items=items)


@bp.route("/create", methods=["GET", "POST"])
def create():
    form = WishlistForm()
    if form.validate_on_submit():
        item = WishlistItem(
            name=form.name.data,
            price=form.price.data,
            link=form.link.data,
            note=form.note.data,
        )
        db.session.add(item)
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("create.html", form=form)


@bp.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    item = WishlistItem.query.get_or_404(id)
    form = WishlistForm(obj=item)
    if form.validate_on_submit():
        item.name = form.name.data
        item.price = form.price.data
        item.link = form.link.data
        item.note = form.note.data
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("update.html", form=form, item=item)


@bp.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    item = WishlistItem.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("main.index"))
