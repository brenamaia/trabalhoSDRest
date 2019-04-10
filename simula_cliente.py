#!/usr/bin/python

import requests

txt = input('Insira seu texto')

texto = requests.post("http:// 192.168.43.158:5000/%s"%(txt))
print(texto.json())





