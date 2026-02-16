import dataset
db = dataset.connect('sqlite:///users.db')
users = db['users']  # таблица для фото (id, name - это url)

def add_user(id, image_url):
    users.insert({'id': id, 'name': image_url})

def get_user(id):
    return users.find_one(id=id)

def get_all_users():
    return list(users.all())

def update_user(id, new_image_url):
    users.update({'id': id, 'name': new_image_url}, ['id'])

def delete_user(id):
    users.delete(id=id)