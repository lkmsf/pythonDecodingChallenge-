
def main():
    with open("../../msg4.txt") as f: 
       inp = f.read() 

    result = "" 
    for i in inp: 
        result += chr(ord(i) + 3) 
    
    final, email = result.split("\n\n\n")
    print(email)

    result = "" 
    key = "oteliforbtatadmtcetebtmynswtifephroelotnronseoebuymlducngmednpgiarseopetsblgngmdrpiwrhdkoeseorvteftgoretorseopretnysayndicateftgonmoswsecadiduhtdetlthsysretnysidaltlmcretnys"
    for i, e in enumerate(email): 
        result += chr(ord(e) + (ord("a") - ord(key[i % len(key)]))) 

    final += "\n\n" + result 
    
    print(final)

if __name__ == "__main__":
    main()
