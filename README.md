# Twitter Data Scraper
- Twitter Data Scraper is a Python script that allows you to scrape tweets that match a particular keyword and date range, and store the scraped data in a MongoDB database. The script also provides the option to download the scraped data in CSV or JSON format.

##### Getting Started
- These instructions will get you a copy of the project up and running on your local machine.

##### Prerequisites
- Python 3.x
- MongoDB

### Installing
##### Clone the repository:
- git clone https://github.com/<username>/twitter-data-scraper.git
##### Install the required Python libraries:
- pip install -r requirements.txt

## Usage

##### Start a MongoDB server:
- mongod

##### Run the app.py script:
- streamlit run app.py
- In the web app, enter a keyword or hashtag to search for, the start and end dates of the date range to search within, and the maximum number of tweets to scrape. Click the "Scrape and Download Twitter Data" button to start the scraping process.
- Once the scraping is complete, the scraped data will be displayed in a table. You can download the scraped data in CSV or JSON format by clicking the respective download button.

##### Acknowledgments
- snscrape - A Python package for scraping social media websites
- MongoDB - A NoSQL database
- Streamlit - A Python library for creating web apps

## Workflow
- Clone the repository to your local machine.
- Install the required Python libraries by running pip install -r requirements.txt.
- Start a MongoDB server by running mongod.
- Run the app.py script using streamlit run app.py.
- In the web app, enter a keyword or hashtag to search for, the start and end dates of the date range to search within, and the maximum number of tweets to scrape.
Click the "Scrape and Download Twitter Data" button to start the scraping process.
- Once the scraping is complete, the scraped data will be displayed in a table.
Download the scraped data in CSV or JSON format by clicking the respective download button.
