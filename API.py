
import requests
'''response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("Status Code:", response.status_code)
print("Response JSON:", response.json())'''

'''
import requests
data = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print("Status Code:", response.status_code)
print("Response:", response.json())
'''
update_data = {"title": "updated title"}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=update_data)
print("Status Code:", response.status_code)
print("Updated Response:", response.json())