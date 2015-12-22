import sys
import json
#from nltk import word_tokenize
from _collections import defaultdict
from operator import itemgetter, attrgetter
counts=defaultdict(int)
tot_count= 0 

def lines(fp):
    
    for  tweet in fp.readlines():
	tweet_text = json.loads(tweet)
	if 'entities' in tweet_text:
            tcount(tweet_text['entities']['hashtags'])
    ht_with_fr = counts.items()
    top10=sorted(ht_with_fr,key=(itemgetter(1)),reverse=True)[0:10]	
    for i in top10:
	print i[0] +'\t'+str(i[1])
def tcount(ht):
    for tag in ht:
    	words = tag['text'].lower().split()
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
