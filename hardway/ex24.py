print("Let's practice everything.")
print('You\'d need to know \'bout escape with \\ that do:')
print('\n newlines and \t tabs.')

poem ='''
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
'''

print('----------')
print(poem)
print('----------')


five = 10 - 2 + 3 - 6
print(f'This should be 5: {five}')


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 # 1000 beans per jar
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10_000
beans, jars, crates = secret_formula(start_point)

print('With a starting point of: {}'.format(start_point))
print(f'We would have {beans} beans, {jars} jars, and {crates} crates.')

start_point /= 10
print('We can also do that this way:')
formula = secret_formula(start_point)
# The single star * unpacks the sequence/collection into positional arguments
print('We would have {} beans, {} jars, and {} crates.'.format(*formula))
