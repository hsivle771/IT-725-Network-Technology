### CS 725/825 Computer Networks, IT 725 Network Technology  (Fall 2021) ###

# Assignment 4 #

*Name:* Elvis Hidalgo  
*Email:* `eh1154@wildcats.unh.edu`

*Assignment description:* [https://www.cs.unh.edu/~cs725/assignments/a4.html](https://www.cs.unh.edu/~cs725/assignments/a4.html)  
*Due:* Wednesday, November 17, 2021, 2:10 pm (start of the class)

This directory must remain private at all times, accessible only to the student, the course instructor and the TA. 

### Program description ###

Disclaimer: I got everything to run apart from getting the values to show on the table.
The cells where the values should be are empty.
Main issue: getting the inputs.

Brief description:
First I created a file called a4.py; a folder called templates which has formnjs.html.
Next I imported the flask module
Then I added the homepage route when the user first gets the page.
Once the user enters their values and clicks "Submit," the calculations function gets called.
Finally after inputs are calculated, they are put into a dictionary and converted to json.
The function returns the json object to the "/prefcalc" route and returns the full results plus 200 OK.

