# Write a function that, given a string of text (possibly with punctuation and line-breaks),
# returns an array of the top-3 most occurring words, in descending order of the number of occurrences.
# https://www.codewars.com/kata/51e056fe544cf36c410000fb

import re

def sanitize(str):
    # Define a pattern of characters to replace
    pattern = r"[#\\/.]" # This includes the characters #, \, / , .
    return re.sub(pattern, ' ', str).lower()

def sort_words(word_list):
    for i in range(len(word_list)):
        max_i = i
        for j in range(i + 1, len(word_list)):
            if word_list[j][1] > word_list[max_i][1]:
                max_i = j
        # Swap the elements
        word_list[i], word_list[max_i] = word_list[max_i], word_list[i]

    return [word[0] for word in word_list]

def top_3_words(str):
    sanitized_str = sanitize(str)
    words = {}

    # Define the regex pattern to match words with letters and optional apostrophes
    # \b ensures word boundaries, [A-Za-z] matches letters, and ' is allowed
    pattern = r"\b['A-Za-z']+\b"

    for word in re.findall(pattern, sanitized_str):
        words.setdefault(word, 0)  # Set default count to 0 if the word doesn't exist
        words[word] += 1

    sorted_words = sort_words(list(words.items()))

    if len(sorted_words) < 3:
        return sorted_words[:2] # only return the 2 most occured words
    else:
        return sorted_words[:3] # only return the 3 most occured words

test1 = {
    "input": "  //Wont won't won't",
    "output": ["won't", "wont"]
}

test2 = {
    "input": "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e",
    "output": ["e", "ddd", "aa"]
}

test3 = {
    "input": """In a village of La Mancha, the name of which I have no desire to call to
                mind, there lived not long since one of those gentlemen that keep a lance
                in the lance-rack, an old buckler, a lean hack, and a greyhound for
                coursing. An olla of rather more beef than mutton, a salad on most
                nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
                on Sundays, made away with three-quarters of his income.""",
    "output": ["a", "of", "on"]
}

test4 = {
    "input": "e 'e 'e 'e DDD dd'd DdD: dd'd dd'd aa' aA Aa, bb cc cC' e 'e 'e",
    "output": ["e", "ddd", "aa"]
}

solution1 = top_3_words(test1['input'])
solution2 = top_3_words(test2['input'])
solution3 = top_3_words(test3['input'])
solution4 = top_3_words(test4['input'])

if solution1 == test1['output']:
    print('success')
else:
    print('fail')

if solution2 == test2['output']:
    print('success')
else:
    print('fail')

if solution3 == test3['output']:
    print('success')
else:
    print('fail')

if solution4 == test4['output']:
    print('success')
else:
    print('fail')

print(f"input \"{test1['input']}\" should eq {test1['output']}")
print(f"your result was {solution1}")

print(f"input \"{test2['input']}\" should eq {test2['output']}")
print(f"your result was {solution2}")

print(f"input \"{test3['input']}\" should eq {test3['output']}")
print(f"your result was {solution3}")

print(solution4)
