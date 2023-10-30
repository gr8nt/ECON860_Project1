import pandas

data1 = pandas.read_csv('parsed_files/API_dataset.csv')
data2 = pandas.read_csv('parsed_files/starred_pinned_repo_dataset.csv') 
  
dataset = pandas.merge(data1, data2,  
                   on='gh_id',  
                   how='left') 
  
  
print(dataset)

dataset.to_csv("parsed_files/API_dataset_with_starred_pinned_repo.csv", index=False)