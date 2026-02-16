import dataset
import os
from pathlib import Path

# Создаем базу в домашней папке (там всегда есть права)
home = str(Path.home())
db_path = os.path.join(home, 'users.db')

db = dataset.connect(f'sqlite:///{db_path}')
users = db['users']

print(f"✅ База данных: {db_path}")

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