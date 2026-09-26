#!/bin/python3

from collections import deque

with open('words5.dict', 'r') as f:
    dictionary_file = [word.strip().lower() for word in f.readlines()]


def word_ladder(start_word, end_word, dictionary_file=dictionary_file):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.

    HINT:
    See <https://github.com/mikeizbicki/cmc-csci046/issues/472> for a discussion about a common memory management bug that causes the generated word ladders to be too long in some cases.
    '''
    stack = deque([start_word])

    queue = deque()
    queue.append(stack)

    while queue:
        temp_stack = queue.popleft()
        temp_word = temp_stack[-1]
        for x in dictionary_file:
            if _adjacent(temp_word, x):
                if x == end_word:
                    temp_stack.append(x)
                    return temp_stack
                stack_copy = temp_stack.copy()
                stack_copy.append(x)
                queue.append(stack_copy)
                # print(queue)
                dictionary_file.remove(x)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    for i in range(len(ladder) - 1):
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    >>> _adjacent('shone','phony')
    False

    '''
    if len(word1) != len(word2):
        return False
    difference = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            difference += 1
        if difference > 1:
            return False
    return True
