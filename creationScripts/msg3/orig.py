
book = "books/hp.txt" 

def main():
    pswd = foo() 
    pswd = removeNonLtrs(pswd)

    lines = [58 ,43 ,13 ,57 ,79 ,84 ,73 ,88 ,14 ,52 ,72 ,94 ,24 ,109 ,81 ,105 ,88 ,87 ,39 ,99]
    words = [10 ,12 ,19 ,15 ,1 ,15 ,17 ,18 ,18 ,8 ,4 ,2 ,1 ,1 ,6 ,15 ,14 ,4 ,14 ,10]
    x = bar(lines, words) 
    x = removeNonLtrs(x)
    z = pswd[::2]
    z += x[5:50]
    z = z[::-1]
    a = toLowerCase(z)
    a = removeDuplicateLetters(a) 
    print(a) 

def toLowerCase(a): 
    r = "" 
    for c in a: 
        r += c.lower() 
    return r

#aaaappppthg -> apthg 
def removeDuplicateLetters(param):  
    result = "" 
    prevLtr = ""
    for c in param: 
        if not c == prevLtr: 
            result += c
        prevLtr = c
    return result 

def foo(): 
    r = "" 
    lines = [71 ,25 ,3 ,71 ,37 ,58 ,46 ,22 ,34 ,40 ,2 ,77 ,71 ,93 ,11 ,40 ,55 ,49 ,95 ,54 ,81 ,64 ,84 ,39 ,75]
    with open(book) as f: 
        s = f.read().splitlines() 
        for l in lines: 
            r += s[l].split()[2]  
            r += s[l].split()[-3]  
    return r

def bar(lines, words): 
    y = "" 
    with open(book) as f: 
        h = f.read().splitlines() 
        for idx in range(len(lines)): 
            l = lines[idx]
            w = words[idx]
            for j in range(w - 5, w + 6): 
                if j < len(h[l].split()): 
                    y += h[l].split()[j][0]
                    y += h[l].split()[j][-1]
    return y

def removeNonLtrs(s): 
    r = "" 
    for c in s: 
        if c.isalpha():
            r += c
    return r

if __name__ == "__main__":
    main()
