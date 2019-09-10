text='中国+china2017 是-*/OK 很难a 也不难'
letter=0
chinese=0
number=0
sign=0
i=0
LETTER=0
slen=len(text)    
while i<slen:
    if ord(text[i])>127:       #ord() ASCII-->x 10进制
        chinese+=1
    elif (ord(text[i])>96 and ord(text[i])<123):
        letter+=1
    elif (ord(text[i])>47 and ord(text[i])<58):
        number+=1
    elif (ord(text[i])>64 and ord(text[i])<91):
        LETTER+=1
    else:
        sign+=1
    i+=1
print('English words %d,chinese %d,number %d,LETTER %d,sign %d'%(letter,chinese,number,LETTER,sign))
