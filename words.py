import numpy as np
data1 = np.loadtxt("loop1.csv", delimiter=",", dtype=str, encoding = 'utf8')
data2 = np.loadtxt("loop2.csv", delimiter=",", dtype=str, encoding = 'utf8')
data3 = np.loadtxt("loop3.csv", delimiter=",", dtype=str, encoding = 'utf8')
data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')

def num_letters(num_rows, num_columns):
    return (2*num_rows)+(2*num_columns)-4

assert num_letters(3, 4) == 10  #3 is the num_rows and 4 is the num_columns
assert num_letters(13, 4) == 30
assert num_letters(4, 4) == 12
assert num_letters(6, 4) == 16
assert num_letters(6, 7) == 22

print("Checking assertions.")

words = [] #this will store the letters we extract from the data file
rows, columns = data.shape  #this gives you the number of rows and number of columns in the data file
#collect all letters - fill in your code here
c = 0
r = 1
while c < columns:
    words.append(str(data[0,c]))
    c = c + 1
print(words)
while r < rows:
    words.append(str(data[r,c-1]))
    r = r + 1
print(words)
c = c - 1
while c > 0:
    words.append(str(data[-1,c-1]))
    c = c - 1
print(words) #check that you collected all the letters in your data file

assert len(words) == num_letters(rows, columns) 

  #this should not throw an error. If it does, most likely your main code is not getting the correct number of letters
