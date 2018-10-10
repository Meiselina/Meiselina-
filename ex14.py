from sys import argv

script, user_name = argv
prompt = '> '

print (f"Hi {user_name}, I'm the {user_name} script")
print ("I'd like to ask you a few questions.")
print (f"Do you like me? {user_name}")
likes = input(prompt)

print (f"Where do you live ? {user_name}")
lives = input(prompt)

print ("What kind of computer do you have?")
computer = input(prompt)

print (""")
Alright, so you said Yes about liking me.
You live in Tainan. Not sure where that is.
And you have a Asus computer. Nice.
(""")