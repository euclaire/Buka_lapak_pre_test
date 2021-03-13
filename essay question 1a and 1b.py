import requests

urls = 'https://jsonplaceholder.typicode.com/posts'

response_get = requests.get(urls)
data = response_get.json()
print(data)

inputs = {
	"title": "recommendation",
	"body": "motorcycle",
	"userId": 12
}

response_post = requests.post(url = urls)
print("\n\n\n", response_post)
