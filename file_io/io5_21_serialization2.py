import pickle


# can also dump func class interface
# assume source is available
# file, network, process etc can't be pickled
def pickle_many():
    # first in first out
    f = open('somedata', 'wb')
    pickle.dump([1, 2, 3, 4], f)
    pickle.dump('hello', f)
    pickle.dump({'Apple', 'Pear', 'Banana'}, f)
    f.close()

    f = open('somedata', 'rb')
    pickle.load(f)  # [1, 2, 3, 4]
    pickle.load(f)  # 'hello'
    pickle.load(f)  # {'Apple', 'Pear', 'Banana'}
