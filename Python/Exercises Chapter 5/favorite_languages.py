favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print(f"\n{name.title()}'s favorite lanaguage is {languages[0].title()}.")
    if len(languages) > 1:    
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"-{language.title()}")
#Create some questions on why this code works:
#1. Why do we use .items() method when looping through the dictionary?
#2. How does the if statement check the length of the list of languages?
#3. What would happen if we used 'if len(languages) == 1' instead of 'if len(languages) < 2'?
#4. How does the nested for loop work to print each language in the list?
#Answers:
#1. The .items() method returns key-value pairs from the dictionary, allowing us to loop through both the keys and values.
#2. The if statement checks the length of the list of languages using the len() function.
#3. If we used 'if len(languages) == 1', it would only match cases where there is exactly one favorite language, and the code block for multiple languages would not execute.
#4. The nested for loop works by iterating over each language in the list of languages for a given person, allowing us to print each language individually.