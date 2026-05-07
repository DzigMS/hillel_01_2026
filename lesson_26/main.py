import re

sting_pattern = r'\+380\d{9}'
pattern = re.compile(r'<.*?>')
phone_number_pattern = re.compile(r'\+380\d{9}')

s1 = """
The other reason the tables are not exhaustive is that 
I wanted them to serve as a quick introduction to regex. 
If you are a complete beginner, you should get a firm +310987654321
grasp of basic regex syntax just by reading the examples in the tables. 
I tried to introduce features in a logical order and to keep out oddities +380123456789
that I've never seen in actual use, such as the 'bell character'. 
With these tables as a jumping board, +380987654321
you will be able to advance to mastery by exploring the other pages on the site.
"""

found = re.findall(phone_number_pattern, s1)

if found:
    print(f'found {found}')

