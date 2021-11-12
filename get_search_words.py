import json

def get_search_words(search_words):
    """Takes an empty list as an argument and asks to enter search words."""
#Get search words from the user. Search words are then put in a list.    
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

def get_search_file():
    """Takes a text file and stores it as the user's list of search words."""
    user_search_file = input("Please enter the text file name containing your list of search words. Please remember the extension '.txt' when entering file name.\n")
    #Try to open the user's file a maximum of 5 times.
    attempts = 5
    while attempts !=0 or file_found == False:
        try:
            with open(user_search_file, 'r') as usf:
                pass
        except FileNotFoundError:
            attempts -=1
            file_found = False
            if attempts == 0: #Program ends after 5 FileNotFoundError errors.
                print("Please check the directory and obtain a '.txt' file name.")
                quit()
            print(f"Valid file names are of the form 'filename.txt'. Please check directory and enter a vaild file name.\n\tYou have {attempts} attempts remaining.")
            user_search_file = input("Enter the name of the .txt file you would like to search. Be sure to include the file extension '.txt'\n")       
        else:
            with open(user_search_file, 'r') as usf:
                search_words = usf.readlines()
                search_words = [s.rstrip() for s in search_words]      
            file_found = True
            return search_words