# Disclaimer: I got everything to run apart from getting the values to show on the table.
# The cells where the values should be are empty.
# Main issue: getting the inputs.
# ---------------------------------------------------------------------------------------
# First I created a file called a4.py; a folder called templates which has formnjs.html.
# Next I imported the flask module
# Then I added the homepage route when the user first gets the page.
# Once the user enters their values and clicks "Submit," the calculations function gets called.
# Finally after inputs are calculated, they are put into a dictionary and converted to json.
# The function returns the json object to the "/prefcalc" route and returns the full results plus 200 OK.
from flask import *

# Instantiates flask object.
app = Flask(__name__)

# Homepage; invokes index function.
@app.route('/')
def index():
    return render_template('formnjs.html')

# Makes prefix calculations after inputs have been submitted.
def make_prefcalc(b_1, b_2, b_3, b_4, pf_ln):
    # Ask for user inputs; validate them, and save to variables
    ipAddress = b_1 + "." + b_2 + "." + b_3 + "." + b_4
    prefixLen = pf_ln

    # Defining variables
    subnet_add = ""
    first_host = ""  # fist host address
    last_host = ""  # last host address
    broadAddress = ""  # broadcast address
    subnet_mask = ""  # subnet mask

    # Extrapolating inputs
    ip_octets_list = [b_1, b_2, b_3, b_4]  # make list of integers

    # if prefix is in xxx.xxx.xxx.000
    if prefixLen > 24 and prefixLen < 33:
        # Add prefix id
        subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2]) + "."
        first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2]) + "."
        last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2]) + "."
        broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2]) + "."
        subnet_mask = str(255) + "." + str(255) + "." + str(255) + "."

        # add remaining octet
        if prefixLen == 25:
            subnet_add += str(0)
            first_host += str(1)
            last_host += str(126)
            broadAddress += str(127)
            subnet_mask += str(128)
        elif prefixLen == 26:
            subnet_add += str(0)
            first_host += str(1)
            last_host += str(62)
            broadAddress += str(63)
            subnet_mask += str(192)
        elif prefixLen == 27:
            subnet_add += str(32)
            first_host += str(33)
            last_host += str(62)
            broadAddress += str(63)
            subnet_mask += str(224)
        elif prefixLen == 28:
            subnet_add += str(32)
            first_host += str(33)
            last_host += str(46)
            broadAddress += str(47)
            subnet_mask += str(240)
        elif prefixLen == 29:
            subnet_add += str(32)
            first_host += str(33)
            last_host += str(38)
            broadAddress += str(39)
            subnet_mask += str(248)
        elif prefixLen == 30:
            subnet_add += str(32)
            first_host += str(33)
            last_host += str(34)
            broadAddress += str(35)
            subnet_mask += str(252)
        elif prefixLen == 31:
            subnet_add += str(32)
            first_host += str(33)
            last_host += str(32)
            broadAddress += str(33)
            subnet_mask += str(254)
        elif prefixLen == 32:
            subnet_add += str(32)
            first_host += str(33)
            last_host += str(32)
            broadAddress += str(32)
            subnet_mask += str(255)

    # else if prefix is in xxx.xxx.000.000
    elif prefixLen > 16 and prefixLen < 25:

        if prefixLen == 24:
            subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(
                ip_octets_list[2]) + "." + str(0)
            first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(
                ip_octets_list[2]) + "." + str(1)
            last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(
                ip_octets_list[2]) + "." + str(254)
            broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(
                ip_octets_list[2]) + "." + str(255)
            subnet_mask = str(255) + "." + str(255) + "." + str(255) + "." + str(0)
        elif prefixLen == 23:
            subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(0)
            first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(
                ip_octets_list[2] + 1) + "." + str(254)
            broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(
                ip_octets_list[2] + 1) + "." + str(255)
            subnet_mask = str(255) + "." + str(255) + "." + str(254) + "." + str(0)
        elif prefixLen == 22:
            subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(0)
            first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(
                ip_octets_list[2] + 2) + "." + str(254)
            broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + (
                        str(ip_octets_list[2]) + 2) + "." + str(255)
            subnet_mask = str(255) + "." + str(255) + "." + str(252) + "." + str(0)
        elif prefixLen == 21:
            subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(0)
            first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(
                ip_octets_list[2] + 4) + "." + str(254)
            broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(
                ip_octets_list[2] + 4) + "." + str(255)
            subnet_mask = str(255) + "." + str(255) + "." + str(248) + "." + str(0)
        elif prefixLen == 20:
            subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(0)
            first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(
                ip_octets_list[2] + 8) + "." + str(254)
            broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(
                ip_octets_list[2] + 8) + "." + str(255)
            subnet_mask = str(255) + "." + str(255) + "." + str(240) + "." + str(0)
        elif prefixLen == 19:
            subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(0)
            first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(
                ip_octets_list[2] + 16) + "." + str(254)
            broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(
                ip_octets_list[2] + 16) + "." + str(255)
            subnet_mask = str(255) + "." + str(255) + "." + str(224) + "." + str(0)
        elif prefixLen == 18:
            subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(0)
            first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(
                ip_octets_list[2] + 32) + "." + str(254)
            broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(
                ip_octets_list[2] + 32) + "." + str(255)
            subnet_mask = str(255) + "." + str(255) + "." + str(192) + "." + str(0)
        elif prefixLen == 17:
            subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(0)
            first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(
                ip_octets_list[2] + 64) + "." + str(254)
            broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(
                ip_octets_list[2] + 64) + "." + str(255)
            subnet_mask = str(255) + "." + str(255) + "." + str(128) + "." + str(0)

    # else if prefix is in xxx.000.000.000
    elif prefixLen > 8 and prefixLen < 17:

        if prefixLen == 16:
            subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(0)
            first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(255) + "." + str(254)
            broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(255) + "." + str(255)
            subnet_mask = str(255) + "." + str(255) + "." + str(0) + "." + str(0)
        elif prefixLen == 15:
            if ip_octets_list[1] - 1 < 0:
                subnet_add = str(ip_octets_list[0]) + "." + str(0) + "." + str(0) + "." + str(0)
                first_host = str(ip_octets_list[0]) + "." + str(0) + "." + str(0) + "." + str(1)
            else:
                subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] - 1) + "." + str(0) + "." + str(0)
                first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] - 1) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(255) + "." + str(254)
            broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(255) + "." + str(255)
            subnet_mask = str(255) + "." + str(254) + "." + str(0) + "." + str(0)
        elif prefixLen == 14:
            if ip_octets_list[1] - 1 < 0:
                subnet_add = str(ip_octets_list[0]) + "." + str(0) + "." + str(0) + "." + str(0)
                first_host = str(ip_octets_list[0]) + "." + str(0) + "." + str(0) + "." + str(1)
            else:
                subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] - 1) + "." + str(0) + "." + str(0)
                first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] - 1) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] + 2) + "." + str(255) + "." + str(254)
            broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] + 2) + "." + str(255) + "." + str(255)
            subnet_mask = str(255) + "." + str(252) + "." + str(0) + "." + str(0)
        elif prefixLen == 13:
            if ip_octets_list[1] - 1 < 0:
                subnet_add = str(ip_octets_list[0]) + "." + str(0) + "." + str(0) + "." + str(0)
                first_host = str(ip_octets_list[0]) + "." + str(0) + "." + str(0) + "." + str(1)
            else:
                subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] - 1) + "." + str(0) + "." + str(0)
                first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] - 1) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] + 6) + "." + str(255) + "." + str(254)
            broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] + 6) + "." + str(255) + "." + str(255)
            subnet_mask = str(255) + "." + str(248) + "." + str(0) + "." + str(0)
        elif prefixLen == 12:
            if ip_octets_list[1] - 1 < 0:
                subnet_add = str(ip_octets_list[0]) + "." + str(0) + "." + str(0) + "." + str(0)
                first_host = str(ip_octets_list[0]) + "." + str(0) + "." + str(0) + "." + str(1)
            else:
                subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] - 1) + "." + str(0) + "." + str(0)
                first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] - 1) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] + 14) + "." + str(255) + "." + str(254)
            broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] + 14) + "." + str(255) + "." + str(255)
            subnet_mask = str(255) + "." + str(240) + "." + str(0) + "." + str(0)
        elif prefixLen == 11:
            if ip_octets_list[1] - 17 < 0:
                subnet_add = str(ip_octets_list[0]) + "." + str(0) + "." + str(0) + "." + str(0)
                first_host = str(ip_octets_list[0]) + "." + str(0) + "." + str(0) + "." + str(1)
            else:
                subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] - 17) + "." + str(0) + "." + str(0)
                first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] - 17) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] + 14) + "." + str(255) + "." + str(254)
            broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] + 14) + "." + str(255) + "." + str(255)
            subnet_mask = str(255) + "." + str(224) + "." + str(0) + "." + str(0)
        elif prefixLen == 10:
            if ip_octets_list[1] - 49 < 0:
                subnet_add = str(ip_octets_list[0]) + "." + str(0) + "." + str(0) + "." + str(0)
                first_host = str(ip_octets_list[0]) + "." + str(0) + "." + str(0) + "." + str(1)
            else:
                subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] - 49) + "." + str(0) + "." + str(0)
                first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] - 49) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] + 14) + "." + str(255) + "." + str(254)
            broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] + 14) + "." + str(255) + "." + str(255)
            subnet_mask = str(255) + "." + str(192) + "." + str(0) + "." + str(0)
        elif prefixLen == 9:
            if ip_octets_list[1] - 49 < 0:
                subnet_add = str(ip_octets_list[0]) + "." + str(0) + "." + str(0) + "." + str(0)
                first_host = str(ip_octets_list[0]) + "." + str(0) + "." + str(0) + "." + str(1)
            else:
                subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] - 49) + "." + str(0) + "." + str(0)
                first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] - 49) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] + 78) + "." + str(255) + "." + str(254)
            broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1] + 78) + "." + str(255) + "." + str(255)
            subnet_mask = str(255) + "." + str(128) + "." + str(0) + "." + str(0)

    # else prefix is in 000.000.000.000
    elif prefixLen < 9:

        if prefixLen == 8:
            subnet_add = str(ip_octets_list[0]) + "." + str(0) + "." + str(0) + "." + str(0)
            first_host = str(ip_octets_list[0]) + "." + str(0) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0]) + "." + str(255) + "." + str(255) + "." + str(254)
            broadAddress = str(ip_octets_list[0]) + "." + str(255) + "." + str(255) + "." + str(255)
            subnet_mask = str(255) + "." + str(0) + "." + str(0) + "." + str(0)
        elif prefixLen == 7:
            subnet_add = str(ip_octets_list[0]) + "." + str(0) + "." + str(0) + "." + str(0)
            first_host = str(ip_octets_list[0]) + "." + str(0) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0] + 1) + "." + str(255) + "." + str(255) + "." + str(254)
            broadAddress = str(ip_octets_list[0] + 1) + "." + str(255) + "." + str(255) + "." + str(255)
            subnet_mask = str(254) + "." + str(0) + "." + str(0) + "." + str(0)
        elif prefixLen == 6:
            subnet_add = str(ip_octets_list[0]) + "." + str(0) + "." + str(0) + "." + str(0)
            first_host = str(ip_octets_list[0]) + "." + str(0) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0] + 3) + "." + str(255) + "." + str(255) + "." + str(254)
            broadAddress = str(ip_octets_list[0] + 3) + "." + str(255) + "." + str(255) + "." + str(255)
            subnet_mask = str(252) + "." + str(0) + "." + str(0) + "." + str(0)
        elif prefixLen == 5:
            if ip_octets_list[0] - 4 < 1:
                subnet_add = str(1) + "." + str(0) + "." + str(0) + "." + str(0)
                first_host = str(1) + "." + str(0) + "." + str(0) + "." + str(1)
            else:
                subnet_add = str(ip_octets_list[0] - 4) + "." + str(0) + "." + str(0) + "." + str(0)
                first_host = str(ip_octets_list[0] - 4) + "." + str(0) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0] + 3) + "." + str(255) + "." + str(255) + "." + str(254)
            broadAddress = str(ip_octets_list[0] + 3) + "." + str(255) + "." + str(255) + "." + str(255)
            subnet_mask = str(248) + "." + str(0) + "." + str(0) + "." + str(0)
        elif prefixLen == 4:
            if ip_octets_list[0] - 4 < 1:
                subnet_add = str(1) + "." + str(0) + "." + str(0) + "." + str(0)
                first_host = str(1) + "." + str(0) + "." + str(0) + "." + str(1)
            else:
                subnet_add = str(ip_octets_list[0] - 4) + "." + str(0) + "." + str(0) + "." + str(0)
                first_host = str(ip_octets_list[0] - 4) + "." + str(0) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0] + 11) + "." + str(255) + "." + str(255) + "." + str(254)
            broadAddress = str(ip_octets_list[0] + 11) + "." + str(255) + "." + str(255) + "." + str(255)
            subnet_mask = str(240) + "." + str(0) + "." + str(0) + "." + str(0)
        elif prefixLen == 3:
            if ip_octets_list[0] - 4 < 1:
                subnet_add = str(1) + "." + str(0) + "." + str(0) + "." + str(0)
                first_host = str(1) + "." + str(0) + "." + str(0) + "." + str(1)
            else:
                subnet_add = str(ip_octets_list[0] - 4) + "." + str(0) + "." + str(0) + "." + str(0)
                first_host = str(ip_octets_list[0] - 4) + "." + str(0) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0] + 27) + "." + str(255) + "." + str(255) + "." + str(254)
            broadAddress = str(ip_octets_list[0] + 27) + "." + str(255) + "." + str(255) + "." + str(255)
            subnet_mask = str(224) + "." + str(0) + "." + str(0) + "." + str(0)
        elif prefixLen == 2:
            if ip_octets_list[0] - 4 < 1:
                subnet_add = str(1) + "." + str(0) + "." + str(0) + "." + str(0)
                first_host = str(1) + "." + str(0) + "." + str(0) + "." + str(1)
            else:
                subnet_add = str(ip_octets_list[0] - 4) + "." + str(0) + "." + str(0) + "." + str(0)
                first_host = str(ip_octets_list[0] - 4) + "." + str(0) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0] + 59) + "." + str(255) + "." + str(255) + "." + str(254)
            broadAddress = str(ip_octets_list[0] + 59) + "." + str(255) + "." + str(255) + "." + str(255)
            subnet_mask = str(192) + "." + str(0) + "." + str(0) + "." + str(0)
        elif prefixLen == 1:
            if ip_octets_list[0] - 4 < 1:
                subnet_add = str(1) + "." + str(0) + "." + str(0) + "." + str(0)
                first_host = str(1) + "." + str(0) + "." + str(0) + "." + str(1)
            else:
                subnet_add = str(ip_octets_list[0] - 4) + "." + str(0) + "." + str(0) + "." + str(0)
                first_host = str(ip_octets_list[0] - 4) + "." + str(0) + "." + str(0) + "." + str(1)
            last_host = str(ip_octets_list[0] + 123) + "." + str(255) + "." + str(255) + "." + str(254)
            broadAddress = str(ip_octets_list[0] + 123) + "." + str(255) + "." + str(255) + "." + str(255)
            subnet_mask = str(128) + "." + str(0) + "." + str(0) + "." + str(0)

    # creating dictionary with calculated values and inputs
    prefix_json = {}
    prefix_json["subnet"] = subnet_add
    prefix_json["first"] = first_host
    prefix_json["entered"] = ipAddress
    prefix_json["last"] = last_host
    prefix_json["broadcast"] = broadAddress
    prefix_json["netmask"] = subnet_mask
    # prefix_json dictionary to json format
    return prefix_json

# Shows the results of the query after "Submit" has been clicked
@app.route('/prefcalc')
def prefcalc():
    if request.method == "GET":
        return render_template('formnjs.html')
    else:
        b1 = request.form.get('b1')
        b2 = request.form.get('b2')
        b3 = request.form.get('b3')
        b4 = request.form.get('b4')
        pfln = request.form.get('preflen')
        # calls a function that takes in the inputs for calculation
        data = make_prefcalc(b1, b2, b3, b4, pfln) # returns json
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response

# Runs the webpage
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
