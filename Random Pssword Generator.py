import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+=:?/"

string = lower_case + upper_case + numbers + symbols
length = 8
password = "".join(random.sample(string, length))

print(password)
