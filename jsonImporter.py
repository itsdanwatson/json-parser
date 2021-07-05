import requests

# Extract JSON data from URL
url = "https://jsonplaceholder.typicode.com/posts"
data = requests.get(url).json()
print("Getting JSON from :", url)


# Sort JSON data Alphabetically by the value "title"
# Create a data function
def return_title_index(item):
    return item['title']


# Sort and Print results
print(sorted(data, key=return_title_index))
