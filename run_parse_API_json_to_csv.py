import json
import pandas
import os
import glob

if not os.path.exists("parsed_files"):
  os.mkdir("parsed_files")


dataset = pandas.DataFrame()

for json_file_name in glob.glob("json_files/*.json"):
	try:
		f = open(json_file_name, "r")
		json_data = json.load(f)
		f.close()

		# print(json_data)

		gh_id = json_data['login']
		avatar_url = json_data['avatar_url']
		url = json_data['url']
		starred_url = json_data['starred_url']
		name = json_data['name']
		company = json_data['company']
		blog = json_data['blog']
		location = json_data['location']
		email = json_data['email']
		hireable = json_data['hireable']
		bio = json_data['bio']
		public_repos = json_data['public_repos']
		followers = json_data['followers']
		following = json_data['following']
		created_at = json_data['created_at']
		updated_at = json_data['updated_at']


		print(gh_id)
		print(avatar_url)
		print(url)
		print(starred_url)
		print(name)
		print(company)
		print(blog)
		print(location)
		print(email)
		print(hireable)
		print(bio)
		print(public_repos)
		print(followers)
		print(following)
		print(created_at)
		print(updated_at)

		row = pandas.DataFrame.from_records([{
				'gh_id' : gh_id,
				'avatar_url' : avatar_url,
				'url' : url,
				'starred_url' : starred_url,
				'name' : name,
				'company' : company,
				'blog' : blog,
				'location' : location,
				'email' : email,
				'hireable' : hireable,
				'bio' : bio,
				'public_repos' : public_repos,
				'followers' : followers,
				'following' : following,
				'created_at' : created_at,
				'updated_at' : updated_at,
			}])

		print(row)
		dataset = pandas.concat([dataset, row])
	except:
		#exclude invalid IDs: json: {"message": "Not Found", "documentation_url": "https://docs.github.com/rest/users/users#get-a-user"}
		pass



dataset.to_csv("parsed_files/API_dataset.csv", index=False)