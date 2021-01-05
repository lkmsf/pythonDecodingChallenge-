
def main():  
    key, msg = open("../../msg2.txt").read().split("\n\n") 
    key = key.splitlines()[1:]
    msg = msg.splitlines()[1] 
    
    d = {} 
    for line in key: 
        k, v = line.split(" -> ")
        d[k] = v

    for key, val in zip("abectik", "cebikta"): 
        d[key] = val 
        d[key.upper()] = val.upper()

    nMsg = ""
    for c in msg: 
        if c in d: 
            nMsg += d[c]
        else: 
            nMsg += c

    print(nMsg)

if __name__ == "__main__":
    main()
