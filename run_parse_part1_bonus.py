import pandas
import os
import re

import glob

from bs4 import BeautifulSoup

if not os.path.exists("parsed_files"):
  os.mkdir("parsed_files")

dataset = pandas.DataFrame()  


for file_name in glob.glob("html_files/*.html"):

  file = open(file_name, "r")
  soup = BeautifulSoup(file.read(), 'html.parser')
  file.close()

  Login_ID2_prelim = soup.find_all("div", {"class": "userid2" })
    
  Login_ID2 = []
  for i in Login_ID2_prelim:
    Login_ID2.append(i.text.strip())

  print(Login_ID2)
   
  scrape_time = file_name.split('\\')[1].replace(".html", "")
  scrape_time_year = scrape_time[0:4]
  scrape_time_month = scrape_time[4:6]
  scrape_time_day = scrape_time[6:8]
  scrape_time_hour = scrape_time[8:10]
  scrape_time_minute = scrape_time[10:12]
  scrape_time_date = scrape_time_month + "/" + scrape_time_day + "/" + scrape_time_year
  scrape_time_UTC = scrape_time_hour + ":" + scrape_time_minute

  dataset = pandas.concat([dataset,
    pandas.DataFrame.from_records([{
      "scrape_time_date": scrape_time_date,
      "scrape_time_UTC": scrape_time_UTC,
      "Login_ID2": Login_ID2,
      }])
    ])

dataset.to_csv("parsed_files/dataset_bonus.csv", index=False)
