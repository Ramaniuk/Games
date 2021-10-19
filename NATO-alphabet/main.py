import pandas

phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

words_dict = {}
for (index, row) in phonetic_alphabet.iterrows():
    words_dict[row.letter] = row.code
#words_dict = {row.letter : row.code for(index, row) in phonetic_alphabet.iterrows()}


def generate_phonetic():
    name = (input("Enter your name: ")).upper()
    try:
        # words_list = []
        # for letter in name:
        #     words_list.append(words_dict[letter])
        words_list = [words_dict[letter] for letter in name]
    except KeyError:
        print("Only letters in the alphabet please")
        generate_phonetic()
    else:
        print(words_list)

generate_phonetic()

