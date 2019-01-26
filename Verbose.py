import re

re.compile(r'''
(\d\d\d-)|   # area code
(\(\d\d\d) ) # -or- area code with parens and no desh
\d\d\d       # first 3 digits
-            # second desh
\d\d\d\d     # last 4 digits
\sx\d[2,4]   # extension, like x1234''', re.IGNORECASE | re.DOTALL | re.VERBOSE)
