Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> def negation(text):
	negated_words=["no","not","never","neither","none","nothing","none","nobody","n't"]
	if any(word in text for word in negated_words):
		return True
	else:
		return False

	
>>> negation("I haven't got a car.")
True
>>> negation("I am happy")
False
>>> 
>>> 
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
