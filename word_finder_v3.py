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
        if attempts == 0:
            print("Please check the directory and obtain a '.txt' file name.")
            quit()
        print(f"Valid file names are of the form 'filename.txt'. Please check directory and enter a vaild file name.\n\tYou have {attempts} attempts remaining.")
        user_file = input("Enter the name of the .txt file you would like to search. Be sure to include the file extension '.txt'\n")       
    else:
        with open(user_file, 'r') as file_object:
            words = file_object.read()
            for w in words.split():
                items.append(w)
            break
    
count_items = len(items)
print(f"Your list contains {count_items} items.")
print(items)

#Get search words from the user. Search words are then put in a list.
search_words = []
ask_user_for_search_words = "What would you like to search for? Type 'Search Now' once all search items have been entered."
print(ask_user_for_search_words)
while True:
    while True:
        user_wants = input()
        user_wants = user_wants.strip() #In case user types trailing spaces.
        if user_wants.lower() == 'search now':
            break
        else:
            search_words.append(user_wants)
    #Remove searches that are all spaces, ie "     "
    for sw in search_words:
        if sw =='':
            search_words.remove(sw) 
#Summarize to user what they will be searching for.
#Gives user opportunity to double check search words, check spelling, etc.
    print(f"\nYou will be searching for {len(search_words)} item(s):")
    print(search_words)
    confirm = input("Is this correct? Enter 'yes' to begin search, or 'no' to edit your search words.\n")
    confirm = confirm.lower()
    if confirm == 'yes':
        break
    else:
        search_words = []
        print(ask_user_for_search_words)
        continue
        

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