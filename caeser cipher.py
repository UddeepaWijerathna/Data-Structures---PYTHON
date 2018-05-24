
def decrypt():
    sentence=input(">>>:")
    x=sentence.upper()
    ascii_code=''
    for i in x:
        ascii=ord(i)
        
        if ascii==65:
            ascii=89
        elif ascii==66:
            ascii=90        
        else:
            ascii=ascii-2

        ascii_code+=str(ascii)
        list=[]
        for i in ascii_code:
            list.append(i)
        word=''
        while not len(list)==0:        
            num=int(str(list.pop(0))+str(list.pop(0)))        
            letter=chr(num)
            word+=letter

    print(word)      
decrypt()
