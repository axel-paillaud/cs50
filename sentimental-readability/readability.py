from cs50 import get_string

def main():

    s = get_string("Text: ")
    count_letters(s)
    count_words(s)

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
    

if __name__ == "__main__":
    main()

