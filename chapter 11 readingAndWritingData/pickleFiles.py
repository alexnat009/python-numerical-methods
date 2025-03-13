import pickle

dict_a = {"A": 0, "B": 1, "C": 2, "D": 3}
pickle.dump(dict_a, open('data/test.pkl', 'wb'))

my_dict = pickle.load(open('data/test.pkl', 'rb'))
print(my_dict)