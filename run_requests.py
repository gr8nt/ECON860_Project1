import requests
import os

import time
import datetime

import pandas

if not os.path.exists("html_files"):
  os.mkdir("html_files")
  
access_point = "http://www.charcoalpaper.com/exams/github/user/dataset"

headers = {
  'accept': '*/*',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
  'accept-language': 'en-US,en;q=0.9,it;q=0.8,es;q=0.7',
  'referer': 'https://www.google.com/'
}


# for loop below runs code every 10 min, for 24 hours total, to scrape bonus users in AWS EC2
# if not seeking to scrape bonus users, can end program after it runs one instance

for i in range(0, 144):
  current_time = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
  print(current_time)
  f = open("html_files/" + current_time + ".html", "w", encoding="utf-8")

  req = requests.Session()
  response = req.get(access_point, headers = headers)
  html = response.text

  f.write(html)
  f.close()
  
  print("waiting")
  time.sleep(600)
