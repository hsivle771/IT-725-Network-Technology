### CS 725/825 Computer Networks, IT 725 Network Technology  (Fall 2021) ###

# Assignment 3 #

*Name:* Elvis Hidalgo  
*Email:* `eh1154@wildcats.unh.edu`

*Assignment description:* [https://www.cs.unh.edu/~cs725/assignments/a3.html](https://www.cs.unh.edu/~cs725/assignments/a3.html)  
*Due:* Wednesday, October 27, 2021, 2:10 pm (start of the class)

This directory must remain private at all times, accessible only to the student, the course instructor and the TA. 

### Program description ###
I used python version 3.
1. First you import the pexpect python library.
2. Ask user for To/From emails by taking user input and assigning it to independent variables.
3. Run the spawn command to tie the nc command to your script and assign it to a variable for later use.
4. Now when you use the expect method of that variable,
insert a list of possible responses from the mail server and create if/elif/else conditional branches to...
evaluate the responses (responses are on the list at a numbered index; range from: 0...list length - 1).

General Things to consider with conditionals:
The numbers followed by question marks are status codes with "?" as a regular expression inplace of any character.
"*" - is any string of characters which is the message that follows the status code if there is one.
5. Status codes of 200 is Ok; 300s is for redirects; 400s is client-side errors; 500s is server-side errors.
6. The sendline methods are used to output messages or other forms of data from you (the client).
7. Lastly, the "exit()" functions are just to end the currently running process (netcat).
