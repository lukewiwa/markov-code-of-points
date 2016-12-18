import langid

with open('cop.txt') as f:
    text = f.readlines()


for line in text:
    language_test = langid.classify(line)
    if language_test[0] == 'en':
        with open('copenglish.txt', 'a+') as f:
            f.write(line)
