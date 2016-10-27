import os

fileNameIndex = { }
dirIndex = { }
textIndex = { }
def myCrawler(): # Retriving file names and directory names # Enter starting path from where 
    for dirname, dirnames, fileNames in os.walk("E:\\6.00x Files"):
        # print path to all fileNames.
        for filename in fileNames:
            # concatinating the file names with their paths
            path = os.path.join(dirname, filename)
            # Filtering out the text files through .txt extension
            if (os.path.splitext(filename)[1]=='.txt'):
                # Opening the text files to parse their content
                with open(path,'r') as f:
                    for line in f:
                        for word in line.split():
                            if word not in textIndex:
                                textIndex[word]=[]
                            if path not in textIndex[word]:
                                textIndex[word].append(path)

            wordList = os.path.splitext(filename)[0]


        # print path to all subdirectories first.
        for subdirname in dirnames:
            wordList=subdirname.split(' ')
            for word in wordList:
                if word not in dirIndex:
                    dirIndex[word]=[]
                dirIndex[word].append(path)


if __name__ == '__main__':
    print("Crawling and indexing")
    myCrawler()

inp=1
while(inp!=0):
    inp = raw_input("1. For searching in readable files\n2. For reading in files, in filenames & directories\n0 To exit: ")

    if int(inp)==1:
        temp=raw_input("Enter the word: ")

        if temp not in textIndex:
            print("Not found!")
            continue
        temp=textIndex[temp]
        for path in temp:
            print (path)

    elif int(inp)==2:
        word=raw_input("Enter the word: ")

        if word in textIndex:
            temp=textIndex[word]
            print("In readable files: ")
            for path in temp:
                print (path)
        if word in fileNameIndex:
            temp=fileNameIndex[word]
            print("In files names: ")
            for path in temp:
                print (path)
        if word in dirIndex:
            temp=dirIndex[word]
            print("In Directory names: ")
            for path in temp:
                print (path)

    elif int(inp)==0:
        exit()


