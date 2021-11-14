import random
import array

# Maximum length of Password is needed
# We take here Password length is 12

max_len = 12

# Now we declare arrays of the character that we need in out password
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]
locase_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upercase_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['@', "#", '$', '%', '^', '&', '*', '(', ')', '~', '+', '<', '>', '?', '/', '!']

# combine all the character arrays and symbols in one array

combined_list = digits + locase_char + upercase_char + symbols

# randomly select at least one character from each character above set
rand_digit =  random.choice(digits)
rand_upper =  random.choice(upercase_char)
rand_lower =  random.choice(locase_char)
rand_symbol = random.choice(symbols)

# combine the character randomly and selected from above
# at this stage, the password contains only 4 characters but we want 12 characters password
# so
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

# now
for x in range(max_len - 4):
    temp_pass = temp_pass + random.choice(combined_list)

    temp_pass_list = array.array('u',temp_pass)
    random.shuffle(temp_pass_list)
password = " "
for x in temp_pass_list:
    password = password + x

print(password)

