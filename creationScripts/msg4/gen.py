
def main():
    with open("orig.txt") as f: 
       inp = f.read() 
    
    inp, email = inp.split("\n\n\n")

    result = "" 
    key = "oteliforbtatadmtcetebtmynswtifephroelotnronseoebuymlducngmednpgiarseopetsblgngmdrpiwrhdkoeseorvteftgoretorseopretnysayndicateftgonmoswsecadiduhtdetlthsysretnysidaltlmcretnys"

    for i, e in enumerate(email): 
        result += chr(ord(e) - (ord("a") - ord(key[i % len(key)]))) 
    inp += "\n\n\n" + result 

    result = "" 
    for i in inp: 
        result += chr(ord(i) - 3) 
    
    with open("../../msg4.txt", "w") as f: 
       f.write(result) 


if __name__ == "__main__":
    main()
