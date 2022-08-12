import pandas as pd
import re

class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """
    def __init__(self, df:pd.DataFrame):
        self.df = df
        print('Automation in Action...!!!')
        
    def drop_unwanted_column(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        """
        unwanted_rows = df[df['retweet_count'] == 'retweet_count' ].index
        df.drop(unwanted_rows , inplace=True)
        df = df[df['polarity'] != 'polarity']
        
        return df
    def drop_duplicate(self, df:pd.DataFrame)->pd.DataFrame:
        """
        drop duplicate rows
        """
        df = df.drop_duplicates()

        return df

    def convert_to_datetime(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert column to datetime
        """
        df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
        
        return df
    
    def convert_to_numbers(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """
        df['polarity'] = pd.to_numeric(df['polarity'])
        df['subjectivity'] = pd.to_numeric(df['subjectivity'])
        df['retweet_count'] = pd.to_numeric(df['retweet_count'])
        df['favorite_count'] = pd.to_numeric(df['favorite_count'])

        return df
    
    def remove_non_english_tweets(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove non english tweets from lang
        """
        df = df[df['lang'] == 'en']

        return df
    
    def drop_nulls(self, df:pd.DataFrame)->pd.DataFrame:
        """
        drop rows that have null values
        """
        df = df.dropna(axis=0, how='any', inplace=False)

        return df
       
    def text_category(self, series:pd.Series)->pd.Series:
        """
        find the category of the tweet
        """
        polarities = []
        for polarity in series:
            if polarity < 0:
                polarities.append('negative')
            elif polarity > 0:
                polarities.append('positive')
            else:
                polarities.append('neutral')
        return polarities
    
    def fill_missing(self, df: pd.DataFrame, column: str, value: str = 'unknown'):
        """
        fill null values of a specific column with the provided value
        """

        df[column] = df[column].fillna(value)

        return df

    def replace_empty_string(self, df:pd.DataFrame, column: str, value: str):
        """
        replace empty strings in a specific column with the provided value
        """

        df[column] = df[column].apply(lambda x: value if x == "" else x)

        return df
    def remove_characters(self, df: pd.DataFrame, column: str):
        """
        removes non-alphanumeric characters with the exception of underscore hyphen and space
        from the specified column
        """

        df[column] = df[column].apply(lambda text: re.sub("[^a-zA-Z0-9\s_-]", "", text))

        return df
    def extract_device_name(self, df: pd.DataFrame) -> pd.Series:
        """
        returns device name from source text
        """
        df["source"] = df["source"].str.replace(r"(\s*\<.*?\>\s*)", " ", regex=True).str.strip()
             

        return df["source"]

if __name__ == "__main__":
    df = pd.read_csv("./processed_tweet_data.csv")
    clean_tweets = Clean_Tweets(df)
    df.to_csv('clean_tweets.csv', index=False)
    print('Automation Completed...!!!')
