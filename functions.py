import json


def load_json_file():
    """
    записывает данные из JSON-файоа в переменную
    :return: список с вложенными словарями
    """
    with open('posts.json', 'r', encoding='UTF-8') as file:
        all_posts = json.load(file)
        return all_posts


def search_in_json(search_post):
    """
    Поиск постов по запросу пользователя
    :param search_post: запрос пользователя
    :return: список с найденными постами
    """
    post_list = []
    all_post = load_json_file()
    for post in all_post:
        if search_post.lower() in post['content'].lower():
            post_list.append(post)

    return post_list


def save_json(all_post):
    """
    запись новых данных в JSON-файл
    :param all_post: список всех постов
    """
    with open('posts.json', 'w', encoding='UTF-8') as file:
        json.dump(all_post, file, ensure_ascii=False)


