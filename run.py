from markov_python.cc_markov import MarkovChain
from bs4 import BeautifulSoup
import urllib2

def webpage_upload_processing(a_markov_chain):
	url_to_parse = raw_input("Please input the url that you wish to parse: ")
	webpage_data = urllib2.urlopen(url_to_parse)
	webpage_parser = BeautifulSoup(webpage_data.read(), "html5lib")
	for tag in webpage_parser.find_all(True):
		if tag.string is not None:
			a_markov_chain.add_string(tag.string)
	print("The website has been parsed and processed.")
	
def file_upload_processing(a_markov_chain):
	file_path=raw_input("What is the file path that you want to open: ")
	a_markov_chain.add_file(file_path)
	print("The file has been parsed and processed.")

print("This program is a practice lesson in utilizing different modules"\
				 +" and letting them work in a constructive fashion.")
print("This program shall first utilize the instruction file for" \
		 + " the markov chains to first parse experimentally to see what" \
		 + " what happens.")

my_markov_chain = MarkovChain()
#put in all the markov chain commands for files and then work on webpages

while(True):
	menu_selection=raw_input("What do you want to do with the Markov Chain"\
				+"\n (r)eset, (a)dd to, or (g)enerate: ")
				
	if( menu_selection == 'r' ):
		
		key_word_initializer=int(raw_input("How many keywords would you like"\
			+ "use when reinitializing the Markov Chain: "))
		if(key_word_initializer == 0):
			my_markov_chain = MarkovChain()
		else:
			my_markov_chain = MarkovChain(key_word_initializer)
		print("The Markov Chain has now been reset.")
		
	elif( menu_selection == 'a' ):
		
		input_processing_selection=raw_input("Do you want to add a (w)ebpage"\
			+ " or a (f)ile: ")
		if(input_processing_selection == 'w'):
			webpage_upload_processing(my_markov_chain)
		elif(input_processing_selection == 'f'):
			file_upload_processing(my_markov_chain)
				
	elif( menu_selection == 'g'):
		
		markov_length=int(raw_input("How many words to you want the markov"\
				+ " chain to be.  Default is 20: "))
		if(markov_length > 0):
			markov_output=my_markov_chain.generate_text(markov_length)
		else:
			markov_output=my_markov_chain.generate_text()
		print(markov_output)
		
	program_exit=raw_input("Do you want to e(x)it or (r)epeat: ")
	if(program_exit == 'x'):
		break
