
import re
f=open("check.s",'r')
text=f.readlines()

for test in text:
    sep = '//'
    rest = test.split(sep, 1)[0]
    
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

