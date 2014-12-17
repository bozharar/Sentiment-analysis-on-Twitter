Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> from nltk.tag import pos_tag
>>> from nltk.tokenize import word_tokenize
>>> from collections import Counter
>>> def POS(text):
	pos_tag(word_tokenize(text))
	return Counter([a for b,a in pos_tag(word_tokenize(text))])

>>> POS("I go to the cinema with my friends.")
Counter({'PRP$': 1, 'NN': 1, '.': 1, 'TO': 1, 'VBP': 1, 'PRP': 1, 'IN': 1, 'DT': 1, 'NNS': 1})
>>> 
>>> 
>>> 
>>> import langid
>>> langid.classify("This is a test for me")
('en', 0.9999999990566106)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def cluster(text):
	f=open("C:\\Users\\bozharar\\Desktop\\clusters.txt")
	for line in f:
		line=line.split()
		if text in line:
			print line

			
>>> cluster("not")
['^001000', '(28)', 'not', 'nt', 'nott', 'n0t', 'nawt', 'rightfully', 'nottt', 'nto', 'notttt', 'noot', 'nooot', 'not-', 'noooot', 'nottttt', 'deservedly', '_not_', 'naht', "n't", 'nnot', 'nooooot', 'notttttt', '-not-', 'noit', '/not/', 'youhave', 'noooooot', 'nottttttt', 'noht']
>>> 
>>> 
>>> def cluster(text):
	f=open("C:\\Users\\bozharar\\Desktop\\Brown_clusters.txt")
	for line in f:
		line=line.split()
		if text in line:
			print line

			
>>> cluster("not")
['1111001000', 'not', '150585']
>>> 
>>> 
>>> def cluster(text):
	f=open("C:\\Users\\bozharar\\Desktop\\Brown_clusters.txt")
	for line in f:
		line=line.split()
		if text in line:
			return ("cluster: ",line)

		
>>> cluster("not")
('cluster: ', ['1111001000', 'not', '150585'])

>>> 
>>> 
>>> def positive_emoticons_last_token(text):
	if text[-1]==(":), :-),=),;),:],:D,^-^,^_^"):
		return True
	return False

>>> positive_emoticons_last_token("Yesterday, I went to theatre and it was so funny :D")
False
>>> 
>>> 
>>> 
