
book = "books/XX.txt" 


def main():
    pswd = foo()   #TODO: 3 bugs 
    pswd = removeNonLtrs(pswd) #TODO: 1 bug

    lines = [58 ,43 ,13 ,57 ,79 ,84 ,73 ,88 ,14 ,52 ,72 ,94 ,24 ,109 ,81 ,105 ,88 ,87 ,39 ,99]
    words = [10 ,12 ,19 ,15 ,1 ,15 ,17 ,18 ,18 ,8 ,4 ,2 ,1 ,1 ,6 ,15 ,14 ,4 ,14 ,10]
    x = bar(words, lines)  #TODO: 3 bugs
    x = removeNonLtrs(x)  #still doesn't work
    z = pswd[::2]
    z += x[5:50]
    z = z[::-1]
    a = toLowerCase(z)  #TODO: 1 bug 
    a = removeDuplicateLetters(a) #TODO: 1 bug
    print(a)

def toLowerCase(a): 
    r = "" 
    for c in a: 
        r += a.lower() 
    return r

#aaaappppthg -> apthg 
def removeDuplicateLetters(param):  
    result = "" 
    prevLtr = ""
    for c in param: 
        if not c == prevLtr: 
            result += c
    return result 

def foo(): 
    r = "" 
    lines = [71 ,25 ,3 ,71 ,37 ,58 ,46 ,22 ,34 ,40 ,2 ,77 ,71 ,93 ,11 ,40 ,55 ,49 ,95 ,54 ,81 ,64 ,84 ,39 ,75
    with open(book) as f: 
        s = f.splitlines() 
        for l in lines: 
            r += s[l].split()[2]  
            r += s[l].split[-3]  
    return r

def bar(lines, words): 
    y = "" 
    with open(book) as f: 
        h = f.read().splitlines() 
        for idx in range(len(lines)): 
            l = lines[idx]
            w = words[idx]
            #Something weird it happening here - supposed to loop 5 prev, the num, and + 5 lines 
            for j in range(w - 5, w + 5): 
                if j < len(h[l].split()): 
                    y += h[l].split()[j][0]  #get first word
                    y += h[l].split()[j][-1  #get last word
    return y

# ",apple. jaksdf" -> "applejaksdf"
def removeNonLtrs(s): 
    r = "" 
    for c in s: 
        if c != " ":
            r += c
    return r

if __name__ == "__main__":
    main()
