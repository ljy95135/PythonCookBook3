# use x instead of w: exclusive
import os


def safe_write():
    with open('somefile', 'xt') as f:
        f.write('Hello\n')


# shorter than test myself
def safe_write2():
    if not os.path.exists('somefile'):
        with open('somefile', 'wt') as f:
            f.write('Hello\n')
    else:
        print('File already exists!')
