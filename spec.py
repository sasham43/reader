# coding: utf-8
import re

book_text = open('/Users/sashakramer/Documents/grover.txt').read()
# my_str = "hey th~!ere"
book_text = book_text.replace("“","\"")
book_text = book_text.replace("”","\"")
my_new_string = re.sub('[^a-zA-Z0-9 \n\."]', '', book_text)
print my_new_string
