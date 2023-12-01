"""
CS1026A 2023
Assignment 03 
Calzy Akmal Indyramdhani
251397118
cindyram@uwo.ca
November 12, 2023
"""

def read_keywords(keyword_file_name):

    keywords_dict = {}
    keywords = open(keyword_file_name, "r")
    
    try:
        for line in keywords:
            keyword, score_str = line.strip().split("\t")
            score = int(score_str)

            if keyword in keywords_dict:
                keywords_dict[keyword].append(score)
            else:
                keywords_dict[keyword] = score
        return keywords_dict

    except IOError:
        print(f"Could not open file {keyword_file_name}")
        return keywords_dict.clear()
    
    finally:
        keywords.close()


def clean_tweet_text(tweet_text):

    try:
        # Check if passed parameter is a String or not.
        if not isinstance(tweet_text, str):
            raise ValueError("Input must be a String.")

        tweet = tweet_text
        cleaned_tweet = []

        for s in tweet:
            if s.isalnum() or s.isspace():
                cleaned_tweet.append(s)
        cleaned_tweet = "".join(cleaned_tweet)        
        return cleaned_tweet.lower()
    
    except ValueError as err:
        print(f"Error, {str(err)}")    


def calc_sentiment(tweet_text, keyword_dict):
    
    sentiment_score = 0

    words = tweet_text.split()

    for word in words:
        if word in keyword_dict:
            sentiment_score += keyword_dict[word]
    
    return sentiment_score


def classify(score):
    
    classify_score = score
    final_classification = ""

    if classify_score > 0:
        final_classification = "Positive"
    elif classify_score == 0:
        final_classification = "Neutral"
    else:
        final_classification = "Negative"

    return final_classification


def read_tweets(tweet_file_name):
    
    tweet_list = []

    tweet_data = open(tweet_file_name, "r")
    
    try:
        for tweet in tweet_data:
            tweets = tweet.strip().split(",")
            
            # Ensure the tweet has the expected number of fields
            if len(tweets) == 11:

                try:
                    date, text, user, favorite, retweet, lang, country, state, city, lat, lon = (
                        str(tweets[0]),
                        str(tweets[1]),
                        str(tweets[2]),
                        int(tweets[3]),
                        int(tweets[4]),
                        str(tweets[5]),
                        str(tweets[6]),
                        str(tweets[7]),
                        str(tweets[8]),
                        float(tweets[9]),
                        float(tweets[10])
                    )
                except ValueError:
                    date, text, user, favorite, retweet, lang, country, state, city, lat, lon = (
                        "NULL", 
                        "NULL", 
                        "NULL", 
                        0, 
                        0, 
                        "NULL", 
                        "NULL", 
                        "NULL", 
                        "NULL", 
                        "NULL", 
                        "NULL"
                    )

                if str(tweets[1]).lower() != "null":
                    text = str(tweets[1]).lower()
                else:
                    text = "null"

                uninserted_tweet = {
                    'date': date,
                    'text': clean_tweet_text(text),
                    'user': user,
                    'favorite': favorite,
                    'retweet': retweet,
                    'lang': lang,
                    'country': country,
                    'state': state,
                    'city': city,
                    'lat': lat,
                    'lon': lon
                }

                new_tweet = {}
                for key, value in uninserted_tweet.items():
                    new_tweet[key] = value
                tweet_list.append(new_tweet)

        return tweet_list

    except IOError:
        print(f"Could not open file {tweet_file_name}")
        return tweet_list.clear()
    
    finally:
        tweet_data.close()


def make_report(tweet_list, keyword_dict):
    
    keywords = keyword_dict
    total_tweet = len(tweet_list)
    avg_favorite = 0
    avg_retweet = 0
    avg_sentiment = 0
    favorite_tweet = 0
    retweet_tweet = 0
    negative_tweet = 0
    neutral_tweet = 0
    positive_tweet = 0
    total_sentiment = 0
    top_countries_names = []
    country_sentiment_scores = {}

    for tweet in tweet_list:
        tweet_text = tweet['text']

        if tweet_text.lower() != "NULL":
            sentiment_score = calc_sentiment(tweet_text, keywords)
            tweet_value = classify(sentiment_score)
            total_sentiment += sentiment_score

            if tweet_value == "Positive":
                positive_tweet += 1
            elif tweet_value == "Negative":
                negative_tweet += 1
            else:
                neutral_tweet += 1
            
            if tweet['favorite'] != 0:
                favorite_tweet += 1
            
            if tweet['retweet'] != 0:
                retweet_tweet += 1

    if favorite_tweet != 0:
        avg_favorite = round(favorite_tweet / total_tweet, 2)
    else:
        avg_favorite = "NAN"
    
    if retweet_tweet != 0:
        avg_retweet = round(retweet_tweet / total_tweet, 2)
    else:
        avg_retweet = "NAN"

    if total_tweet != 0:
        avg_sentiment = round(total_sentiment / total_tweet, 2)
    else:
        avg_sentiment = "NAN"

    for tweet in tweet_list:
        country = tweet['country']
        if country != "NULL":
            country_sentiment_scores[country] = country_sentiment_scores.get(country, 0) + 1

    top_countries = sorted(country_sentiment_scores.items(), key=lambda x: x[1], reverse=True)[:5]
    for countries in top_countries:
        country_name = countries[0]
        top_countries_names.append(country_name)
    top_countries = ", ".join(top_countries_names)

    sentiment_report = {
        'avg_favorite': avg_favorite,
        'avg_retweet': avg_retweet,
        'avg_sentiment': avg_sentiment,
        'num_favorite': favorite_tweet,
        'num_negative': negative_tweet,
        'num_neutral': neutral_tweet,
        'num_positive': positive_tweet,
        'num_retweet': retweet_tweet,
        'num_tweets': total_tweet,
        'top_five': top_countries
    }

    return sentiment_report


def write_report(report, output_file):
    
    try:
        file_report = open(output_file, "w")
        
        file_report.write(f"Average sentiment of all tweets: {report['avg_sentiment']}\n")
        file_report.write(f"Total number of tweets: {report['num_tweets']}\n")
        file_report.write(f"Number of positive tweets: {report['num_positive']}\n")
        file_report.write(f"Number of negative tweets: {report['num_negative']}\n")
        file_report.write(f"Number of neutral tweets: {report['num_neutral']}\n")
        file_report.write(f"Number of favorited tweets: {report['num_favorite']}\n")
        file_report.write(f"Average sentiment of favorited tweets: {report['avg_favorite']}\n")
        file_report.write(f"Number of retweeted tweets: {report['num_retweet']}\n")
        file_report.write(f"Average sentiment of retweeted tweets: {report['avg_retweet']}\n")
        file_report.write(f"Top five countries by average sentiment: {report['top_five']}")
    
        print(f"Wrote report to {output_file}")

    except IOError:
        print(f"Could not open file {output_file}")
    
    finally:
        file_report.close()