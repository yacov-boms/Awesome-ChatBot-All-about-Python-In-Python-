# Chat3  
A Q&A chatbot to provide general information abou Python programming language. 
This chatbot is for human language messaging  interaction.   
The heart of the chatbot is a **Python program with spacy package** residing (currently) on a local computer.  
It is also comprised of:  
*	_PyWebIo_ - An advanced python package that initiates local web server which operates a specific python function and listens to messages on an alocated port. 
*	_Ngrok_ - A safe https connection from the local web server to Facebook Messenger.
*	Can be approached from any autorized browser.

## Chatbot Functionality:  
**At startup:**  
*	**loads model en_core_web_lg** 
* Reads a text file taken from wikipedia with some tweaking.
*	applies NLP function to create a semantic doc object
*	Does cleaning and lemmatazaion

**In response to a users query:**  
*	Possible basic rule based greetings
*	Creates a semantic query object
*	**Checks cosine similarity** between the query and each of the file's sentences  
  based on the **English large model semantics.**
*	Picks the best similar sentence and sends it to the user

**Innovation:**  
**Use of PyWebIo, an advanced package that handles automatically server construcion and opeations.**
**The package saves the need to directly address server issues and thereby facilitates development, 
  optimizes and accelerates it.**  
