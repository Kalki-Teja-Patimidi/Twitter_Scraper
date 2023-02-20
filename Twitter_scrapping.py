import streamlit as st
import pandas as pd
import snscrape.modules.twitter as sntwitter
from datetime import datetime, timedelta
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["twitter_data"]


# Define function to scrape Twitter data and store in MongoDB
def scrape_twitter_data(keyword, since_date, until_date, limit):
    # Create empty list to store tweets
    tweets = []

    # Format dates for use in Twitter search query
    since_date_str = since_date.strftime("%Y-%m-%d")
    until_date_str = until_date.strftime("%Y-%m-%d")

    # Define Twitter search query
    query = f"{keyword} since:{since_date_str} until:{until_date_str} lang:en"

    # Use snscrape to scrape Twitter data
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= limit:
            break
        tweets.append({
            "date": tweet.date.strftime("%Y-%m-%d %H:%M:%S"),
            "id": tweet.id,
            "url": tweet.url,
            "content": tweet.content,
            "user": tweet.username,
            # "reply_count": tweet.replyCount,
            # "retweet_count": tweet.retweetCount,
            # "language": tweet.lang,
            # "source": tweet.sourceLabel,
            # "like_count": tweet.likeCount
        })

    # Store tweets in MongoDB
    store_data_in_mongodb(keyword, since_date_str, until_date_str, tweets)

    # Return tweets as Pandas dataframe
    return pd.DataFrame(tweets)


# Define function to store Twitter data in MongoDB
def store_data_in_mongodb(keyword, since_date, until_date, tweets):
    if not tweets:
        return
    collection_name = f"{keyword}_{since_date}_{until_date}"
    collection = db[collection_name]
    collection.insert_many(tweets)


# Define Streamlit app
def app():
    # Set Streamlit app title
    st.title("Twitter Data Scraper")

    # Get user inputs for keyword, date range, and tweet limit
    keyword = st.text_input("Enter a keyword or hashtag to search for")
    since_date = st.date_input("Enter the start date for the search range")
    until_date = st.date_input("Enter the end date for the search range")
    limit = st.number_input("Enter the maximum number of tweets to scrape", min_value=1, max_value=1000, step=1)

    # Scrape Twitter data and display in table
    if st.button("Scrape and Download Twitter Data"):
        # Scrape Twitter data and store in MongoDB
        tweets_df = scrape_twitter_data(keyword, since_date, until_date + timedelta(days=1), limit)
        st.write(tweets_df)

        # Download Twitter data as CSV or JSON
        csv_data = tweets_df.to_csv(index=False)
        json_data = tweets_df.to_json(orient="records")

        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name=f"{keyword}_{since_date}_{until_date}.csv",
            mime="text/csv"
        )

        st.download_button(
            label="Download JSON",
            data=json_data,
            file_name=f"{keyword}_{since_date}_{until_date}.json",
            mime="application/json"
        )

        st.write(f"Saved {len(tweets_df)} tweets to CSV and JSON files.")


app()
