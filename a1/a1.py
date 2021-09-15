import requests

r = requests.get("https://youtube.com")
response = str(r.text).splitlines()[0]
t = "Elapsed time: " + str(r.elapsed)

print(f"{response}\n\n{t}")
