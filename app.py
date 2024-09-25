from flask import Flask, render_template, request, redirect, url_for
import os 
from aiml import Kernel
from py2neo import Graph, Node, Relationship
from spelling import correct_spelling
from nltk_part import named_entity_recognition, perform_sentiment_analysis
from webscrap import search_wikipedia
from glob import glob
import random
import training_data
import pytholog
from svm import svc
from wordnet import get_synonyms, get_antonyms

graph = Graph("bolt://localhost:7687", auth=("neo4j", "12345678"))
app = Flask(__name__)

k = Kernel()

aiml_files = glob('C:/Users/MUHAMMAD HASEEB/Documents/CHATBOT/Easy-Chatbot-master/data/*.aiml')
for file_path in aiml_files:
    k.learn(file_path)


# BRAIN_FILE="C:\\Users\\MUHAMMAD HASEEB\\Documents\\CHATBOT\\Easy-Chatbot-master\\pretrained_model\\aiml_pretrained_model.dump"
# print(BRAIN_FILE)

# if os.path.exists(BRAIN_FILE):
#     print("Loading from brain file")
#     k.loadBrain(BRAIN_FILE)
# else:
#     print("Parsing aiml files")
#     k.bootstrap(learnFiles="./pretrained_model/learningFileList.aiml", commands="load aiml")
#     print("Saving brain file: " + BRAIN_FILE)
#     k.saveBrain(BRAIN_FILE)


@app.route('/')
def home():
    return render_template('LS.html')


@app.route('/signup', methods= ['POST', 'GET'])
def sigup():
    form_type = request.form.get('form_type')

    if form_type == 'signup':
        Susername = request.form.get('SUsername')
        Semail = request.form.get('SEmail')
        Spassword = request.form.get('SPassword')
        Scpassword = request.form.get('SCPassword')

        myemail = graph.run("""MATCH(n:PERSON {name:$usrname,email:$usremail,password:$usrpass}) return n.email"""
               , {'usrname':Susername,'usremail':Semail ,'usrpass':Spassword })
        
        if len(myemail.data()) == 0:
            graph.run("""MERGE(n:PERSON {name:$usrname,email:$usremail,password:$usrpass})"""
              , {'usrname':Susername , 'usremail':Semail ,'usrpass':Spassword })
            return redirect(url_for('chat'))   
        else:
            return ('Already have an account on this email') 



@app.route('/signin', methods= ['POST', 'GET'])
def signin():
    form_type = request.form.get('form_type')
    if form_type == 'signin':
        Lemail = request.form.get('LEmail')
        Lpassword = request.form.get('LPassword')

        myemail = graph.run("""MATCH(n:PERSON {email:$usremail,password:$usrpass}) return n.email"""
               , {'usremail':Lemail ,'usrpass':Lpassword })
        if len(myemail.data()) == 0:
            return ('Dont have an account')
        else:
            return redirect(url_for('chat'))




@app.route('/chat')
def chat():
    return render_template('chat.html')

# ================================= Pytholog ======================================================

knowledge_base = pytholog.KnowledgeBase('KB')
knowledge = [
    'father(X, Y):- male(X), parent(X, Y)',
    'mother(X, Y):- female(X), parent(X, Y)',
    'child(X, Y):- parent(Y, X)'
]
knowledge_base(knowledge)

print('_'*60)
# resetting predicates
# k.respond('RESET QUESTIONS')
# k.respond('RESET FACTS')
k.setPredicate('male','unknown')
k.setPredicate('female','unknown')
k.setPredicate('parent','unknown')
k.setPredicate('child','unknown')
k.setPredicate('fatherof','unknown')
k.setPredicate('motherof','unknown')
k.setPredicate('childof','unknown')

def set_fact(fact, value, value2='default'):
    print('value2: ', value2)
    if value2 != 'default' :

        name1 = svc(value)
        name2 = svc(value2)

        if name1 == 0:
            new_fact = 'male' + '(' + value.lower() + ')'
            knowledge.insert(0, new_fact)
            knowledge_base(knowledge)

        elif name1 == 1:
            new_fact = 'female' + '(' + value.lower() + ')'
            knowledge.insert(0, new_fact)
            knowledge_base(knowledge)

        if name2 == 0:
            new_fact = 'male' + '(' + value.lower() + ')'
            knowledge.insert(0, new_fact)
            knowledge_base(knowledge)

        elif name2 == 1:
            new_fact = 'female' + '(' + value.lower() + ')'
            knowledge.insert(0, new_fact)
            knowledge_base(knowledge)

        new_fact = fact + '(' + value.lower() + ',' + value2.lower() + ')'

        print('in facts')
        
        graph.run("""MERGE(n:PERSON {name: $usrname}) MERGE(n2:PERSON {name: $usr2name}) MERGE (n)-[r:PARENT]->(n2)""",
           {'usrname': value, 'usr2name': value2})
        
    else:
        print('in facts else')
        new_fact = fact + '(' + value.lower() + ')'

        graph.run("""MERGE(n:PERSON {name:$usrname})"""
              , {'usrname':value})

    knowledge.insert(0, new_fact)
    knowledge_base(knowledge)
    
    # k.respond('RESET FACTS')
    print('resetting')
    k.setPredicate('male','unknown')
    k.setPredicate('female','unknown')
    k.setPredicate('parent','unknown')
    k.setPredicate('child','unknown')


def query_kb(fact, value):
    
    # k.respond('RESET QUESTIONS')
    k.setPredicate('fatherof','unknown')
    k.setPredicate('motherof','unknown')
    k.setPredicate('childof','unknown')

    query = fact + '(X, ' + value.lower().strip() + ')'
    result = knowledge_base.query(pytholog.Expr(query))
    
    if result[0] is str:
        return None
    else:
        rs = []
        for value in result:
            rs.append(value['X'].title().replace('_', ' '))
        rs = list(set(rs))
        rs = ", ".join(rs)
        return rs


# function to check predicates
def check_predicates():
    male = k.getPredicate('male')
    female = k.getPredicate('female')
    parent = k.getPredicate('parent')
    child = k.getPredicate('child')
    father_of = k.getPredicate('fatherof')
    mother_of = k.getPredicate('motherof')
    child_of = k.getPredicate('childof')

    print('male', male)
    print('female', female)
    print('parent', parent)
    print('child', child)
    print('father', father_of)
    print('mother', mother_of)
    print('child', child_of)


    result = None

    if male != 'unknown':
        set_fact('male', male)
    if female != 'unknown':
        set_fact('female', female)
    if parent != 'unknown':
        set_fact('parent', parent, child)
    if father_of != 'unknown':
        result = query_kb('father', father_of)
    if mother_of != 'unknown':
        result = query_kb('mother', mother_of)
    if child_of != 'unknown':
        result = query_kb('child', child_of)


    print('========================')
    print('male', male)
    print('female', female)
    print('parent', parent)
    print('child', child)
    print('father', father_of)
    print('mother', mother_of)
    print('child', child_of)



    return result


# =======================================================================================


k.setBotPredicate('name', 'VoxBot')

@app.route('/get', methods=['POST', 'GET'])
def get_bot_response():
    # getting query from the user
    query = request.args.get('msg')

    # Spell Checking
    question = correct_spelling(query)

    # NER 
    question = question.title()
    entities = named_entity_recognition(question)
    print('entities', entities)
    for entity, label in entities:
        if label == 'PERSON':
            graph.run("""MERGE(n:PERSON {name:$usrname})"""
               , {'usrname':entity})
     
    # Sentiment Analysis
    result = perform_sentiment_analysis(question)
    if result['compound'] < 0:
        print('sentiment')
        response = random.choice(training_data.negative_responses)
        return (str(response))
    
    else:
        # Making Relations
        response = k.respond(question)
        pr = check_predicates()
        if pr:
            response = pr
            return (str(response))

        
    response = k.respond(question)    
    
    # Web Scraping
    if response == 'unknown': 
        response = search_wikipedia(question)
    
    # WORDNET
    if response == 'word':    
        word = k.getPredicate('search')
        synonyms = get_synonyms(word)
        antonyms = get_antonyms(word)    

        s = ", ".join(synonyms)
        a = ", ".join(antonyms)

        print('word: ', word)
        print('s', s)
        print('a', a)

        response = "Synonyms of ", word + ": "+ s + "and the Antonyms of" , word + ": ", a
        

    response_text = str(response)
    
    # if response_text:
    #     return render_template('chat.html', botResponse=response_text)
    # else:
    #     return render_template('chat.html', botResponse=':)')

    if response:
        return (str(response))
    else:
        return (str(":)"))
    

if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0', port='5000')

