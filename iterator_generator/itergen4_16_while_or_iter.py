# while version
CHUNKSIZE = 8192


def process_data(data):
    pass


def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)


# iter version
def reader2(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        process_data(chunk)
