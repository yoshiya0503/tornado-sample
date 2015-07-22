#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"password")
print(token)
f.decrypt(token)
