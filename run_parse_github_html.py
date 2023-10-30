import pandas
import os
import re

import glob

from bs4 import BeautifulSoup

if not os.path.exists("parsed_files"):
  os.mkdir("parsed_files")

dataset = pandas.DataFrame()  


for file_name in glob.glob("github_html_files/*.html"):
  # file_name = "github_html_files/gh_id.html"

  file = open(file_name, "r", encoding="utf-8")
  soup = BeautifulSoup(file.read(), 'html.parser')
  file.close()

  

  gh_id = soup.find("title").string.split(" ")[0]

  # returns number of starred repositories
  try:
    Num_Starred = soup.findAll("span", {"class": "Counter" })[3].string
  except:
    Num_starred = 0

  # returns user's top pinned repository
  try:
    Pinned_Repo = soup.find("span", {"class": "repo" }).string.strip()
  except:
    Pinned_Repo = 'No Pinned Repositories'


  print(gh_id)
  print(Num_Starred)
  print(Pinned_Repo)


  row = pandas.DataFrame.from_records([{
        'gh_id' : gh_id,
        'Num_Starred' : Num_Starred,
        'Pinned_Repo' : Pinned_Repo,
    }])

  print(row)
  dataset = pandas.concat([dataset, row])
    

dataset.to_csv("parsed_files/starred_pinned_repo_dataset.csv", index=False)