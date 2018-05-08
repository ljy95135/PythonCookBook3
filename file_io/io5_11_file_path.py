import os

# os.path: basename commonpath dirname join
# expand
path = '~/Data/data.csv'
print(os.path.expanduser(path))  # '/Users/beazley/Data/data.csv'
# split file extension
print(os.path.splitext(path))  # ('~/Data/data', '.csv')
