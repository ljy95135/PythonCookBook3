import re

text1 = '/* this is a comment */'
text2 = '''/* this is a
multiline comment */'''
comment = re.compile(r'/\*(.*?)\*/')

# [' this is a comment ']
print(comment.findall(text1))
# []
print(comment.findall(text2))

# use re.DOTALL flag
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
# [' this is a\nmultiline comment ']
print(comment.findall(text2))

# better to customized one
# (:?.|\n)* all characters
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))