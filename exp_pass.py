from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3 as lite
import os
import hashlib
import uuid
#создание тестовой базы
exp_pass = Flask(__name__)
#
conn = lite.connect('test.db', check_same_thread=False)
K = conn.cursor()
#создание таблицы юзеров
K.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY,'
            ' login varchar(50), password BLOB, salt BLOB);')
conn.commit()

def hech_create():
    password = input('Vvedite parol>>').encode()
    salt_generation = uuid.uuid4().hex
    hash_passworda = hashlib.pbkdf2_hmac('sha256', password, salt_generation, 100000).hex()
    print(dk)
hech_create()