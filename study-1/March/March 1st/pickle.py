import pickle
f = open('text.txt', 'wb') # wb == write binary
data = {1:'python', 2:'you need'}
pickle.dump(data, f)