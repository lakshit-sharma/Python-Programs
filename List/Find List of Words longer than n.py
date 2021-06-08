# Write a Python program to find the list of words that are longer than n from a given list of words.

print("list1=['my', 'name', 'is','john', 'cena', 'i', 'am', 'the', 'number', 'one', 'wrestler', 'in', 'the', 'world']")

list1=['my', 'name', 'is','john', 'cena', 'i', 'am', 'the', 'number', 'one', 'wrestler', 'in', 'the', 'world']

def find(words):
    list2 = []
    n=3
    for word in words:
        if len(word) > n:
            list2.append(word)
    return list2

print('list of words that are longer than n',find(list1))
