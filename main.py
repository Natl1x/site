from flask import Flask, render_template, request, flash, redirect, url_for
from settings import *
from sql_queries import DataBase

#=============================================

app = Flask(__name__)
db = DataBase()
app.config['SECRET_KEY'] = SECRET_KEY

#=============================================

@app.route("/")
def index():
    items = db.get_all_items()
    categories = db.get_categories()
    return render_template("index.html", items=items, categories = categories)

@app.route("/item/<item_id>")
def item(item_id):
    item = db.get_item(item_id)
    categories = db.get_categories()
    items = db.get_category_items(item[3])
    return render_template("item.html", item=item, categories = categories, items=items[:4])

@app.route("/category/<id>")
def category(id):
    categories = db.get_categories()
    items = db.get_category_items(id)
    return render_template("category.html", items=items, categories = categories)

@app.route("/order/<item_id>", methods = ["GET", "POST"])
def order(item_id):
    categories = db.get_categories()
    item = db.get_item(item_id)
    if request.method == 'POST':
        try:
            db.add_order(item[0], 
                        request.form["name"],
                        request.form["phone"],
                        request.form["city"],
                        request.form["address"], 
                        request.form["amount"],
                        item[4])
            flash("Додано замовлення!", "alert-light") #надсилаємо швидкі сповіщення у браузер
            return redirect(url_for('index')) #перенаправляємо на головну сторінку
        except:
            flash("Помилка оформлення замовлення!", "alert-danger") #надсилаємо швидкі сповіщення у браузер

    return render_template("order.html", item=item, categories = categories)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
    