# Twitter-Data-Analysis

Sentiment analysis on China-USA related topic collected from twitter.

## Data and Features
Twitter is the Major Source of data for this challenge. We will provide a pre-downloaded data on china-usa related topics. The data comes in two parts. 

- The [first](https://drive.google.com/file/d/1sfx50_tQ6jyBENo0L7hM3WL-11RhWqEB/view?usp=sharing) will be around 140mb of a raw twitter data dump in JSON format. This data is collected using the following keywords: [‘chinaus’, ‘chinaTaiwan’,  ‘chinaTaiwancrisis’, ‘taiwan’, ‘XiJinping’, ‘USCHINA’, ‘pelosi’, ‘TaiwanStraitsCrisis’, ‘WWIII’,  ‘pelosivisittotaiwan’],  

- The [second](https://drive.google.com/file/d/1219EjMcjCD4yLqTbBUauOE0-95dqhz4Q/view?usp=sharing) one will be around 130mb of the same format, but collected based on the original keyword plus country specific geocodes included e.g. ‘-28.479,26.128,400km  for South Africa. 

The final data represents a data drift that is common to many scenarios. You are expected to use the first data to build your model but set up a deployment strategy that will trigger an alert when data drift is detected. 

## Modules:
- Data exploration and pre-processing: perform data reading, pre-processing and data exploration and visualisations.
- Topic modelling and sentiment analysis: using scikit-learn, Gensim, or other packages and APIs to model the topics discussed in the tweets and their sentiments.Use word clouds, k-mean clustering, etc. as a simple model for topic modelling.
- Visualaization: Visualize the results on a dashboard

## Tools used
- scikit-learn, 
- Gensim,
- Pandas
- nktl
