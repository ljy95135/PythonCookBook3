from datetime import datetime

text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')  # parse to datetime
# strftime: from datetime
z = datetime.today()
diff = z - y
print(diff)

# strptime it's slow, can design customized one for easy situation
