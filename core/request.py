import requests

url = 'https://dinq.in/rest/get-category-type/'

r = requests.get(url)
d = r.json().get("category_types")
print(d)

"""

https://dinq.in/rest/input-quiz/

https://dinq.in/rest/get-category-type/


"""