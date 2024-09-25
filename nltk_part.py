import nltk

# NER using NLTK
def named_entity_recognition(text):
    tokens = nltk.word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)
    ne_tree = nltk.ne_chunk(tagged_tokens)
    
    named_entities = []
    for subtree in ne_tree:
        if hasattr(subtree, 'label'):
            entity = ' '.join(c[0] for c in subtree.leaves())
            label = subtree.label()
            named_entities.append((entity, label))
    
    return named_entities


# =============================================================================
# import random
from nltk.sentiment import SentimentIntensityAnalyzer
# import training_data

# Sentiment analysis
def perform_sentiment_analysis(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)
    return sentiment_scores

# Example usage
# while True:
#     text = input('ENTER: ', )
#     sentiment_scores = perform_sentiment_analysis(text)
#     print("Sentiment scores:", sentiment_scores)
#     if sentiment_scores['compound'] > 0:
#         print(random.choice(training_data.positive_responses))
#     elif sentiment_scores['compound'] == 0:
#         print(random.choice(training_data.neutral_responses))
#     elif sentiment_scores['compound'] < 0:
#         print(random.choice(training_data.negative_responses))



# ====================================================================================
