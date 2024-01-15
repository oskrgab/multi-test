# Original post
def make_engineering(subjects):
  for i in range(len(subjects)):
    print(subjects[i] + ' Eng.')

# List of subjects
my_subjects = [
  'Petroleum',
  'Mechanical',
  'Civil',
  'Electrical'
]

print("Using non-pythonic for loop:")
make_engineering(my_subjects)

# Explanation of other for loops

# 1. Iterate using the "in" keyword
def make_engineering_1(subjects):
  for subject in subjects:
    print(subject + ' Eng.')

print("\nUsing for loop with 'in':")
make_engineering_1(my_subjects)

# 2. Using list comprehensions
def make_engineering_2(subjects):
  return [print(subject + ' Eng.') for subject in subjects]

print("\nUsing list comprehension:")
make_engineering_2(my_subjects)

# 3. Using map
def make_engineering_3(subjects):
  return list(map(lambda x: print(x + ' Eng.'), subjects))

print("\nUsing map:")
make_engineering_3(my_subjects)

# 4. Using enumerate
def make_engineering_4(subjects):
  for i, subject in enumerate(subjects):
    print(f'{i}: {subject} Eng.')

print("\nUsing enumerate:")
make_engineering_4(my_subjects)

