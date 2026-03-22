# Sentiment-Based Movie Rating System
# Install dependency first: pip install textblob

from textblob import TextBlob

def analyze_sentiment(review):
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Convert polarity (-1 to +1) into rating (0 to 5)
    rating = round((polarity + 1) * 2.5, 2)

    return sentiment, rating


def main():
    print("=== Sentiment-Based Movie Rating System ===")
    
    review = input("Enter movie review: ")

    sentiment, rating = analyze_sentiment(review)

    print("\nResult:")
    print("Sentiment:", sentiment)
    print("Rating:", rating, "/5")


if __name__ == "__main__":
    main()
