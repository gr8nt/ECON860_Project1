# Part 1 / Bonus



# run_requests.py
  Scrapes http://www.charcoalpaper.com/exams/github/user/dataset and saves as file name UTC date/time in html_files directory (creates path if does not exist).
  
  Runs for 24 hours, scraping every 10 minutes, in order to collect bonus user data (run in EC2). If not seeking bonus data, program can be stopped after first instance.

# run_parse.py
  Parses only the first html file in html_files directory, since non-bonus data is static. Login ID, Repo Count, Follower Count, Member Since values for Login ID list are saved in parsed_files/dataset.csv (excludes data for duplicate login IDs).

# run_parse_part1_bonus.py
  Parses html_files directory, records bonus users, if applicable, along with date/time(UTC) of occurence. Results then saved in parsed_files/dataset_bonus.csv (creates path if does not exist). 





# Part 2 / Bonus



# run_requests_API.py
  Scrapes github API for each user ID in parsed_files/dataset.csv. Saves API for each user as json file in json_files directory (creates path if does not exist).

# run_parse_API_json_to_csv.py
  Parses json_files directory, saves select user attributes from github API for list of users into parsed_files/API_dataset.csv

  Skips invalid user IDs (json = {"message": "Not Found", "documentation_url": "https://docs.github.com/rest/users/users#get-a-user"})

# run_requests_github_html.py 
  Scrapes github html for list of valid user IDs in API_dataset.csv. Saves html for each user in github_html_files directory (creates path if does not exist).
  
  The github html must be scraped in addition to the API because the API does not contain data on number of stars, or additional public repo data for the part 2 bonus.

# run_parse_github_html.py
  Parses github_html_files directory, saves number of stars from github html for list of users into parsed_files/starred_pinned_repo_dataset.csv

  Bonus: Also parses for the name of the first pinned repository github displays for each user and saves to the same dataset.

# combine_API_starred_pinned_repo_datasets.py
  Merges API_dataset with starred_pinned_repo_dataset

  This is the final dataset and it is saved as parsed_files/API_dataset_with_starred_pinned_repo.csv





# Part 3


# scatterplot.py
  creates scatterplot using parsed_files/API_dataset.csv..   X = public repos, Y = followers
