# -*- coding: utf-8 -*-
import config
import requests
import json
import os
from urllib.parse import urlparse

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}

print('> rate_limit: \n', requests.get('https://api.github.com/rate_limit', headers=headers).content.decode())
print('> start')

owner = config.read('owner')
data_pool = []

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

def req(url):
  print('> get: ', url)
  req = requests.get(url, headers=headers)
  repos = json.loads(req.content.decode())
  return repos

per_page = 100
page = 1

def loop():
  global page
  url = 'https://api.github.com/' + owner + '/repos?per_page=' + str(per_page) + '&page=' + str(page)
  repos = req(url)
  for repo in repos:
    data_pool.append(repo)
  if len(repos) == per_page:
    page = page + 1
    loop()

try:
  loop()
  data_pool.sort(key=get_value, reverse=True)
  for i in config.read('output'):
    # 取出前n条
    save_json('/top'+str(i), data_pool[0:i])
except Exception as e:
  print('> exception: ', e)

print('> rate_limit: \n', requests.get('https://api.github.com/rate_limit', headers=headers).content.decode())
print('> end')
