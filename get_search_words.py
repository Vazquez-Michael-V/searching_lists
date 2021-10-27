import json

def get_search_words(search_words):
    """Takes an empty list as an argument."""
#Get search words from the user. Search words are then put in a list.
    #search_words = []
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
    #Remember the user's search words.
            confirmed_search_words = search_words
            filename = 'confirmed_search_words.json'
            with open(filename, 'w') as f:
                json.dump(confirmed_search_words, f)
                break
        else:
            search_words = []
            print(ask_user_for_search_words)
            continue

#search_words = []
#get_search_words(search_words)
#print(search_words)