#Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
#You will then be given an unknown number of names to query your phone book for. 
#For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; 
#if an entry for name is not found, print Not found instead.

#1 <= n <= 10**5
#1 <= queries <= 10**5

import fileinput

def address_book(items):
  address_book = {}
  threshold = int(items[0])
  for i, item in enumerate(items):
    if i < threshold:
      name, num = item.split(' ')
      address_book[name] = num.strip()
    else:
      name = item.strip()
      num = address_book.get(name, 0)
      print(f"{name}={num}" if num else "Not found")
    

items = fileinput.input()

address_book(items)
