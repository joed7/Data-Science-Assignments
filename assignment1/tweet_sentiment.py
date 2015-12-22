import sys
import json

scores={}
def hw():
    print 'Hello, world!'

def build_dict(afinnfile):
    for line in afinnfile:
	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
 	scores[term] = int(score)  # Convert the score to an integer.

def lines(fp):
    
    for  tweet in fp.readlines():
	tweet_text = json.loads(tweet)
	if 'text' in tweet_text:
            score=tscore(tweet_text['text'])
	    print str(score)	
	else:
            print str(0)           	
def tscore(text):
    val=0
    words = text.lower().split()
    for w in words:
	if w in scores:
	    val = val+scores[w]	
    return val		
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    build_dict(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
