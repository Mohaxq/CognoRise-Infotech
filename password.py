# Importing the libraries
import random 
import string 
import time 

# Function to generate a random password
all_char = string.ascii_letters + string.digits + string.punctuation

# Ask user for password length
print("Your Generated Password Will Has At Least Half Of It Are Letters")
print("="*50)
pass_length = int(input("Enter The Length Of The Password : "))
print("="*50)

# Generate the password
password = ""

while len(password) < pass_length :
  # Chek if the password Has At Least Half Of It Are Letters
  if len(password) >= (pass_length//2) :
    random_char = random.choice(all_char)
    # Chek if the random char is a letter --> isalpha() 
    if random_char.isalpha() :
      # Add the random char to the password
      password += random_char
    else :
      continue
  else : 
    # Add a The remainder of the password with random digts 
    random_char = random.choice(all_char)
    password += random_char

# Print the password 
print("Generating Strong Password...")
time.sleep(1)
print(f"Your Password Is : {password}")
