import sys
import json
#from nltk import word_tokenize
from _collections import defaultdict

counts=defaultdict(int)
tot_count= 0 

def lines(fp):
    
    for  tweet in fp.readlines():
	tweet_text = json.loads(tweet)
	if 'text' in tweet_text:
            tcount(tweet_text['text'])

    for k,v in counts.items():
	#print k +'\t'+ str(1.0*v/tot_count)
	print (k +'\t'+ str(1.0*v/tot_count)).encode('utf-8')	
def tcount(text):
    global tot_count
    words = text.lower().split()
    tot_count = tot_count + len(words)
    for w in words:
	 counts[w]=counts[w]+1

	
def main():
    tweet_file = open(sys.argv[1])
    #hw()
    #lines(sent_file)
    #build_dict(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
