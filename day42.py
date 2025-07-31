# Regular Expressions
# (RegEx)

import re 

pattern = r"[A-Z]+int"

text = ''' Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsam, adipisci quae, eligendi porro illo sint Mint recusandae, voluptatum repellat reiciendis a amet nisi velit. Facere error suscipit, dolor nam quibusdam veniam! '''

# for first occurence

# match = re.search(pattern, text)

# for multiple occurence

matches = re.finditer(pattern, text)

for match in matches:
    print(text[match.span()[0]:match.span()[1]]) 