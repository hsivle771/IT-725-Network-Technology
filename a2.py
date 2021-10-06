# Program which takes IPv4 and prefix length from input and outputs...
# subnet, first & last host addresses, 
# subnet broadcast address, and subnet mask.
# I calculated how much I needed to add and subtract from the octect by...
# using 132.177.1.32 as my default IP, and following the patterns as the prefix decreases.

# Ask for user inputs; validate them, and save to variables
try:
    ipAddress = input("Enter IP address: \n")
except:
    print("""
    \nIP Address Exception:\n Invalid input. Make sure to include only numbers and periods inbetween.\n
    IP address can't be left blank. Periods also must be included between octets.\n
    """)
    
try:
    prefixLen = int(input("Enter prefix length: \n"))
except:
    print("\nPrefix Error:\n Prefix must be an integer. It can't be blank, 0, or greater than 2 digits.\n")

# Defining variables
subnet_add = ""
first_host = "" # fist host address
last_host = "" # last host address
broadAddress = "" # broadcast address
subnet_mask = "" # subnet mask

# Extrapolating inputs
try:
    ip_octets_list = [int(s) for s in ipAddress.split(".")] # make list of integers
except:
    print("Letter Found Error:\n IP Address has one or more letters. Try again and make sure only numbers and periods exist.")

# if prefix is in xxx.xxx.xxx.000
if prefixLen > 24 and prefixLen < 33:
    # Add prefix id
    subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2]) + "."
    first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2]) + "."
    last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2]) + "."
    broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2]) + "."
    subnet_mask = str(255) + "." + str(255) + "." + str(255) + "."
    
    # add remaining octet
    if prefix == 25:
        subnet_add += str(0)
        first_host += str(1)
        last_host += str(126)
        broadAddress += str(127)
        subnet_mask += str(128)
    elif prefix == 26:
        subnet_add += str(0)
        first_host += str(1)
        last_host += str(62)
        broadAddress += str(63)
        subnet_mask += str(192)
    elif prefix == 27:
        subnet_add += str(32)
        first_host += str(33)
        last_host += str(62)
        broadAddress += str(63)
        subnet_mask += str(224)
    elif prefix == 28:
        subnet_add += str(32)
        first_host += str(33)
        last_host += str(46)
        broadAddress += str(47)
        subnet_mask += str(240)
    elif prefix == 29:
        subnet_add += str(32)
        first_host += str(33)
        last_host += str(38)
        broadAddress += str(39)
        subnet_mask += str(248)
    elif prefix == 30:
        subnet_add += str(32)
        first_host += str(33)
        last_host += str(34)
        broadAddress += str(35)
        subnet_mask += str(252)
    elif prefix == 31:
        subnet_add += str(32)
        first_host += str(33)
        last_host += str(32)
        broadAddress += str(33)
        subnet_mask += str(254)
    elif prefix == 32:
        subnet_add += str(32)
        first_host += str(33)
        last_host += str(32)
        broadAddress += str(32)
        subnet_mask += str(255)
        
# else if prefix is in xxx.xxx.000.000
elif prefixLen > 16 and prefixLen < 25:
    
    if prefixLen == 24:
        subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2]) + "." + str(0)
        first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2]) + "." + str(1)
        last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2]) + "." + str(254)
        broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2]) + "." + str(255)
        subnet_mask = str(255) + "." + str(255) + "." + str(255) + "." + str(0)
    elif prefixLen == 23:
        subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(0)
        first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(1)
        last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2] + 1) + "." + str(254)
        broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2] + 1) + "." + str(255)
        subnet_mask = str(255) + "." + str(255) + "." + str(254) + "." + str(0)
    elif prefixLen == 22:
        subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(0)
        first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(1)
        last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2] + 2) + "." + str(254)
        broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + (str(ip_octets_list[2]) + 2) + "." + str(255)
        subnet_mask = str(255) + "." + str(255) + "." + str(252) + "." + str(0)
    elif prefixLen == 21:
        subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(0)
        first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(1)
        last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2] + 4) + "." + str(254)
        broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2] + 4) + "." + str(255)
        subnet_mask = str(255) + "." + str(255) + "." + str(248) + "." + str(0)
    elif prefixLen == 20:
        subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(0)
        first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(1)
        last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2] + 8) + "." + str(254)
        broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2] + 8) + "." + str(255)
        subnet_mask = str(255) + "." + str(255) + "." + str(240) + "." + str(0)
    elif prefixLen == 19:
        subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(0)
        first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(1)
        last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2] + 16) + "." + str(254)
        broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2] + 16) + "." + str(255)
        subnet_mask = str(255) + "." + str(255) + "." + str(224) + "." + str(0)
    elif prefixLen == 18:
        subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(0)
        first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(1)
        last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2] + 32) + "." + str(254)
        broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2] + 32) + "." + str(255)
        subnet_mask = str(255) + "." + str(255) + "." + str(192) + "." + str(0)
    elif prefixLen == 17:
        subnet_add = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(0)
        first_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(0) + "." + str(1)
        last_host = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2] + 64) + "." + str(254)
        broadAddress = str(ip_octets_list[0]) + "." + str(ip_octets_list[1]) + "." + str(ip_octets_list[2] + 64) + "." + str(255)
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



# Output
print(f"""
Subnet address:    {subnet_add}
First host:        {first_host}
Last host:         {last_host}
Broadcast address: {broadAddress}
Subnet mask:       {subnet_mask}
""")
