from gensim import corpora, models
from gensim.utils import SaveLoad
from gensim.matutils import corpus2csc, sparse2full, corpus2dense


class BuildModel():
    def __init__(self) -> None:
        pass

    def makeDict(self, myTweetList):
        """Create dictionary from list of tokenized documents"""
        return corpora.Dictionary(myTweetList)

    def makeCorpus(self, myTweetList, myDict):
        """Create corpus from list of tokenized documents"""
        return [myDict.doc2bow(tweet) for tweet in myTweetList]
    
    def createLDA(self, myCorpus, myDictionary, myTopics = 50, myPasses = 10, myIterations = 50, myAlpha=0.001):
        """LDA model call function"""
        return models.LdaMulticore(myCorpus, id2word=myDictionary, num_topics=myTopics, passes=myPasses, iterations=myIterations, alpha=myAlpha)
    
    def saveModelObjects(self, myLda, myModelName, myCorp, myCopName, myDict, myDictName):
        """Save model objects"""
        SaveLoad.save(myLda, myModelName)
        corpora.MmCorpus.serialize(myCopName, myCorp)
        myDict.save(myDictName)
        print("Model Objects Successfully SAVED!")