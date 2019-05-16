#from nltk.corpus import stopwords
import xml.etree.ElementTree as ET
import re
import collections
#from porterStemmer import PorterStemmer
from nltk.stem.porter import PorterStemmer
from collections import defaultdict
p = PorterStemmer()
from array import array

#from collections import Counter
#cachedStopWords = stopwords.words("english")

#fp=open("mini_dumps/doc_test","r")
class CreateInvertedIndex:

    def __init__(self):
        self.index=defaultdict(list)
        global page_no
        page_no=0
        global tree
        tree = ET.parse('mini_dumps/doc_1.xml')
        
        global doc_no
        doc_no=1
        global cachedStopWords
        cachedStopWords=[".",",","<",">","{","}","|",":",";","?","!","@","#","$","%","^","&","*","a","(",")","*", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

         

    def collection_parsing(self):

        #tree = ET.parse('mini_dumps/doc_1.xml')
        if doc_no==15:
                if page_no>=106:
                    return {}
        if page_no>=500:

            global doc_no
            doc_no=doc_no+1
            
            
            global page_no
            page_no=0
            global tree
            tree=ET.parse('mini_dumps/doc_'+str(doc_no)+'.xml')
            global root
            root = tree.getroot()
            #root1=root
            #print('mini_dumps/doc_'+str(doc_no)+'.xml')

        #data=fp.read()
        
        #print(root)
        #dict_id={}
        #dict_title={}
    
        #for i in range(500):
        global root
        root=tree.getroot()
        
        
        #print(page_no)
        #dict_title[i]=title
        #dict_id[i]=iden
        #root=root1
        global root
        root=root[page_no]
        title=(root[0].text)   
        #print(title)   
        iden=(root[2].text)

        '''#print(dict_title.values())
        for page in root.findall('page'):
	    print page.find('text').text'''
        for text in root.iter('text'):
            data=(text.text)
        global page_no
        page_no=page_no+1
        if iden==None or title==None or text==None:
            return {}

        d={}
        d['id']=iden
        d['title']=title
        d['text']=data

        return d
    def writeIndexToFile(self):
        '''write the inverted index to the file'''
        #f=open(indexFile, 'w')
       # f=open('indexFile_'+str(doc_no), 'a')
        with open("IndexFile_"+str(doc_no), "a") as myfile:
            
            for term in self.index.keys():
                postinglist=[]
                for p in self.index[term]:
                    docID=p[0]
                    positions=p[1]
                    postinglist.append(':'.join([str(docID) ,','.join(map(str,positions))]))
           # print >> f, ''.join((term,'|',';'.join(postinglist)))
                print(''.join((term,'|',';'.join(postinglist))), end=" \n", file=myfile)
                    #myfile.write(''.join((term,'|',';'.join(postinglist))), end="", file=myfile)
           # print(f, ''.join((term,'|',';'.join(postinglist))))
            
       # f.close()


    def getTerms(self, line):
        '''given a stream of text, get the terms from the text'''
        line=line.lower()
        line=re.sub(r'[^a-z0-9 ]',' ',line)
        line=line.split()
        line=[x for x in line if x not in cachedStopWords]  
        line=[ p.stem(word) for word in line]
        return line

    def mainFunction(self):
        
        pagedict={}
        pagedict=self.collection_parsing()
        while pagedict != {}:                          
            lines='\n'.join((pagedict['title'],pagedict['text']))
            pageid=int(pagedict['id'])
            terms=self.getTerms(lines)
            
           
            termdictPage={}
            for position, term in enumerate(terms):
                try:
                    termdictPage[term][1].append(position)
                except:
                    termdictPage[term]=[pageid, array('I',[position])]
            
            
            for termpage, postingpage in termdictPage.items():
                self.index[termpage].append(postingpage)
            
            #pagedict=self.collection_parsing()
            if(page_no==500):
                self.index = collections.OrderedDict(sorted(self.index.items()))
                self.writeIndexToFile()
                #self.mainFunction()  
                pagedict={}
                self.index=defaultdict(list)
            pagedict=self.collection_parsing()
        if doc_no==15:
            self.index = collections.OrderedDict(sorted(self.index.items()))
            self.writeIndexToFile()

              #data= re.sub(r"\W+",' ',data)


if __name__=="__main__":
    c=CreateInvertedIndex()
    c.mainFunction()
