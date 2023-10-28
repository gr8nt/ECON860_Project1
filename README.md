# Part 1



# run_requests.py
  Scrapes http://www.charcoalpaper.com/exams/github/user/dataset and saves in html_files directory (creates path if does not exist).
  
  Runs for 24 hours, scraping every 10 minutes, in order to collect bonus user data (run in EC2). If not seeking bonus data, program can be stopped after first instance.

# run_parse.py
  Parses only the first html file in html_files directory, since non-bonus data is static. Login ID, Repo Count, Follower Count, Member Since values are saved in parsed_files/dataset.csv (excludes data for duplicate login IDs).

# run_parse_part1_bonus.py
  Parses html_files directory, records bonus users, if applicable, along with date/time(UTC) of occurence. Results then saved in parsed_files/dataset_bonus.csv (creates path if does not exist). 





# Part 2



# run_requests_API.py
  Scrapes github API for each user ID in parsed_files/dataset.csv. Saves API for each user as json file in json_files directory (creates path if does not exist).

# run_parse_API_json_to_csv.py
  Parses json_files directory, saves select user attributes from github API for list of users into parsed_files/API_dataset.csv

  Skips invalid user IDs (json = {"message": "Not Found", "documentation_url": "https://docs.github.com/rest/users/users#get-a-user"})





# Part 3


# scatterplot.py
  creates scatterplot using parsed_files/API_dataset.csv..   X = public repos, Y = followers
