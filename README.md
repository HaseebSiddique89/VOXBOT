# VOXBOT
 This project is a Flask-based chatbot using AIML, Neo4j, and AI techniques like spell checking, named entity recognition, and sentiment analysis. It stores user interactions, builds relationships between entities, and responds to queries. The bot fetches info from Wikipedia, provides word synonyms, and uses logic-based reasoning for answers.

## Flask Setup and Routes
- The chatbot is built as a web application using the Flask framework.
- Routes include:
    - Home page ("/"): Displays the landing page of the chatbot.
    - User signup ("/signup"): Handles user registration.
    - User login ("/signin"): Manages user authentication.
    - Chat ("/chat"): Renders the chat interface for user interactions.

## User Signup and Login
- The chatbot allows users to create accounts and log in.
- The chatbot verifies the uniqueness of the email address using Neo4j.
- Successful signup redirects users to the chat interface.

## Chat Interface
- Provides a user-friendly environment for interacting with the chatbot.

## AIML Initialization
- Uses AIML for natural language processing and conversation management.

## Knowledge Base (Pytholog)
- Manages family relationship facts using Prolog-based logic.

## Spell Checking
- Custom module for spell checking user inputs.

## Named Entity Recognition (NER)
- Identifies entities such as names and stores them in Neo4j for personalized responses.

## Sentiment Analysis
- Uses NLTK for sentiment analysis and adapts responses based on user sentiment.

## Web Scraping
- If the chatbot has no response, it scrapes Wikipedia for information.

## Machine Learning
- Implements gender prediction using SVM for family relationship handling.

## Neo4j
- All data is stored in a Neo4j graph database.

## WordNet Integration
- Provides synonyms and antonyms from WordNet.

## Text-to-Speech
- Allows users to hear the bot’s responses using text-to-speech functionality.

---

# Technologies Under Process
- Episodic Memory
- Human-like typing responses
- OpenAI integration
