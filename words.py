def num_letters(num_rows, num_columns):
    return 2*(num_rows+num_columns)-4

assert num_letters(3, 4) == 10  #3 is the num_rows and 4 is the num_columns
assert num_letters(13, 4) == 30
assert num_letters(4, 4) == 12
assert num_letters(6, 4) == 16
assert num_letters(6, 7) == 22

print("Checking assertions.")
