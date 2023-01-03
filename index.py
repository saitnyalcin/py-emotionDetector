import matplotlib.pyplot as plt
import matplotlib
from textblob import TextBlob

def set_text_color(text):
    # Perform sentiment analysis
    sentiment = TextBlob(text).sentiment.polarity

    # Normalize sentiment to a value between 0 and 1
    norm_sentiment = (sentiment + 1) / 2

    # Create a color map with red for negative sentiment, green for positive sentiment
    cmap = plt.get_cmap('RdYlGn')

    # Use the color map to get the text color based on the normalized sentiment
    text_color = cmap(norm_sentiment)

    # Convert the color to a hex code
    text_color = matplotlib.colors.to_hex(text_color)

    return text_color

text = "I am feeling amazing ever today!"
color = set_text_color(text)
print(f"Text color: {color}")