from cs50 import get_string

def main():

    s = get_string("Text: ")
    letters = count_letters(s)
    words = count_words(s)
    sentences = count_sentences(s)

    L = letters * 100 / words
    S = sentences * 100 / words

    indexFloat = 0.0588 * L - 0.296 * S - 15.8
    index = round(indexFloat)
    print(index)

def count_letters(sentences):
    count_letters = 0
    for i in range(len(sentences)):
        c = sentences[i]
        if(c.isalpha()):
            count_letters += 1
    return count_letters

def count_words(sentences):
    word_list = sentences.split()
    count_words = len(word_list)
    return count_words

def count_sentences(sentences):
    excl = sentences.count('!')
    interr = sentences.count('?')
    point = sentences.count('.')
    count_sentences = excl + interr + point
    return count_sentences

if __name__ == "__main__":
    main()

