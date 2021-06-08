#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']


list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list1.remove('Red')
list1.remove('Pink')
list1.remove('Yellow')

print('Specified List - ',list1)
