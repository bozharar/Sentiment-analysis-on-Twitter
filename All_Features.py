Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def getCharacterNgrams(wordlist,n):
	return [wordlist[i:i+n] for i in range(1+len(wordlist)-n)]

>>> getCharacterNgrams('selam belit naber',4)
['sela', 'elam', 'lam ', 'am b', 'm be', ' bel', 'beli', 'elit', 'lit ', 'it n', 't na', ' nab', 'nabe', 'aber']
>>> 
>>> 
>>> def wordNgram(text,n):
	text=text.split(' ')
	a=[]
	for i in range(len(text)-n+1):
		a.append(text[i:i+n])
	return a

>>> wordNgram("hey ay ben sen of gel kal git",3)
[['hey', 'ay', 'ben'], ['ay', 'ben', 'sen'], ['ben', 'sen', 'of'], ['sen', 'of', 'gel'], ['of', 'gel', 'kal'], ['gel', 'kal', 'git']]
>>> 
>>> 
>>> def number_of_questionmarks(text):
	return text.count("?")

>>> number_of_questionmarks("ben !! merhaba ! hey ?? ! yoy sen kim?")
3
>>> 
>>> 
>>> def question_marks(text):
	if text[-1]=="?":
		return True
	return False

>>> question_marks("ben !! merhaba ! hey ?? ! yoy sen kim?")
True
>>> 
>>> 
>>> def number_of_exclamationmarks(text):
	return text.count("!")

>>> number_of_exclamationmarks("ben !! merhaba ! hey ?? ! yoy sen kim?")
4
>>> 
>>> 
>>> def exclamation_marks(text):
	if text[-1]=="!":
		return True
	return False

>>> exclamation_marks("ben !! merhaba ! hey ?? ! yoy sen kim?!?!!")
True
>>> 
>>> 
>>> def number_of_allcaps(text):
	return sum(1 for c in text if c.isupper())

>>> number_of_allcaps("ABAKHvsjlf hlLLnlkþþ AAAAA bbbD")
13
>>> 
>>> 
>>> 
>>> def number_of_hashtags(text):
	return text.count("#")

>>> number_of_hashtags("ben #yarýn okula #gideceðim #arkadasýmlaberaber sen #napýcaksýn")
4
>>> 
>>> 
>>> 
>>> import re
>>> import collections
>>> from collections import Counter
>>> def number_of_hashtag(text):
	hashtag=re.findall(r"""(?:\#+[\w_]+[\w\'_\-]*[\w_]+)""",text)
	return Counter(hashtag)

>>> number_of_hashtag("ben #yarýn okula #gideceðim #arkadasýmlaberaber sen #napýcaksýn")
Counter({'#nap': 1, '#arkadas': 1, '#yar': 1, '#gidece': 1})
>>> 
>>> 
>>> def number_of_words(text):
	return len(text.split())

>>> number_of_words("show the bird to me hey yeey")
7
>>> 
>>> 
>>> 
>>> def avg_word_length(text):
	l = text.split()
	return sum([len(word) for word in l]) / len(l)

	
>>> 
>>> avg_word_length("What is your mom doing?")
3
>>> 
>>> 
>>> def long_words(text):
	word=text.split()
	if len(word)>15 in text:
		return True
	else:
		return False

	
>>> long_words("I am interested in artmusiccinematheatre.")
False
>>> 
>>> 
>>> def Twitter_username(text):
	username=re.findall(r"(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)", text)
	return username

>>> Twitter_username("@RayFranco is answering to @jjconti, this is a real '@username83' but this is an@email.com, and this is a @probablyfaketwitterusername")
['RayFranco', 'jjconti', 'username83', 'probablyfaketwitterusername']
>>> 
>>> 
>>> def url(text):
	urls=re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', text)
	return urls

>>> url("Today she worked on http://example.com and www.ku.edu.tr")
['http://example.com', 'www.ku.edu.tr']
>>> 
>>> 
>>> def term_split(text):
	for str in text.split():
		 if str.startswith('#'):
			 return str.split()

			
>>> term_split("hey yoo me #dayofthedream")
['#dayofthedream']
>>> 
>>> 
>>> 
>>> from nltk.corpus import stopwords
>>> stopword=stopwords.words('english')
>>> def stopwords(text):
	return [i for i in text.split() if i in stopword]

>>> stopwords("this is a foo bar sentence and example sentence for us to learn this subject")
['this', 'is', 'a', 'and', 'for', 'to', 'this']
>>> 
>>> 
>>> def stopwords(text):
	if [i for i in text.split() if i in stopword]:
		return True
	else:
		return False

	
>>> stopwords("foo bar sentence example sentence")
False
>>> 
>>> 
>>> 
>>> def stopwords(text):
	return Counter([i for i in text.split() if i in stopword])

>>> stopwords("this is a foo bar sentence and example sentence for us")
Counter({'this': 1, 'a': 1, 'is': 1, 'and': 1, 'for': 1})
>>> 
>>> 
>>> 
>>> def elongated_words(text):
	elong = re.compile(r"(.)\1{2}")
	return Counter([word for word in text.split() if elong.search(word)])

>>> elongated_words('soooo grrrrrrrrreat gone byee aaaaay')
Counter({'aaaaay': 1, 'soooo': 1, 'grrrrrrrrreat': 1})
>>> 
>>> 
>>> elongated_words('soo hiiiii whyyyy done')
Counter({'hiiiii': 1, 'whyyyy': 1})
>>> 
>>> 
>>> def emoticons(text):
	emoticon=re.findall(r"(?:[<>]?[:;=8][\-o\*\']?[\)\]\(\[dDpP/\:\}\{@\|\\]|[\)\]\(\[dDpP/\:\}\{@\|\\][\-o\*\']?[:;=8][<>]?)", text)
	return emoticon

>>> emoticons('I love to play voleyball with my sister ;)')
[';)']
>>> emoticons('I love :D to play voleyball with my sister ;)')
[':D', ';)']
>>> 
>>> def negation(text):
	negated_words=["no","not","never","neither","none","nothing","none","nobody","n't"]
	if any(word in text for word in negated_words):
		return True
	else:
		return False

	
>>> negation("I haven't got a car.")
True
>>> 
>>> negation("I am happy")
False
>>> 
>>> 
>>> def positive_emoticons(text):
	positive_emoticons=[':)', ':-)','=)',';)',':]',':D','^-^','^_^']
	if any(word in text for word in positive_emoticons):
		return True
	else:
		return False

		
>>> positive_emoticons("Yesterday, I went to theatre :(( and it was so funny")
False
>>> positive_emoticons("Yesterday, I went to theatre ^-^ and it was so funny")
True
>>> 
>>> 
>>> def negative_emoticons(text):
	negative_emoticons =[':(',':-(',':((','-.-','>:-(','D:',':/']
	if any(word in text for word in negative_emoticons):
		return True
	else:
		return False

	
>>> negative_emoticons("I heard that she is sick :-(")
True
>>> negative_emoticons("I heard that she is sick")
False
>>> 
>>> 
>>> 
>>> def positive_emoticons(text):
	positive_emoticons=[':)', ':-)','=)',';)',':]',':D','^-^','^_^']
	if any(word in text[-1] for word in positive_emoticons):
		return True
	else:
		return False

	
>>> positive_emoticons('Yesterday, I went to theatre and it was so funny :D ')
False
>>> 
>>> 
>>> 
>>> from nltk.tag import pos_tag
>>> from nltk.tokenize import word_tokenize
>>> def POS(text):
	pos_tag(word_tokenize(text))
	return Counter([a for b,a in pos_tag(word_tokenize(text))])

>>> POS("I go to the cinema with my friends.")
Counter({'PRP$': 1, 'NN': 1, '.': 1, 'TO': 1, 'VBP': 1, 'PRP': 1, 'IN': 1, 'DT': 1, 'NNS': 1})
>>> 
>>> 
>>> import langid
>>> langid.classify("This is a test for me")
('en', 0.9999999990566106)
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
>>> def positive_emoticons_last_token(text):
	if text[-1]==(":), :-),=),;),:],:D,^-^,^_^"):
		return True
	return False

>>> positive_emoticons_last_token("Yesterday, I went to theatre and it was so funny :D")
False
>>> 
>>> 
>>> 
>>> 
