import string
def find_biggest(filename):
    """Find the biggest word in the book"""
    d = dict()
    d2=dict()
    max_length=0
    for line in open(filename):
        line = line.replace('-', ' ')
        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace)
            d[word] = d.get(word, 0) + 1
    for i in d:
        d2[i]=len(i)
    for key,value in d2.items():
        if value>max_length:
            max_length=value
            print(key,value)

def main():
    print("In Book1.txt")
    find_biggest("Book1.txt")
    print("In Book2.txt")
    find_biggest("Book2.txt")
    print("In Book3.txt")
    find_biggest("Book3.txt")
if __name__ == '__main__':
    main()