from flask import render_template, Blueprint, request
from functions import search_in_json

# создаем блюпринт и привязывем к нему шаблоны
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')  # вывод домашней страница программы
def home_page():
    return render_template('index.html')


@main_blueprint.route('/search/')  # вывод страницы поиска
def search():
    search_post = request.args['s']  # помещаем запрос в переменную
    posts = search_in_json(search_post)  # переменную помещаем в функцию как аргумент
    return render_template('post_list.html', posts=posts, search_post=search_post)
