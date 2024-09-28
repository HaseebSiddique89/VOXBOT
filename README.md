# VOXBOT
 This project is a Flask-based chatbot using AIML, Neo4j, and AI techniques like spell checking, named entity recognition, and sentiment analysis. It stores user interactions, builds relationships between entities, and responds to queries. The bot fetches info from Wikipedia, provides word synonyms, and uses logic-based reasoning for answers.

## Flask Setup and Routes
- The chatbot is built as a web application using the Flask framework.
- •	The Flask application sets up routes to handle different user interactions.
- Routes include:
    - Home page ("/"): Displays the landing page of the chatbot.
    - User signup ("/signup"): Handles user registration.
    - User login ("/signin"): Manages user authentication.
    - Chat ("/chat"): Renders the chat interface for user interactions.

## User Signup and Login
- The chatbot allows users to create accounts and log in.
- The user signup functionality enables users to register by providing a username, email, and password.
- The chatbot verifies the uniqueness of the provided email address.
- If the email is unique, a new user node is created in the Neo4j graph database, and the user is redirected to the chat interface.
- If the email already exists, an error message is displayed.
- The user login functionality validates the provided email and password against the database for authentication.

![Signup Page](https://github.com/HaseebSiddique89/VOXBOT/blob/main/images/Picture1.jpg)

![Login Page](https://github.com/HaseebSiddique89/VOXBOT/blob/main/images/Picture2.jpg)

## Chat Interface
- The chat interface provides a user-friendly environment for users to interact with the chatbot.
- Users can enter queries, messages, or commands in the chat interface.
- The chatbot processes the input and generates appropriate responses based on theimplemented functionalities.

![Chat Interface](https://github.com/HaseebSiddique89/VOXBOT/blob/main/images/Picture3.jpg)

## AIML Initialization
- The chatbot utilizes AIML (Artificial Intelligence Markup Language) for natural language processing and conversation management.
- AIML files are loaded into an AIML Kernel object (k) to enable the chatbot to understand and respond to user inputs.
- The chatbot learns from AIML files located in a specified directory to enhance its conversational abilities.

## Knowledge Base (Pytholog)
- The chatbot incorporates a Pytholog Knowledge Base to manage family relationship-related facts and queries.
- Initial knowledge base rules are defined to handle family relationships, including rules for fathers, mothers, and children.
- The knowledge base is loaded with these initial rules to provide accurate responses to family relationship-related queries.

## Spell Checking
- To enhance user experience and understandability, the chatbot performs spell checking on user inputs.
- A custom module is used for spell checking, ensuring that user queries are correctly interpreted and processed.

![Spell Checking](https://github.com/HaseebSiddique89/VOXBOT/blob/main/images/Picture4.jpg)

## Named Entity Recognition (NER)
- The chatbot employs Named Entity Recognition (NER) to identify entities in user queries.
- Entities such as names of persons are recognized and stored as nodes in the Neo4j graph database.
- This information enriches the chatbot's knowledge and enables it to provide more personalized responses.

## Sentiment Analysis
- The chatbot performs sentiment analysis on user queries using the Natural Language Toolkit (NLTK).
- By analyzing the sentiment of the user's input, the chatbot can adapt its responses accordingly.
- If the sentiment is negative, the chatbot generates appropriate responses to address the user's concerns or frustrations.

![Sentiment Analysis](https://github.com/HaseebSiddique89/VOXBOT/blob/main/images/Picture5.jpg)

## Web Scraping
- If the chatbot has no response, it scrapes Wikipedia for information.

![Web Scrape](https://github.com/HaseebSiddique89/VOXBOT/blob/main/images/Picture6.jpg)

## Handling User Queries and AIML Responses
- User queries are passed to the AIML Kernel object (k) to generate responses.
- The chatbot analyzes the AIML response and checks for cases where the response is "unknown".
- In such cases, the chatbot performs web scraping by searching Wikipedia for relevant information to provide an appropriate response.

## Pytholog Knowledge Base Manipulation
- The chatbot interacts with the Pytholog knowledge base to manage family relationship-related facts and queries.
- Functions are implemented to set new facts (e.g., adding a new parent-child relationship) and query existing facts (e.g., finding a person's father or mother).
- The chatbot updates the Neo4j graph database to reflect the new facts and relationships.

![Knowledge Base Answer](https://github.com/HaseebSiddique89/VOXBOT/blob/main/images/Picture7.jpg)

## Machine Learning
- I have implemented machine learning which predicts the gender of the persons which is further used in makin relationships using prolog.
- Using SVM model.

## Neo4j
- All the data is being stored in graphical database (Neo4j) including persons relations etc.

![Neo4j Graph](https://github.com/HaseebSiddique89/VOXBOT/blob/main/images/Picture8.jpg)

## WordNet Integration
- The chatbot integrates with WordNet, a lexical database, to provide synonyms and antonyms of words.
- Users can request synonyms and antonyms by providing a word as a command.
- The chatbot retrieves the corresponding synonyms and antonyms from WordNet and presents them as part of its response.

![Wordnet](https://github.com/HaseebSiddique89/VOXBOT/blob/main/images/Picture9.jpg)

## Text-to-Speech
- I have implemented text to speech functionality which allows the user to press the voice button and can hear the bot’s response voice.

---

# Technologies Under Process
- Episodic Memory
- Human-like typing responses
