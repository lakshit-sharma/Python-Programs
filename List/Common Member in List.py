# Write a Python function that takes two lists and returns True if they have at least one common member.

list1,list2 = [34,12,15,17,65,38,90,47],[56,87,92,25,29,43,64,17]

def check(list1,list2):
    result = False
    for x in list1:
        for y in list2:
            x==y
            result = True
            return result

print('Is the Lists have common Member - ',check(list1,list2))
