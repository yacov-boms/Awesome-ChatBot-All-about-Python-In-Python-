# Chat3  
A Q&A chatbot to provide general information about Python programming language in "pure" Python. 
This chatbot is for human language messaging interaction from any browser. 
**It combines use of _Spacy_ NLP machine learning with innovative Python _PyWebIo_ package.**
The heart of the chatbot is a Python program with Spacy package residing (currently) on a local computer.  
It also uses _PyWebIo_ - A simple but advanced Python package that initiates local web server which operates a user Python function and listens to messages on a specific port. 

## Chatbot Functionality:  
**At startup:**  
*	**loads model en_core_web_lg** 
* Reads a text file taken from wikipedia with some tweaking.
*	Applies NLP function to create a semantic doc object
*	Does cleaning and lemmatazaion

**In response to a users query:**  
*	Possible basic rule based greetings
*	Creates a semantic query object
*	**Checks cosine similarity** between the query and each of the file's sentences  
  based on the **English large model semantics.**
*	Picks the best similar sentence and sends it to the user.  
In the attached demonstration we can see how Spacy detects similarity between morpholigically different words like 'highlight' and 'emphasizes', widespread' and 'popular', 'scaleable' and 'extensible'.

**Innovation:**  
**Use of PyWebIo, an advanced Python package that handles automatically server construcion and basic opeations including controls and styling.  
No need for explicit use of HTML, CSS or Java script.  
The package saves the need to directly address server issues and thereby facilitates development, 
optimizes and accelerates it.**  
