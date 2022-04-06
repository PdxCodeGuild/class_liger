import re

phone_1 = '555.555.5555'
phone_2 = '1234567890'

# result = re.match('\d{3}[-.]\d{3}[-.]\d{4}', phone_1)

# if result:
    # print(result.group())
# else:
    # print('No matches!')

phone_1 = 'ABCDEFG555.555.5555ABCDEFG'
result = re.search('\d{3}[-.]\d{3}[-.]\d{4}', phone_1)
# print(result.group())


zen_of_python = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

# replace all non-word characters that aren't spaces with single spaces
zen_of_python = re.sub('[^ \w]', ' ', zen_of_python)

# replace groups of 1 or more single spaces with a single space
zen_of_python = re.sub('\s+', ' ', zen_of_python)

# print(zen_of_python)


'''
// Examples from Regex101.com
// Copy/paste to see what they match

// hijkl
// [a-z]
// [A-Z]
// [A-z]
// [G-R]
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

// A{3} find three or more As
AAA

// \d to find digits
0123456789

// \W to find non-word characters
!@#$%^&*()_

00000000ABC
ABC000000000000ABC000

// \d\d\d\.\d\d\d\.\d\d\d\d
// \d\d\d[-.]\d\d\d[-.]\d\d\d\d
// \d{3}[-.]\d{3}[-.]\d{4}
555-555-5555
503.123.4567
123*333*1234

// \w+.com (match anything.com)
// [A-z]+.[A-z]{3}
// (http:\/\/)?(www.)?[A-z]+.(org|com|dev)
pdxcodeguild.com
keegangood.dev
pypi.org 

http://www.pypi.org
www.pdxcodeguild.com
http://keegangood.dev

// Sr\.?\s[A-Z]\w*
Sr. Hernandez
Sra. Bautista
Sr Esparza

'''