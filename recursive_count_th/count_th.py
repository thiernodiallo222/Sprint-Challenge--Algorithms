'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2:
        return 0
    if len(word) == 2 and word.lower == 'th':
        return 1
    else:
        count_th(word[0:len(word)-1])
    return count 

