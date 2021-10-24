#Get items from a Tab Delimited text file.
items = []
with open('items_excel_TabDelimited.txt', 'r') as file_object:
    words = file_object.read()
    for w in words.split():
        items.append(w)

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
    confirm = input("Is this correct?\n")
    confirm = confirm.lower()
    if confirm == 'yes':
        break
    else:
        search_words = []
        print(ask_user_for_search_words)
        continue
        

#Words list is searched for the user's seach words. 
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