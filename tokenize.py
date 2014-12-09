fh = open("Territory.txt")
text=fh.read()
toks=text.split()
gloss = list()
ngloss=list()                       # empty list

for onetok in toks:
    tok = onetok.rstrip('" .,\/?!')

    if tok not in gloss:            # Add new TOKs 
        gloss.append(tok)
        ngloss.append(1)
        #print "TOK",tok,"GLOSS",gloss,"NGLOSS",ngloss
    else:
        iposn = 0
        for item in gloss:
            if tok == item:
                ngloss[iposn] = ngloss[iposn] + 1
                
            else:
                iposn=iposn+1
                
    #z=raw_input("PAUSE")
 #   print tok

gloss.sort()
#print gloss
fhout = open("Glossary.txt",'w')
i=0
for item in gloss:
    k=ngloss[i]
    outbuff=item+"  "+str(k)
    fhout.write(outbuff)
    fhout.write('\n')
    i = i+1
fhout.close()

