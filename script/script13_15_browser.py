import webbrowser

x = webbrowser.open('http://www.python.org')
print(x)
c = webbrowser.get('firefox')
c.open('http://www.python.org')
c.open_new_tab('http://docs.python.org')
