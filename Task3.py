import string

def file_replace(fin):
    word1=list()
    f = open('new_file.cfg', 'w')
    for line in fin:
        print(line.replace('172','192'))
        f.write(line.replace('172','192'))


def file_access_list(fin):
    word1 = list()
    list1 = list()
    d = dict()
    for line in fin:
        word = line.strip()
        word1.append(word.split("!"))
        print(word1)
    for item in word1:
        if "access-list" in str(item):
            for item1 in item:
                list1 = (item1.split())
                d[list1[1]] = item1
                print(d)
    for item in d:
        print(item, d[item])
    
def main():
    fin = open("running-config.cfg")
    file_replace(fin)
    file_access_list(fin)
if __name__ == '__main__':
    main()