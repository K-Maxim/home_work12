from flask import Blueprint, render_template, request
from functions import load_json_file, save_json
import logging

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route("/post/", methods=['GET'])
def post_form():
    """
    страница для добавления своего поста
    :return: страницу в браузере
    """
    return render_template('post_form.html')


@loader_blueprint.route('/loaded/', methods=['POST'])  # страница, которая показывает что ты добавил
def post_uploaded():
    text = request.values.get('content')  # помещение текста к посту в переменную
    picture = request.files.get('picture')  # помещение картинки к посту в переменную
    filename = picture.filename  # помещение названия файла в переменную
    all_posts = load_json_file()  # импорт списка всех постов
    picture.save(f"./uploads/images/{filename}")  # сохранение картинки в определенную папку
    if filename.split('.')[-1] not in ['jpg', 'jpeg', 'png']:  # проверка расширения формата картинки
        logging.info('Файл не является изображением')  # выведет в консоли, если файл не картинка
    try:
        all_posts.append({
            'pic': f'/uploads/images/{filename}',
            'content': text
        })
        save_json(all_posts)
        # если добавление прошло успешно
    except FileNotFoundError:
        logging.error('Ошибка при загрузке')
        return f'<h1>Файл не найден</h1>'
        # если файл в который надо добавить не был найден
    else:
        return render_template('post_uploaded.html', text=text, filename=filename)
        # если try будет успешным, то выведет страницу с готовым новым постом
