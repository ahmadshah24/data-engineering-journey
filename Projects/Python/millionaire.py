questions = [
    ["who is the president of the united states?", "joe biden", "donald trump", "barack obama", "george w bush", 2],
    ["what is the capital of United states?", 'Pari','london','Washigton DC','Kabul',3],
    ["what is the largest planet in our solar system?", 'Earth','Mars','Jupiter','Saturn',3],
    ["what is the smallest country in the world?", 'Vatican City','Monaco','Nauru','Tuvalu',1],
    ["what is the highest mountain in the world?", 'Mount Everest','K2','Kangchenjunga','Lhotse',1],
    ["what is the largest ocean in the world?", 'Atlantic Ocean','Indian Ocean','Arctic Ocean','Pacific Ocean',4],
    ["what is the longest river in the world?", 'Nile River','Amazon River','Yangtze River','Mississippi River',1],
    ["what is the largest desert in the world?", 'Sahara Desert','Gobi Desert','Kalahari Desert','Arabian Desert',1],
    ["what is the most populous country in the world?", 'China','India','United States','Indonesia',1],
    ["what is the largest mammal in the world?", 'Blue Whale','Elephant','Giraffe','Hippopotamus',1]
]

prizes = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
score = 0
sum = 0
i = 0
for question in questions:
    print(question[0])
    print("1.", question[1])
    print("2.", question[2])
    print("3.", question[3])
    print("4.", question[4])
    answer = int(input("Enter your answer (1-4): \n"))
    if answer == question[5]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is:", question[question[5]])
        break
    print("you won $", prizes[i])
    i+=1
    sum += prizes[i]

print("Your final score is:", score)
print("Your total winnings are: $", sum)
