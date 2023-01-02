from textblob import TextBlob

def detect_feelings(text):
   # Create a TextBlob object from the input text
    blob = TextBlob(text)

    # Calculate the sentiment of the text
    sentiment = blob.sentiment

    # Extract the polarity and subjectivity scores
    polarity = sentiment.polarity
    subjectivity = sentiment.subjectivity

    # Determine the overall sentiment of the text
    if polarity > 0:
        return "positive"
    elif polarity == 0:
        return "neutral"
    else:
        return "negative"

# Test the function with some example input
text = "i do not want to do anything today"
feelings = detect_feelings(text)
print(feelings)  # Output: "positive"

text = "I am feeling very sad today"
feelings = detect_feelings(text)
print(feelings)  # Output: "negative"