import requests
import json

def get_response(url):
    """
    функция для получения ответа сервера на HTTP-запрос
    :param url: адрес сайта
    :return: объект, содержащий ответ сервера на HTTP-запрос
    """
    return requests.get(url)

def create_user_dict(user_info):
    """
    функция преобразовывает json к виду
      {
        "model": "myapp.person",
        "pk": 1,
        "fields": {
          "first_name": "John",
          "last_name": "Lennon"
        }
      }
    :param user_info: словарь, содержащий информацию о пользователе
    :return: преобразованный словарь
    """
    user_dict = {'model': 'blog.User'} # имя модели для загрузки в бд
    user_dict['pk'] = user_info['id'] # id пользователя

    fields = {} # словарь для значений полей модели
    fields['name'] = user_info['name']
    fields['username'] = user_info['username']
    fields['email'] = user_info['email']
    fields['street'] = user_info['address']['street']
    fields['suite'] = user_info['address']['suite']
    fields['city'] = user_info['address']['city']
    fields['zipcode'] = user_info['address']['zipcode']
    fields['lat'] = user_info['address']['geo']['lat']
    fields['lng'] = user_info['address']['geo']['lng']
    fields['phone'] = user_info['phone']
    fields['website'] = user_info['website']
    fields['company_name'] = user_info['company']['name']
    fields['catch_phrase'] = user_info['company']['catchPhrase']
    fields['bs'] = user_info['company']['bs']

    user_dict['fields'] = fields

    return user_dict

def create_post_dict(post_info):
    """
    функция приводит словарь такому же виду, как предыдущая функция
    :param post_info: словарь, содержащий информацию о посте
    :return: преобразованный словарь
    """
    post_dict = {'model': 'blog.Post'}  # имя модели для загрузки в бд
    post_dict['pk'] = post_info['id']  # id поста

    fields = {} # словарь для значений полей модели
    fields['user_id'] = post_info['userId']
    fields['title'] = post_info['title']
    fields['body'] = post_info['body']

    post_dict['fields'] = fields

    return post_dict

def save_json(final_json):
    """
    функция для сохранения json-файла, создает файл с именем db.json
    :param final_json: список из словарей, будущий json-файл
    :return: не возвращает объектов
    """
    with open('db.json', 'w', encoding='utf-8') as file:
        file.write(final_json)

def main():
    # загрузка данных из обоих тестовых файлов
    response_users = json.loads(get_response('http://jsonplaceholder.typicode.com/users').text)
    response_posts = json.loads(get_response('http://jsonplaceholder.typicode.com/posts').text)

    final_json = [] # пустой список, в который будут добавлены словари с данными
                    # о пользователях и постах

    if get_response('http://jsonplaceholder.typicode.com/users').status_code == 200 and\
       get_response('http://jsonplaceholder.typicode.com/posts').status_code == 200:

        for i in response_users:
            final_json.append(create_user_dict(i))

        for j in response_posts:
            final_json.append(create_post_dict(j))
    else:
        print('Ошибка, ответ сервера по первой ссылке - {}, по второй - {} '
              .format(response_users.status_code, response_posts.status_code))

    save_json(json.dumps(final_json))

if __name__ == '__main__':
    main()
