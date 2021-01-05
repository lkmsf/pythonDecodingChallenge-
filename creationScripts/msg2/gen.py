import random 

#alphabet minus bhjkl
ALPH = "abcdefghijklmnopqrstuvwxyz"
#"abectik" should map to "cebikta"

def main():
    aCopy = [x for x in ALPH if x not in "abectik"]
    orig = aCopy.copy() 
    random.shuffle(aCopy)
    
    #line below would be better as a for loop but I wanted practice with more complex list comprehensions 
    eD = {key: value for k, v in zip(orig, aCopy) for key, value in zip([k, k.upper()], [v, v.upper()])}
    for val, key in zip("abectik", "cebikta"): 
        eD[key] = val 
        eD[key.upper()] = val.upper()

    #encode message 
    encodedMsg = ""
    with open("orig.txt") as f2: 
        for c in f2.read(): 
            if c not in eD: 
                encodedMsg += c
            else: 
                encodedMsg += eD[c]

    #write message and key 
    with open("../../msg2.txt", "w") as f: 
        f.write("Key: \n")

        for nL, oL in zip(orig, aCopy): 
            f.write(oL + " -> " + nL + "\n")

        f.write("\n Message: \n")
        f.write(encodedMsg)

if __name__ == "__main__":
    main()
