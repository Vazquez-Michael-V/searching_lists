import json
import os
import get_search_words


#Get items from a Tab Delimited text file.
#Give the user some instructions.
print("Before beginning, please be sure the text file you wish to search is saved as a Tab Delimited text file.")
print("Example of valid text file name: 'file.txt'")
user_file = input("Enter the name of the Tab Delimited text file you would like to search. Be sure to include the file extension '.txt'\n")

#Check the file name input by the user.
items = []
attempts = 5
while True:
    try:
        with open(user_file, 'r') as file_object:
            pass
    except FileNotFoundError:
        attempts -=1
        if attempts == 0: #Program ends after 5 FileNotFoundError errors.
            print("Please check the directory and obtain a '.txt' file name.")
            quit()
        print(f"Valid file names are of the form 'filename.txt'. Please check directory and enter a vaild file name.\n\tYou have {attempts} attempts remaining.")
        user_file = input("Enter the name of the .txt file you would like to search. Be sure to include the file extension '.txt'\n")       
    else:
        with open(user_file, 'r') as file_object:
            item_text = file_object.readlines()  #Can handle items with spaces, ie 'wireless mouse' and 'office chair'
            items = [i.rstrip() for i in item_text]                
            break
    
count_items = len(items)
print(f"\nYour list contains {count_items} items.")
print(items)

#Need to address case sensitivity of user input.
#Check if user already has a list of search words.
search_words = []
filename = 'confirmed_search_words.json'
try:
    with open(filename) as f:
        confirmed_search_words = json.load(f)
except FileNotFoundError:
   get_search_words.get_search_words(search_words)
else:    
    print("\nYou have a previously saved list of search words.")
    print(confirmed_search_words)
    use_again = input("Would you like to use search for these words again? ")
    if use_again.lower() == 'yes':
        search_words = confirmed_search_words
    else: #Give the user the option to type in search words or pass a text file of search words.
        #Ask user, "File or individually enter the words?"
        search_type = input("Do you have a TabDelimited text file of search words? ")
        if search_type.lower() == 'yes':
            search_words = get_search_words.get_search_file()
        else:
            get_search_words.get_search_words(search_words)

#Items list is searched for the user's seach words. 
#Findings are appended to a list.
found_items = []

for sw in search_words:
    for w in items:
        if sw == w or sw in w:
            found_items.append(w)

#Remove duplicates from list.
for fw in found_items:
    if found_items.count(fw) > 1:
        for i in range(0, found_items.count(fw)-1):
            found_items.remove(fw)

print(f"\nYour search returned {len(found_items)} item(s).")
print(found_items)

#Save the found items to a text file.
with open('found_items_file.txt', 'w') as fif:
    for i in found_items: 
        fif.write(f"{i}\n")

#Automatically opens the found items text file.
os.startfile('found_items_file.txt')