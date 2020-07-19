'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurence of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    substring = "th"
    count = 0

    index = word.find(substring)
    if index >= 0:
        count += 1
        word = word[index + len(substring):]

        # increment count by recursively calling count_th
        count += count_th(word)
    return count 
    # if len(word) < 2:
    #     count = 0
    #     return count 
    # if len(word) == 2 and word.lower == 'th':
    #     count = 1
    #     return count
    # sub_str = word[len(word) - 2:len(word) - 1]
    # if sub_str.lower == 'th':
    #     count += 1
    #     return count 
    # return count+count_th(word[:])


