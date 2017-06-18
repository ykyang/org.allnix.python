def break_words(stuff) -> list:
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def print_first(words: list):
    """Prints the first element after popping it off."""
    word = words.pop(0)
    print(word)


def print_last(words: list):
    """Prints the last """
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence: str) -> list:
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first(words)
    print_last(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first(words)
    print_last(words)

