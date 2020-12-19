"""
This program is to determine the Xmas movie we will
watch based on xmas_list.txt

"""
# Import and Open file
import random
with open("C:\python\xmas_list.txt", "r") as f:
    lines = f.readlines()
    print(random.choice(lines))