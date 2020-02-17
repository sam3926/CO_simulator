
import re

reg=[]
for i in range(32):
    reg.append(0)

reg[1]=20
reg[2]=20

mem=[]
for i in range(1024):
    mem.append(0)

mem_index=0    
print(reg)

def sep(text):
    data_index_start=0
    command_index_start=0
    
    #for check in text:
    index=-1
    flag=False
    for test in text:
        sep = '//'
        test = test.split(sep, 1)[0]
        index=index+1
        expr = re.compile('.data')
        mo=expr.search(test)
        
        if mo:
            data_index_start=index
        
        expr = re.compile('.globl\s*main')
        mo=expr.search(test)
        if mo:
            command_index_start=index
        
    return text[data_index_start:command_index_start],text[command_index_start+1:]

# above this all the common function and memory allocation will be there
        
f=open("check.s",'r')
text=f.readlines()
dataseg,command=sep(text)

special_mem=[]
#data segment works starts here FUN START NOW :)
#print(dataseg)

def ldword(words):
    global mem_index
    for word in words:
        mem[mem_index]=int(word)
        mem_index+=1
        #print(mem[mem_index-1])
    print(mem[:mem_index])
    print(mem_index)
g=-1
def define_memory_chunk(name,words):
    global mem_index
    start=mem_index
    for word in words:
        mem[mem_index]=int(word)
        mem_index+=1
        #print(mem[mem_index-1])
    print(mem[:mem_index+1])
    end=mem_index-1
    segment=[]
    segment.append(name)
    segment.append(start)
    segment.append(end)
    special_mem.append(segment)
    print(special_mem)

while g<(len(dataseg)-1):
    g+=1
    test=dataseg[g]
    sep='//'
    if test is '\n':
        continue
    rest=test.split(sep,1)[0]
    if not rest:
        continue
    flag=False
    expr=re.compile('\w*\s\s*.word\s(\d*,\s*)*\d*\s*')
    
    mo=expr.search(rest)
    #checking for names memory
    if mo:
        flag=True
        ch=mo.group()
        ch=re.split('\W|,|$',ch)
        instr=[]
        for i in ch:
            if i:
                instr.append(i)
        
        #simplopr(instr)
        print(instr)
        define_memory_chunk(instr[0],instr[2:])
        
        
    if flag is not True:
        expr=re.compile('.word\s(\d*,\s*)*\d*\s*') # for simple word
        mo=expr.search(rest)
        if mo:
            flag=True
            ch=mo.group()
            ch=re.split('\W|,|$',ch)
            instr=[]
            for i in ch:
                if i:
                    instr.append(i)
        
        #simplopr(instr)
            print(instr)
        #ldword(instr[1:])
        
    #    define_memory_chunk('name',instr[1:])
    #print(test)
#data segment ends now
# command segment works from here


def simplopr(command):
    index=[]
    for rg in command[1:]:
        #print(ord(rg[0]))
        a=ord(rg[0])
        a=a-97
        index.append(a*10 + int(rg[1]))
    
    if i in index:
        if i not in range(32):
            print("Invalid Syntax")
    print(command[0])
    if command[0] == 'add':
        #print("ADDED")
        reg[index[0]]=reg[index[1]]+reg[index[2]]
    elif command[0] == 'sub':
        #print("SUBTRACTED")
        reg[index[0]]=reg[index[1]]-reg[index[2]]
    else:
        print("INVALID SYNTAX")
 

def srch( check,command,g):
    counter=-1
    for i in command:
        counter=counter+1
        sep = '//'
        if i is '\n':
            continue
        rest = i.split(sep, 1)[0]
        if not rest:
            continue
        expr=re.compile('\s*'+check+'[:]\s*')
        mo=expr.search(rest)
        flag=False
        if mo:
            flag=True
            if counter is not g:
                return counter
            
def comparison(instr,command,g):
    index=[]
    print(instr)
    for rg in instr[1:-1]:
        #print(ord(rg[0]))
        a=ord(rg[0])
        a=a-97
        index.append(a*10 + int(rg[1]))
    print(index)
    if instr[0] =='beq':
        if(reg[index[0]]==reg[index[1]]):
            print("EQUAL")
            return ((srch(instr[3],command,g))-1)
        else:
            return g
    elif instr[0] =='bne':
        if(reg[index[0]]==reg[index[1]]):
             print("EQUAL")
             return g
        else:
            return ((srch(instr[3],command,g))-1)
    else:
        print("INVALID SYNTAX")
        return g
        
        
g=-1
while g<(len(command)-1):
    g+=1
    #print(g)
    test=command[g]
    #print(test)
    sep = '//'
    if test is '\n':
        continue
    rest = test.split(sep, 1)[0]
    if not rest:
        continue
    flag=False
    # flag is used to keep the track of the number of instructions compiled in a step
    #for add sub and so on:)
    expr=re.compile('(\s*\w\w\w\s*\$\w\d\s*,\s*\$(\w\d|zero)\s*,\s*\$(\w\d|zero)\s*)')
    mo=expr.search(rest)
    
    if mo:
        flag=True
        ch=mo.group()
        ch=re.split('\W|,|$',ch)
        instr=[]
        for i in ch:
            if i:
                instr.append(i)
        
        simplopr(instr)
        print(instr)
    
    if flag is not True: #for bne and beq
        expr = re.compile('(\s*\w\w\w\s*\$(\w\d|zero)\s*,\s*\$(\w\d|zero)\s*,\s*(\w|\d)*\s*)')
        mo=expr.search(rest)
        if mo:
            flag=True
            ch=mo.group()
            ch=re.split('\W|,|$',ch)
            instr=[]
            for i in ch:
                if i:
                    instr.append(i)
            print(instr)
            g=comparison(instr,command,g)
            #g=(srch(instr[3],command,g))-1
            print(g)
            
    if flag is not True:  # for jump
        expr = re.compile('(\s*[j]\s\s*(\w|\d)*)')
        mo=expr.search(rest)
        if mo:
            flag=True
            ch=mo.group()
            ch=re.split('\W|,|$',ch)
            instr=[]
            for i in ch:
                if i:
                    instr.append(i)
            g=(srch(instr[1],command,g))-1
            #continue
            print(g)
            print(instr)
     
    if flag is not True:  # for LW and SW
        expr = re.compile('(\s*\w\w\s*\$\w\d\s*,(\s*(\d\(\$\w\d\))|(0x\d*)))')
        mo=expr.search(rest)
        if mo:
            flag=True
            ch=mo.group()
            ch=re.split('\W|,|$',ch)
            instr=[]
            for i in ch:
                if i:
                    instr.append(i)
            print(instr)
    
    if flag is not True:
        expr =re.compile('\s*(\w|\d)*')
        mo=expr.search(rest)
        if mo:
            flag=True
            
    if flag is not True:
        print("Invalid Syntax")
        break
print(reg)
