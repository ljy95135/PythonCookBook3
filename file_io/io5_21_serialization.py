# pickle is used for python while json can be used in many situations
import pickle


def pick_file(mydata):
    f = open('somefile', 'wb')
    pickle.dump(mydata, f)
    f.close()
    f = open('somefile', 'rb')
    mydata = pickle.load(f)
    f.close()
    return mydata


data = [1, 2, 3]
# dumps return bytes obj
b = pickle.dumps(data)
print(b)  # b'\x80\x03]q\x00(K\x01K\x02K\x03e.'
data = pickle.loads(b)
print(data)
