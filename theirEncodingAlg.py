#using instead of random library so it's deterministic cross platform/python version
from numpy import random 

fileName = "file.txt" 

def main():
    with open(fileName) as f: 
        origText = f.read() 
    
    encodedText = "" 
    for word in origText.split(): 
        if len(word) <= 2: 
            encodedText += word + " "
            continue 

        #shuffle inner word except for outer characters 

        #map from original index to new shuffled index 
        charMap = {} 

        #keep first letter and last letter the same 
        charMap[0] = 0 
        charMap[len(word) - 1] = len(word) - 1

        #shuffle the inner word
        random.seed(ord(word[0]) + ord(word[-1]))                #first and last letters don't change 
        randomIndecies = list(range(1, len(word) - 1)) #randomize middle indecies 
        random.shuffle(randomIndecies)

        for i in range(len(randomIndecies)): 
            charMap[i + 1] = randomIndecies[i]             #map old index to index of new letter 

        #recreate shuffled word
        for i in range(len(word)): 
            encodedText += word[charMap[i]] 
        encodedText += " "
    
    with open(fileName, "w") as f: 
        f.write(encodedText)
        

if __name__ == "__main__":
    main()
