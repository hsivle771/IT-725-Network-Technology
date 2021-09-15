# Imports the "requests library"
import requests

# Use the get() function on the requests object to request the conents of the youtube website
r = requests.get("https://youtube.com")
# .text for retrieving the HTML, cast it to as str, split it by line into a list and assign the first line to "response" variable
response = str(r.text).splitlines()[0]
# assign elapsed time (total time of request->response) to "t" variable
t = "Elapsed time: " + str(r.elapsed)

print(f"{response}\n\n{t}")
