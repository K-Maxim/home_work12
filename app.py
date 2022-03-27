# импорт библотеки фласк
from flask import Flask, send_from_directory

# импорт блюпринтов
from main.views import main_blueprint
from lesson12_project_source_v3.loader.views import loader_blueprint

# создаем объект класса
app = Flask(__name__)

# присваиваем этому объекту блюпринты
app.register_blueprint(main_blueprint, url_prefix='/')
app.register_blueprint(loader_blueprint, url_prefix='/')


@app.route("/uploads/images/<path:path>") # разрешаем доступ к папке с картинками
def static_dir(path):
    return send_from_directory("uploads/images", path)


if __name__ == '__main__':
    app.run()

