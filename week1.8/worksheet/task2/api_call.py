
import httpx


base_url = "https://dummyjson.com/"

content = "posts/1"

url = base_url + content  # API request

response = httpx.get(url)   # API call

print(response.status_code)   # HTTP response

content = response.json()   # JSON data

print(content)
apple = base_url + "products/search?q=apple"
apples = httpx.get(apple)

print(apples.json()["total"])

likes = base_url + "posts/5"
data = httpx.get(likes)
print(data.json())

meal = base_url + "recipe/meal-type/snack"
val = httpx.get(meal)
print(val.json())