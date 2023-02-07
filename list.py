shopping_list = []
need_items = True

while need_items == True:
     item_to_add = input("What item would you like to add to your list?")
     shopping_list.append(item_to_add)
     print("Your list has the following items in it: ")
     print("-----")
     for item in shopping_list:
          print("- " + item)
     print("---")
     
     answer = input("Would you like to add another item? (y/n) ")
     if answer == "n":
          need_items = False
     
print("Your final list is: ")
print("----")
for item in shopping_list:
     print("- " + item)
print("-----")