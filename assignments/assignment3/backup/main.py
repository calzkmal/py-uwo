"""
CS1026A 2023
Assignment 03 
Calzy Akmal Indyramdhani
251397118
cindyram@uwo.ca
November 12, 2023
"""

# Import the sentiment_analysis module
from sentiment_analysis import *

def main():
    # Get the keyword filename from the user
    keyword_filename = input("Input keyword filename (.tsv file): ")
    # Check if the filename has a ".tsv" extension
    if not keyword_filename.endswith(".tsv"):
        raise Exception("Must have tsv file extension!")
    
    # Same one for this
    tweet_filename = input("Input tweet filename (.csv file): ")
    if not tweet_filename.endswith(".csv"):
        raise Exception("Must have csv file extension!")

    # And same one for this
    report_filename = input("Input report filename (.txt file): ")
    if not report_filename.endswith(".txt"):
        raise Exception("Must have txt file extension!")

    # Read tweets from the tweet file and keywords from the keyword file
    tweet_list = read_tweets(tweet_filename)
    keyword_dict = read_keywords(keyword_filename)

    # Generate and then write the sentiment report using the provided functions
    final_report = make_report(tweet_list, keyword_dict)
    write_report(final_report, report_filename)

# Call the main function to execute the program
main()

''' TESTING ONLY

# text = read_keywords("keywords.tsv")
    # pprint(text)

    # print(clean_tweet_text("Java, Python, C++; endless possibilities await in the world of coding! http://t.co/ASD32S4S"))
    # print(clean_tweet_text(212))

    # pprint(read_keywords("keywords.tsv"))
    # save = read_tweets("adidas.csv")
    # pprint(save)

    # pprint(read_tweets("adidas.csv"))

    # try: 
    #     print()
    
    # except:
    #     print()

    # text_dict = read_keywords("keywords.tsv")
    # tweet_list = read_tweets("adidas.csv")

    # pprint(make_report(tweet_list, text_dict))

'''