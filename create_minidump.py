PAGE_LIMIT=500
cnt=0
doc_id=1
MINI_DUMPS="mini_dumps"
filename=MINI_DUMPS+"/doc_1"
fw=open(filename,"w")
with open("wiki_dump.xml") as infile:
    for line in infile:
    	fw.write(line)
    	if(line.strip()=='</page>'):
    		cnt=cnt+1

    		if(cnt==PAGE_LIMIT):
    			doc_id+=1
    			fw.close()
    			filename=MINI_DUMPS+"/doc_"+str(doc_id)
    			fw=open(filename,"w")
    			cnt=0
    	
fw.close()
