import requests
import os

import time
import datetime

import pandas

if not os.path.exists("github_html_files"):
  os.mkdir("github_html_files")

access_point = "https://github.com"

headers = {
  'accept': '*/*',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
  'accept-language': 'en-US,en;q=0.9,it;q=0.8,es;q=0.7',
  'referer': 'https://www.google.com/'
}

f = open("token", "r")
token = f.read()
f.close

id_list = pandas.read_csv("parsed_files/API_dataset.csv")
id_list = id_list['gh_id']

#reference git token ID in .gitignore text document stored in directory
github_session = requests.Session()
github_session.auth = ("gr8nt", token)


for gh_id in id_list:
  print(gh_id)
  f = open("github_html_files/" + gh_id + ".html", "w", encoding="utf-8")

  req = requests.Session()
  response = req.get(access_point + "/" + gh_id, headers = headers)
  html = response.text

  f.write(html)
  f.close()
  
  print("waiting")
  time.sleep(8)
