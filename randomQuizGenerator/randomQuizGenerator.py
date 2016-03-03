#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 
   'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
   'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
    # Create the quiz and answer key files.
    quizFile = open('capitalquiz%s.txt' % quizNum, 'w')
    answerFile = open('capitalquiz_answers%s.txt' % quizNum, 'w')
    quizFile.write(' ' * 15 + "Quiz Form %s\n" % quizNum)
    # Write out the header for the quiz.
    quizFile.write('Name:\nDate:')
    quizFile.write('\n\n') # two new lines.


    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # TODO: Loop through all 50 states, making a question for each.
    for questionNum in range(50):
      finalAnswersList = []
      currentState = states[questionNum]
      correctAnswer = capitals[currentState]
      finalAnswersList.append(correctAnswer)
      #gets a list of answers
      listOfAnswers = list(capitals.values())
      random.shuffle(listOfAnswers)
      # picks three wrong answers, and adds those to list of answers.
      # better to replace this code with random.sample
      while (len(finalAnswersList) < 4):
        stateIntToPick = random.randint(0, 49)
        wrongState = states[stateIntToPick]
        wrongAnswer = capitals[wrongState]
        if (wrongAnswer not in finalAnswersList):
          finalAnswersList.append(wrongAnswer)
      random.shuffle(finalAnswersList)
      # answerFile.write('%s. %s\n' % (questionNum, correctAnswer))
      # wanted the letter, not the name, which was done above.
      finalAnswerPos = finalAnswersList.index(correctAnswer)
      answerFile.write('%s. %s\n' % (questionNum, 'ABCD'[finalAnswerPos]))
      quizFile.write('%s. What is the capital of %s?' % (questionNum, currentState))
      quizFile.write('\n')
      for pos in range(4):
        quizFile.write('%s. %s' % ('ABCD'[pos], finalAnswersList[pos]) + ' ' * 3)
      quizFile.write('\n\n')









  

