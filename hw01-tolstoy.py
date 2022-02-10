import string
import urllib.request
file = urllib.request.urlopen('https://www.gutenberg.org/files/2600/2600-h/2600-h.htm')
punc_removed = []
def remove_punctuation(s):
    n = s.split()
    for r in n:
        p = r.decode('UTF-8')
        for i in range(0, len(p)):
            if p[i] in string.punctuation:
                p = p.replace(p[i], ' ')
        punc_removed.append(p)
    return punc_removed

def print_unique(s):
    unique_words = []
    list1 = [p.replace(" ", "") for p in s]
    for word in list1:
        word = word.upper()
        if word not in unique_words:
            unique_words.append(word)
    return unique_words


def main():
    content = file.read()
    print('Total number of Unique words in HTML are :',len(print_unique(remove_punctuation(content))))

main()
