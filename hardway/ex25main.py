import ex25
sentence = 'All good things come to those who wait.'
print(sentence)

words = ex25.break_words(sentence)
#print(f'type(words): {type(words)}')

sorted_words = ex25.sort_words(words)
#print(sorted_words)

ex25.print_first(words)
ex25.print_last(words)

sorted_words = ex25.sort_sentence(sentence)
print(sorted_words)

ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)
