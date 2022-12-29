import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from gensim.matutils import corpus2csc, sparse2full, corpus2dense
from wordcloud import WordCloud


class Visualize():
    def __init__(self) -> None:
        pass

    def translateLdaIdx(self, myLdaViz):
        """Translate lda model topics to match the topics in pyLDAvis visualization"""
        ldaVizIdx = myLdaViz[0].index
        return list(ldaVizIdx)
    
    def createDenseMat(self, myLdaModel, myCorpus, newIdx):
        """Transform corpus to dataframe with topics matching lda visulization """
        numTopics = myLdaModel.num_topics
        myDense = corpus2dense(myLdaModel[myCorpus], numTopics)
        myDf  = pd.DataFrame(myDense)
        mySortedDf = myDf.transpose()
        mySortedDf = myDf.transpose()[newIdx]
        mySortedDf.columns = ['topic' + str(i + 1) for i in range(numTopics)]
        return mySortedDf
    
    def sortByTopicToIdx(self, cleanedTweetList, mySortedDf, myTopic, myTopicThresh=0.1):
        """Returns  an index of tweets surpassing a topic value threshold"""
        myCleanArray = np.array(cleanedTweetList)
        srtIdx = list(mySortedDf[mySortedDf[myTopic]>myTopicThresh].index)
        return srtIdx

    def sortTweetsByIdx(self, cleanedTweetList, srtIdx):
        """Returns sorted tweets as a list based on a defined sort index"""
        myCleanArray = np.array(cleanedTweetList)
        srtTweets = list(myCleanArray[srtIdx])
        return srtTweets

    def makeWordCloud(self, cleanedTweetList, mySortedDf, myTopic, myTopicThresh=0.1):
        """Create world cloud of tweets passing a given threshold for a given topic"""
        sortedIdx = self.sortByTopicToIdx(cleanedTweetList, mySortedDf, myTopic, myTopicThresh=0.1 )
        mySortedTweets = self.sortTweetsByIdx(cleanedTweetList, sortedIdx)
        filteredWords = ' '.join([' '.join(string) for string in mySortedTweets])
        myTopicCloud = WordCloud(max_font_size=100, scale=8).generate(filteredWords)
        fig = plt.figure(figsize=(10,10), dpi=1600)
        plt.imshow(myTopic)
        plt.axis('off')
        plt.show()