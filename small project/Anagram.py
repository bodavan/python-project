# Python Program to Check if Two Strings are Anagram

# method -1

def check(s1,s2):
    sort_s1 = sorted(s1)
    sort_s2 = sorted(s2)
    if sort_s1 == sort_s2:
        print("the string are anagram")
    else:
        print("the string aren't anagrams.")

s1 = "listen"
s2 = "silent"
check(s1,s2)


# method 2:
word1 = input("enter your first word: ")
word2 = input("enter your second word: ")

x = [word1[i] for i in range(0,len(word1))]
x.sort()
y = [word2[i] for i in range(0,len(word2))]
y.sort()

if x == y:
    print("the string are anagrams.")
else:
    print("the words are not anagrams")