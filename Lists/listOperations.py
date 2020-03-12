import os
import sys
mega_list = [2,3,4,5,6]
list1 = ["hi", "1", 1, 3.4, "there", True]
def add_an_item(item):
    print("Adding/appending an item at the end of the list\n")
    list1.append(item)

    print("Item is appended\n")
    print(list1)

def update_to_list_by_index(ind, item):
    print("Pass index and the object.\n. Format insert(index, object)")
    list1.insert(ind, item)
    print(list1)
def remove_item(item):
    print("Removes the item described. Format list.remove(item)")
    mega_list.remove(item)
    print("Item has been removed")
    print(mega_list)

def del_an_item_by_index(ind):
    print("This will take index to delete the object\n")
    print("Our list looks like this before pop", mega_list)
    mega_list.pop(ind)
    print("The element on this index is removed\n")
    print(mega_list)
    print("pop method witout an index removes the last element")
    mega_list.pop()
    print(mega_list)

def extend_list(item):
    print("Make sure that you pass a list for extend\n")
    mega_list.extend(item)
    print("List is extended\n")
    print(mega_list)

def del_list():
    print("List before clearing elements", mega_list)
    mega_list.clear()
    print(mega_list)

def replace_item(ind, item):
    list1[ind] = item
    print("Now list looks like", list1)

if __name__ == "__main__":

    if sys.argv[1] == 'add':
        add_an_item(sys.argv[2])
    elif sys.argv[1] == 'update_index':
        update_to_list_by_index(int(sys.argv[2]), sys.argv[3])
    elif sys.argv[1] == 'remove_item':
        remove_item(int(sys.argv[2]))
    elif sys.argv[1]=='del':
        del_an_item_by_index(int(sys.argv[2]))
    elif sys.argv[1] == 'extend':
        input_str= input("Enter the numbers seperated by space\n")
        user_list = input_str.split()
        print(user_list)
        extend_list(user_list)
    elif sys.argv[1] == 'DEL':
        del_list()
    elif sys.argv[1] == 'replace':
        replace_item(int(sys.argv[2]), sys.argv[3])

    else:
        print("chose an operation to perform")




