import sys

argv = sys.argv

script, userName = argv
prompt = '> '

print(f"Hi {userName}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {userName}?")

like = input(prompt)

print(f"Where do you live {userName}?")
live = input(prompt)