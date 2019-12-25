import re

regex = r".ar"

test_str = "The car parked in the garage."

matches = re.finditer(regex, test_str)
for i in matches:
    print(i)