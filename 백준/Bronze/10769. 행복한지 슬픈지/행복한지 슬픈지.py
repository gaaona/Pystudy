emoticon_dict = {
    ':-)' : 0,
    ':-(' : 1
}

count_list = [0,0]

sentence = input()

for i in range(len(sentence)-2):
    if sentence[i:i+2] == ':-':
        count_list[emoticon_dict[sentence[i:i+3]]] += 1

happy = count_list[0]
sad = count_list[1]

if happy == sad and sad == 0:
    print('none')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
else:
    print('unsure')