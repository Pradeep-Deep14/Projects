email=input("Enter your email: ").strip()

#.strip() is used to remove white spaces

username=email[:email.index('@')]
#list slicing till @
domain=email[email.index('@')+1:]
#list slicing after @

print(f"Your username is {username} & domain is {domain}")

#format string to Display the output