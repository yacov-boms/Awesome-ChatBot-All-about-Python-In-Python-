import sys
sys.path.append("C:/Python39/Lib/site-packages")

import pywebio
print(pywebio.__version__)
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *

import spacy
nlp = spacy.load("en_core_web_lg", disable=['ner'])
import re
import random

# Read article
f=open("C:/Users/kobi/ChatTest/PythonLang.txt",'r',errors = 'ignore')
raw=f.read()                            # string
f.close()

# Clean text
raw = re.sub("[\[].*?[\]]", "", raw)    # Drop Citations

def clean_sent(sent):
    clean_sent = [w.lemma_ for w in sent if (w.is_stop==False and not w.is_punct)]
    return nlp(' '.join(clean_sent))

text_doc = nlp(raw)
text_clean_docs = [clean_sent(sent) for sent in text_doc.sents]

# Handle Greetings
GREETING_INPUTS = ("hello", "hi", "greetings", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "Glad to talk to you"]
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Main Procedure
def respond():
    put_image(open('pythonJpg.jpg', 'rb').read(), width='10%', height='10%')
    put_markdown('## Awesome ChatBot - All about Python - In Python!')
    user_name = input('Please enter your name:', type=TEXT, required=True)
    put_html('scroll-behavior: smooth')
    while True:
        user_text = input('Hi ' + user_name +', Please enter your query (type "bye" to checkout):',required=True, type = TEXT,
               placeholder='Example: What kind of programming language is python?')
        if(user_text=='thanks' or user_text =='thank you' ):# Thanks
            answer = 'You are welcome.. ' + user_name
        elif user_text == 'bye':
            answer = 'Bye Bye'+' '+ user_name
        elif(greeting(user_text)!=None):                  # Greetings
            answer = greeting(user_text)
        else:
            query_doc = nlp(user_text)
            query_clean_doc = clean_sent(query_doc)
            sims = [query_clean_doc.similarity(text_clean_doc) for text_clean_doc in text_clean_docs]
            #print('------------------ sims: ', sims)
            idx = sims.index(max(sims))
            answer = list(text_doc.sents)[idx]
        
        put_table([
            [put_row([put_text(user_name + ' : '), put_text(user_text)],size='75px 740px')],
            [put_row([put_text('Answer : '), put_text(str(answer))],size='75px 740px')]
            ])
        if user_text == 'bye':
            break


if __name__ == '__main__':
    print('----------- starting main  --------------')
    start_server(respond, port=80, debug=True)

