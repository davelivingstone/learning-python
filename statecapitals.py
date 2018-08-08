''' Jessica McKellar's code. I just typed what I saw in her lecture. It
was initially in Python 2.x, but I worked on it and "ported" it (can I
actually say that?) to Python 3. I had an annoying error after I simply
changed print to print() and raw_input to input, namely
TypeError: 'dict_keys' object does not support indexing. I thought for a
bit and decided to change states = capitals_dict.keys() to
states = list(capitals_dict.keys()), because dict.keys always appeared
before the list created out of the keys in the dictionary (it created an iterator). 
I figured, OK, it looks a bit redundant, turning a list into a list, but it worked.
I also changed for i in [1, 2, 3, 4, 5] to for i in range(6), and I think
I'd even want more than that, 10-12 questions would make things a little
more interesting.
I also added a counter for right answers and to print different messages,
depending on the number of right answers.
To top it all off, I decided to change the rather old string formatting
and I used f-strings to format a few strings, such as the string after
the else statement that tells you if you entered a wrong answer.
Furthermore, I created number_of_questions = list(range(6)), so I can use
this elsewhere through the program and not have to change the number
everywhere, if and when I decide to have less or more questions. Of course,
I also changed "if counter == 6" to "if counter == len(number_of_questions),"
and now I only need to change the number in the first variable.'''

capitals_dict = {'Alabama': 'Montgomery',
                'Alaska': 'Juneau',
                'Arizona': 'Phoenix',
                'Arkansas': 'Little Rock',
                'California': 'Sacramento',
                'Colorado': 'Denver',
                'Connecticut': 'Hartford',
                'Delaware': 'Dover',
                'Florida': 'Tallahassee',
                'Georgia': 'Atlanta',
                'Hawaii': 'Honolulu',
                'Idaho': 'Boise',
                'Illinois': 'Springfield',
                'Indiana': 'Indianapolis',
                'Iowa': 'Des Moines',
                'Kansas': 'Topeka',
                'Kentucky': 'Frankfort',
                'Louisiana': 'Baton Rouge',
                'Maine': 'Augusta',
                'Maryland': 'Annapolis',
                'Massachusetts': 'Boston',
                'Michigan': 'Lansing',
                'Minnesota': 'Saint Paul',
                'Mississippi': 'Jackson',
                'Missouri': 'Jefferson City',
                'Montana': 'Helena',
                'Nebraska': 'Lincoln',
                'Nevada': 'Carson City',
                'New Hampshire': 'Concord',
                'New Jersey': 'Trenton',
                'New Mexico': 'Santa Fe',
                'New York': 'Albany',
                'North Carolina': 'Raleigh',
                'North Dakota': 'Bismarck',
                'Ohio': 'Columbus',
                'Oklahoma': 'Oklahoma City',
                'Oregon': 'Salem',
                'Pennsylvania': 'Harrisburg',
                'Rhode Island': 'Providence',
                'South Carolina': 'Columbia',
                'South Dakota': 'Pierre',
                'Tennessee': 'Nashville',
                'Texas': 'Austin',
                'Utah': 'Salt Lake City',
                'Vermont': 'Montpelier',
                'Virginia': 'Richmond',
                'Washington': 'Olympia',
                'West Virginia': 'Charleston',
                'Wisconsin': 'Madison',
                'Wyoming': 'Cheyenne'
                }

import random

states = list(capitals_dict.keys())
counter = 0
number_of_questions = list(range(6))

for i in number_of_questions:
    state = random.choice(states)
    capital = capitals_dict[state]
    capital_guess = input(f"What is the capital of {state}?\n")

    if capital_guess == capital:
        print("Correct! Nice job.")
        counter += 1
    else:
        print(f"Incorrect. The capital of {state} is {capital}.")

print("All done.")

if counter == len(number_of_questions):
    print("Wow, you got all of them, you should be on Jeopardy.")
elif counter < 3:
    print(f"Geography class was a long time ago, eh? You got just {counter} out of {len(number_of_questions)}.")
else:
    print(f"You got {counter} out of {len(number_of_questions)}, not too shabby.")


'''This is the original code that I saw in Jessica McKellar's tutorial
and I wrote verbatim:

capitals_dict = {'Alabama': 'Montgomery',
				'Alaska': 'Juneau',
				'Arizona': 'Phoenix',
				'Arkansas': 'Little Rock',
				'California': 'Sacramento',
				'Colorado': 'Denver',
				'Connecticut': 'Hartford',
				'Delaware': 'Dover',
				'Florida': 'Tallahassee',
				'Georgia': 'Atlanta',
				'Hawaii': 'Honolulu',
				'Idaho': 'Boise',
				'Illinois': 'Springfield',
				'Indiana': 'Indianapolis',
				'Iowa': 'Des Moines',
				'Kansas': 'Topeka',
				'Kentucky': 'Frankfort',
				'Louisiana': 'Baton Rouge',
				'Maine': 'Augusta',
				'Maryland': 'Annapolis',
				'Massachusetts': 'Boston',
				'Michigan': 'Lansing',
				'Minnesota': 'Saint Paul',
				'Mississippi': 'Jackson',
				'Missouri': 'Jefferson City',
				'Montana': 'Helena',
				'Nebraska': 'Lincoln',
				'Nevada': 'Carson City',
				'New Hampshire': 'Concord',
				'New Jersey': 'Trenton',
				'New Mexico': 'Santa Fe',
				'New York': 'Albany',
				'North Carolina': 'Raleigh',
				'North Dakota': 'Bismarck',
				'Ohio': 'Columbus',
				'Oklahoma': 'Oklahoma City',
				'Oregon': 'Salem',
				'Pennsylvania': 'Harrisburg',
				'Rhode Island': 'Providence',
				'South Carolina': 'Columbia',
				'South Dakota': 'Pierre',
				'Tennessee': 'Nashville',
				'Texas': 'Austin',
				'Utah': 'Salt Lake City',
				'Vermont': 'Montpelier',
				'Virginia': 'Richmond',
				'Washington': 'Olympia',
				'West Virginia': 'Charleston',
				'Wisconsin': 'Madison',
				'Wyoming': 'Cheyenne'
				}

import random

states = capitals_dict.keys()

for i in [1, 2, 3, 4, 5]:
	state = random.choice(states)
	capital = capitals_dict[state]
	capital_guess = raw_input("What is the capital of " + state + "?\n")

	if capital_guess == capital:
		print "Correct!. Nice job."
	else:
		print "Incorrect. The capital of " + state + " is " + capital + "."

print "All done."'''
