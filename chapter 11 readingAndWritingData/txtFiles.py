import numpy as np

# create and write to file
# f = open("test.txt", 'w')
# for i in range(5):
#     f.write(f'This is line {i}\n')
# f.close()

# append to existing file
# f = open("test.txt", 'a')
# f.write(f'this in another line\n')
# f.close()

f = open("data/test.txt", 'r')
content = f.read()
f.close()
print(content)

f = open("data/test.txt", 'r')
contents = f.readlines()
f.close()
print(contents)

arr = np.array([1.20, 2.20, 3.00, 4.14, 5.65, 6.12]).reshape((2, 3))
print(arr)
np.savetxt("data/my_arr.txt", arr, fmt='%.2f', header='Col1 Col2 Col3')

my_arr = np.loadtxt('data/my_arr.txt')
print(my_arr)
