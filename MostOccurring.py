import glob
import os

def extractMostCommonWords():
    print("Extracting the most common words from the text files in this folder")
    wordCount = {}
    for filename in glob.glob('*.txt'):
        with open(os.path.join(os.getcwd(), filename), 'r', encoding='UTF-8') as f: 
            for word in f.read().lower().split():
                word = word.replace(".","")
                word = word.replace(",","")
                word = word.replace(":","")
                word = word.replace("\"","")
                word = word.replace("!","")
                word = word.replace("â€œ","")
                word = word.replace("â€˜","")
                word = word.replace("*","")
                word = word.replace("\xa2", "")
                if(word not in wordCount):
                    wordCount[word] = 1
                else: wordCount[word] +=1
                        
    print(dict(sorted(wordCount.items(), key=lambda item: -item[1])))



if __name__=="__main__":
    extractMostCommonWords()
