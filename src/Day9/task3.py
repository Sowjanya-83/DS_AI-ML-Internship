import pandas as pd
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
cleaned_usernames = usernames.str.strip()
cleaned_usernames = cleaned_usernames.str.lower()
contains_a = cleaned_usernames.str.contains('a')
print("Cleaned Usernames:")
print(cleaned_usernames)
print("\nDoes the username contain 'a'?")
print(contains_a)
