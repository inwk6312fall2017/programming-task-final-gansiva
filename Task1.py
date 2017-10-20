#fin1=open("Book1.txt")
#fin2=open("Book2.txt")
#fin3=open("Book3.txt")
import string
def find_biggest(filename):
    """Find the biggest word in the book"""
    d = dict()
    for line in open(filename):
        line = line.replace('-', ' ')
        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace)
            #word = word.strip().lower()
            #print(word)
            d[word] = d.get(word, 0) + 1
    for i in range(len(d)):
        if len(d[i])<len(d[i+1]):
            length=len(d[i+1])
        elif len(d[i])>len(d[i+1]):
            length=len(d[i])
    return length

def main():
    find_biggest("Book1.txt")

if __name__ == '__main__':
    main()