import pandas
import os
import re

import glob

from bs4 import BeautifulSoup

if not os.path.exists("parsed_files"):
  os.mkdir("parsed_files")

dataset = pandas.DataFrame()  


# will parse first html file in "html_files" directory since part 1 charcoal data is static
# would only want to use a for loop to parse each html when parsing for github bonus users
file = open("html_files/" + os.listdir('html_files')[0], "r")
soup = BeautifulSoup(file.read(), 'html.parser')
file.close()

  

Login_ID_prelim = soup.find_all("div", {"class": "userid" })
    
Repo_Count_prelim = soup.find_all("div", {"class": "repocount" })

Follower_Count_prelim = soup.find_all("div", {"class": "followercount" })

Member_Since_prelim = soup.find_all("div", {"class": "membersince" })


  
Login_ID = []
for i in Login_ID_prelim:
  Login_ID.append(i.text.strip())

Repo_Count = []
for i in Repo_Count_prelim:
  Repo_Count.append(i.text.strip())

Follower_Count = []
for i in Follower_Count_prelim:
  Follower_Count.append(i.text.strip())

Member_Since = []
for i in Member_Since_prelim:
  Member_Since.append(i.text.split(" ")[2])

dataset = pandas.DataFrame(
  {'Login_ID': Login_ID,
   'Repo_Count': Repo_Count,
   'Follower_Count': Follower_Count,
   'Member_Since': Member_Since
  })

dataset.drop_duplicates().to_csv("parsed_files/dataset.csv", index=False)
