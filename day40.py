# Request module

import requests as req

#res = req.get("https://www.google.com")
#print(res.text)

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

headers = {
    "Content-type": "application/json; charset=UTF-8"
}


res = req.post(url, headers=headers, json=data)
print(res.text)