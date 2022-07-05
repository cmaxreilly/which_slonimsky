#The purpose of this program is to randomly select an exercise from Slonimsky's thesaurus for daily practice.

#Step 1: Establish a list with a range from the thesaurus. (1, 1330)

thesaurus_exercises = list(range(1,1331))

#test of list

#print(thesaurus_exercises)

#Success!

#Step 2: Select a random number from thesaurus_exercises.

import random

random_exercise = random.choice(thesaurus_exercises)

#Step 3: Print random excercise number.

print(random_exercise)

#Step 4: Alias this python script to which_slonimsky in ~/.bash_aliases.

#Success! I will probably reuse this program many times, so I am glad about the documentation. I will have to 
#do more documentation like this in the future.