words = ['table', 'chair', 'mouse','car','truck','door','floor','window','glass','shades',
'curtains', 'keyboard','tower','laptop','electrical socket','extension cord','hardwood floor',
'light blocking curtains','reclining chair','wired mouse','wireless mouse', 'carpet','soft carpet',
'ceiling fan','electric fan','small portable fan','refrigerator','freezer','refrigerator and freezer combo',
'refrigerator with ice maker', 'wooden table','door with small window at top','durable carpet',
'mouse with programmable buttons - wireless','mouse with programmable buttons - wired','desk - recycled plastics',
'mousepad','floor mat',"plastic floor cover - 5'x5'",'retractable shades - room darkening'
]

#User's search words are put in a list.
search_words = []

#Arbitrary choice of 4 search words.
while len(search_words) < 4:
    user_wants = input("What would you like to search for? ")
    search_words.append(user_wants)

#Words list is searched for the user's seach words. 
#Findings are appended to a list.
found_words = []
for sw in search_words:
    for w in words:
        if sw == w or sw in w:
            found_words.append(w)

#Remove duplicates from list.
for fw in found_words:
    if found_words.count(fw) > 1:
        for i in range(0, found_words.count(fw)-1):
            found_words.remove(fw)

print(found_words)