#!/usr/bin/env python2
# This implementation is O(N) because it scans all the characters of
# each word once

def get_chars(word):
    h = {}
    for c in word:
        try:
            h[c] += 1
        except:
            h[c] = 1
    return h

def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    h1 = get_chars(word1)
    h2 = get_chars(word2)
    for k in h1.keys():
        try:
            if h1[k] != h2[k]:
                return False
        except:
            return False
    return True

pairs = [("hello", "oellho"),
         ("abc", "cda"),
         ("abc", "bca"),
         ("other", "othello"),
         ("this", "sith"),
        ]
for a, b in pairs:
    print "%s and %s is %d"%(a, b, is_anagram(a, b))

# The above is where it ends for Carbon phone interview
# Below implements the part for the Meraki interview which I FAILED

def is_anagram2(word_sorted, word2):
    return word_sorted == ''.join(sorted(word2))

words = [a for a, b in pairs]
words += [b for a, b in pairs]
h = {}
for w in words:
    s = ''.join(sorted(w))
    h[s] = {w}
    for w1 in words:
        #if is_anagram(w, w1):
        if is_anagram2(s, w1):
            h[s].add(w1)
for e in h:
    print ', '.join(h[e])
