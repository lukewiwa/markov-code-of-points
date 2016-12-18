import markovify

with open('copenglish.txt') as f:
    text = f.read()

text_model = markovify.Text(text)

def sentences(repeats=1):
    for i in range(repeats):
        print(text_model.make_short_sentence(140))

if __name__ == '__main__':
    sentences()
