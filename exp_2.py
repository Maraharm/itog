from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3 as lite
import os
import hashlib
import uuid
def hash_werk():
    password = input('Vvedite parol>>')
    salt_generation = uuid.uuid4().hex
    hash_passworda = generate_password_hash(password+salt_generation)
    #запрос на добавление в базу salt_generation и hash_passworda



hash_werk()
def check_pass():
    #запрос на получение из базы соли и хеша для этого логина
    hash =
    salt_in_base =
    check_password_hash(hash, password+salt_in_base)