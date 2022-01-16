def menu():
  import random
  from availableQuestions import availableQuestions

  storedQuestions = [["When did Nixon become president?", "1969"], ["How many wives did Henry VIII have?", "6"], ["How big was Henry VIII's privy council?", "12 members"], ]

  q1 = availableQuestions("When did Nixon become president?", "1969")
  #q2 = availableQuestions("How many wives did Henry VIII have?", "6")
  #q3 = availableQuestions("How big was Henry VIII's privy council?", "12 members")

  #testing question and answers can be displayed
  print(q1.question, q1.answer)

  def menuChoice():
    return input("Press 1")

  viewed = [""] 
  length = len(storedQuestions) 
  sessionFinish = False

  i = 0 

  while menuChoice != "end" or "End":
    menuChoice()
    if menuChoice() == "1":
      if sessionFinish == "True":
        storedQuestions = viewed
        print(storedQuestions)
      else:
        while storedQuestions != []: 
          randomQuestion = random.randint(0,(length-1))
          viewed = viewed.update(storedQuestions[randomQuestion])
          print(storedQuestions[randomQuestion][0]) 
          answer = input("Please input the answer ")
          if answer == storedQuestions[randomQuestion][1]:
            print("Correct well done.")  
            del storedQuestions[randomQuestion]
            length = length-1
            if storedQuestions == []:
              sessionFinish = "True"
              print("Done")
          else:
            print("Incorrect the answer was " + storedQuestions[randomQuestion][1])
          i = length - 1
    elif menuChoice() == "2":
      print(storedQuestions)
      
    # hello world

  
