import requests

url = 'https://dinq.in/rest/get-category-type/'

r = requests.get(url)
print(r)
print(r.json())

d = r.json().get("category_types")

print(d[0])

"""

https://dinq.in/rest/input-quiz/

https://dinq.in/rest/get-category-type/


"""