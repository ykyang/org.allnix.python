ten_thing = "Apple Orange Crow Telephone Light Sugar"
print("Wait there are not 10 thing in that list.  Let's fix that.")

thing_list = ten_thing.split(' ')
more_thing = ['Day', 'Night', 'Song', 'Frisbee',
              'Corn', 'Banana', 'Girl', 'Boy']

while len(thing_list) < 10:
    next_one = more_thing.pop()
    print(f'Adding: {next_one}')
    thing_list.append(next_one)
    print(f'There are {len(thing_list)} items now')

print(f'There we go: {thing_list}')

print(thing_list[1])
print(thing_list[-1])
print(thing_list.pop())
print(' '.join(thing_list))
print('#'.join(thing_list[3:5]))

