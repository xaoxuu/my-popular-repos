# -*- coding: utf-8 -*-
import config
import requests
import json
import os
from urllib.parse import urlparse

data_pool = []

print('> rate_limit: \n', requests.get('https://api.github.com/rate_limit').content.decode())
print('> start')

def get_value(elem):
  return elem['stargazers_count']

def save_json(path, content):
  root = 'v1'
  dir = root + path + '/'
  file = dir + 'data.json'
  # 创建路径
  isExists = os.path.exists(dir)
  if not isExists:
    os.makedirs(dir)
  # 写入文件
  with open(file, 'w', encoding = 'utf-8') as file_obj:
    json.dump(content, file_obj, ensure_ascii = False, indent = 2)

try:
  print('> links: ', config.read('links'))
  for link in config.read('links'):
    print('> get: ', link)
    url = urlparse(link)
    req = requests.get(link)
    repos = json.loads(req.content.decode())
    for repo in repos:
      data_pool.append(repo)
  data_pool.sort(key=get_value, reverse=True)
  for i in config.read('output'):
    # 取出前n条
    save_json('/top'+str(i), data_pool[0:i])


except Exception as e:
  print('> exception: ', e)

print('\n> rate_limit: \n', requests.get('https://api.github.com/rate_limit').content.decode())
print('> end')
