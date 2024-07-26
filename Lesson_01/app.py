from flask import Flask
from flask import render_template

app = Flask(__name__)


# Главная страница


@app.route("/")
def home():
    return render_template("base.html")


# Страница категории


@app.route("/category/<category_name>")
def category(category_name):
    subcategories = {"cats": ["Корма для кошек"], "dogs": ["Корма для собак"]}
    return render_template(
        "category.html",
        category_name=category_name.capitalize(),
        subcategories=subcategories[category_name],
    )


# Страница подкатегории


@app.route("/category/<category_name>/<subcategory_name>")
def subcategory(category_name, subcategory_name):
    products = {
        "cats": {
            "Корма для кошек": [
                {
                    "id": 1,
                    "name": "Сухой корм для кошек",
                    "price": 1000,
                    "description": "Качественный сухой корм для кошек.",
                },
                {
                    "id": 2,
                    "name": "Влажный корм для кошек",
                    "price": 1200,
                    "description": "Качественный влажный корм для кошек.",
                },
            ]
        },
        "dogs": {
            "Корма для собак": [
                {
                    "id": 3,
                    "name": "Сухой корм для собак",
                    "price": 1100,
                    "description": "Качественный сухой корм для собак.",
                },
                {
                    "id": 4,
                    "name": "Влажный корм для собак",
                    "price": 1300,
                    "description": "Качественный влажный корм для собак.",
                },
            ]
        },
    }
    return render_template(
        "subcategory.html",
        category_name=category_name.capitalize(),
        subcategory_name=subcategory_name,
        products=products[category_name][subcategory_name],
    )


# Страница товара


@app.route("/product/<int:product_id>")
def product(product_id):
    products = {
        1: {
            "name": "Сухой корм для кошек",
            "price": 1000,
            "description": "Качественный сухой корм для кошек.",
        },
        2: {
            "name": "Влажный корм для кошек",
            "price": 1200,
            "description": "Качественный влажный корм для кошек.",
        },
        3: {
            "name": "Сухой корм для собак",
            "price": 1100,
            "description": "Качественный сухой корм для собак.",
        },
        4: {
            "name": "Влажный корм для собак",
            "price": 1300,
            "description": "Качественный влажный корм для собак.",
        },
    }
    product = products.get(product_id)
    return render_template("product.html", product=product)


if __name__ == "__main__":
    app.run(debug=True)
