n = int(input())
for x in range(n):
    word = input()
    if(len(word) > 10):
        newWord = word[0] + str(len(word)-2) + word[-1]
    else:
        newWord = word
    print(newWord)