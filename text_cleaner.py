import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from re import sub

nltk.download()

class TextCleaner():
    def __init__(self, tweetList:list) -> None:
        self.wnl = WordNetLemmatizer()
        self.tweetList = tweetList

    def removePunc(self, myWord: str) -> str:
        """Method to remove punctuation from string inputs """
        if myWord is None:
            return myWord
        else:
            return sub('[.:;()/!&-*@$,?^\d+]', '', myWord)

    def removeAscii(self, myWord):
        """Method to remove ASCII from string input"""
        if myWord is None:
            return myWord
        else:
            return str(sub(r'[^\x00-\x7F]+','', myWord.strip()))

    def lemmatize(self, myWord):
        """Method to lemmatize words"""
        if myWord is None:
            return myWord
        else:
            return str(self.wnl.lemmatize(myWord))

    def removeStopWords(self, myWord):
        """Method to remove  stop words"""
        if myWord is None:
            return myWord
        if myWord not in str(stopwords.words('english')):
            return myWord

    def removeLinkUser(self, myWord):
        """Method to remove web addresses and twitter handles"""
        if not myWord.startswith('@') and not myWord.startswith('http'):
            return myWord

    def prepText(self, myWord):
        """Final text pre-processing method"""
        return self.removeStopWords(self.lemmatize(self.removeAscii(self.removePunc(self.removeLinkUser(myWord.lower())))))

    def filterTweetList(self):
        """Remove stop words, lemmatize, and clean all tweets"""
        self.tweetList = [[self.prepText(word) for word in tweet.split(
        ) if self.prepText(word) is not None] for tweet in self.tweetList]

