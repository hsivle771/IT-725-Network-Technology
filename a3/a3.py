import pexpect
 
# Ask user for To/From emails
f_email = input("Enter your email address: ")
t_email = input("Enter the email of who to send the message to: ")
 
# Run the date command using spawn
child = pexpect.spawn("chmod /usr/bin/ nc berlioz.cs.unh.edu 2222")
 
i = child.expect(["failed", "2?? *", "4?? *", "refused", "closed", "timeout"])
 
if i == 0:
  child.sendline("berlioz.cs.unh.edu: connect failed\n")
  exit()
elif i == 1:
  # Status code is in the 200s, so do nothing.
elif i == 2:
  exit()
elif i == 3:
  child.sendline("berlioz.cs.unh.edu: connection refused\n")
  exit()
elif i == 4:
  child.sendline("berlioz.cs.unh.edu: connection closed\n")
  exit()
elif i == 5:
  child.sendline("berlioz.cs.unh.edu: connection timeout\n")
  exit()
else:
  child.sendline("HELO berlioz.cs.unh.edu\r")
  child.expect(["2?? *", "5?? *", "4?? *"])
  
  if i == 0:
    # Status code is in the 200s, so do nothing.
  elif i == 1 || i == 2:
    exit()
  else:
    child.sendline(f"MAIL FROM:<{f_email}>\r")
    child.expect(["2?? *", "5?? *", "4?? *"])
  
    if i == 0:
      # Status code is in the 200s, so do nothing.
    elif i == 1 || i == 2:
      exit()
    else:
      child.sendline(f"RCPT TO:{t_email}>\r")
      child.expect(["2?? *", "5?? *", "4?? *"])
  
      if i == 0:
        # Status code is in the 200s, so do nothing.
      elif i == 1 || i == 2:
        exit()
      else:
        child.sendline("DATA\r")
        child.expect(["3?? *", "5?? *", "4?? *"])
  
        if i == 0:
          # Status code is in the 300s, so do nothing.
        elif i == 1 || i == 2:
          exit()
        else:
          # Body of message
          child.sendline(f"From: {f_email}\r")
          child.sendline(f"To: {t_email}\r")
          child.sendline("Subject: " + input() + "\n")
          child.sendline(input())
          child.sendline(".\r") # end of message
          child.expect(["2?? *", "5?? *", "4?? *"])
  
          if i == 0:
            # Status code is in the 200s, so do nothing.
          elif i == 1 || i == 2:
            exit()
          else:
            child.sendline("QUIT\r")
            exit()