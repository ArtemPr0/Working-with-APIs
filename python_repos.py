import requests

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary.
response_dict = r.json()

print(f"Messages: {response_dict['message']}")
print(f"Documentation: {not response_dict['documentation_url']}")

# Explore information about the repositories.
repo_dicts = response_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)

print("\nSelected information about first repository:")
print
