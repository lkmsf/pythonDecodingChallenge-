from numpy import random #using instead of random library so it's deterministic cross platform/ pyhton version

def main():
    with open("../../msg1.txt") as f: 
        origText = f.read() 
    
    unencodedText = "" 
    for word in origText.split(): 
        if len(word) <= 2: 
            unencodedText += word + " "
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
            charMap[randomIndecies[i]] = i + 1         #map old index to index of new letter 

        #recreate shuffled word
        for i in range(len(word)): 
            unencodedText += word[charMap[i]] 
        unencodedText += " "
    
    print(unencodedText) 

if __name__ == "__main__":
    main()
