#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

import hashlib


m = hashlib.md5(b'password').hexdigest()
p = hashlib.md5(b'password').hexdigest()
b = b'byte'
u = u'unicode'
print(b, u)
print(type(b), type(u))
hoge = isinstance(b, str)
print(hoge)
hoge = isinstance(u, str)
print(hoge)
print(u.encode('utf-8'))

print(m)
print(m)
