import string

def file_replace(fin):
    word1=list()
    f = open('new_file.cfg', 'w')
    for line in fin:
        print(line.replace('172','192'))
        f.write(line.replace('172','192'))




def main():
    fin = open("running-config.cfg")
    file_replace(fin)
if __name__ == '__main__':
    main()