# Start1
import random
import string

def get_random_string(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    # print random string
    print(result_str)

# string of length 8
get_random_string(8)
get_random_string(8)

# Ende
# Start2
import random
import string

# get random password pf length 8 with letters, digits, and symbols
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(8))
print("Random password is:", password)
# Ende

#Start3
import random
import string

password = ''.join(random.choice(string.printable) for i in range(8))
print("Random password is:", password)
# Ende

# Start4
import random
import string

def get_random_password():
    random_source = string.ascii_letters + string.digits + string.punctuation
    # select 1 lowercase
    password = random.choice(string.ascii_lowercase)
    # select 1 uppercase
    password += random.choice(string.ascii_uppercase)
    # select 1 digit
    password += random.choice(string.digits)
    # select 1 special symbol
    password += random.choice(string.punctuation)

    # generate other characters
    for i in range(6):
        password += random.choice(random_source)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password

print("First Random Password is ", get_random_password())
# output  qX49}]Ru!(
print("Second Random Password is ", get_random_password())
# Output  3nI0.V#[T
# Ende

# Start5
import secrets
import string

# secure random string
secure_str = ''.join((secrets.choice(string.ascii_letters) for i in range(8)))
print(secure_str)
# Output QQkABLyK

# secure password
password = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(8)))
print(password)
# output 4x]>@;4)
#Ende

# Start6
import random
import string

def get_string(letters_count, digits_count):
    letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    digits = ''.join((random.choice(string.digits) for i in range(digits_count)))

    # Convert resultant string to list and shuffle it to mix letters and digits
    sample_list = list(letters + digits)
    random.shuffle(sample_list)
    # convert list to string
    final_string = ''.join(sample_list)
    print('Random string with', letters_count, 'letters', 'and', digits_count, 'digits', 'is:', final_string)

get_string(5, 3)
# Output get_string(5, 3)

get_string(6, 2)
# Output Random string with 6 letters and 2 digits is: 7DeOCm5t
