N = int(input())
word_dict = {chr(i): 0 for i in range(ord("A"), ord("Z") + 1)}

for n in range(N):
    word = input()
    for idx, i in enumerate(word, 1):
        word_dict[i] += 10 ** (len(word) - idx)
word_dict = list(word_dict.items())
word_dict.sort(key=lambda x: x[1], reverse=True)
word_dict = dict(word_dict)

result = 0
for idx, i in enumerate(word_dict):
    result += word_dict[i] * (9 - idx)
print(result)
