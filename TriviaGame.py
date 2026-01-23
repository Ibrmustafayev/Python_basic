import random

questions = {
    "What is the capital of France?": "Paris",
    "How many continents are there on Earth?": "7",
    "Which planet is known as the Red Planet?": "Mars",
    "What is the largest ocean on Earth?": "Pacific Ocean",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What gas do plants absorb from the air?": "Carbon dioxide",
    "What is H₂O commonly known as?": "Water",
    "How many bones are in the human body (adult)?": "206",
    "What part of the cell contains DNA?": "Nucleus",
    "What force keeps us on the ground?": "Gravity",
    "Which country has the largest population in the world?": "India",
    "What is the longest river in the world?": "Nile",
    "Which desert is the largest hot desert?": "Sahara",
    "Mount Everest is located in which mountain range?": "Himalayas",
    "Which country is famous for the Great Wall?": "China",
    "Which movie features a character named Jack Sparrow?": "Pirates of the Caribbean",
    "What is the name of the wizard school in Harry Potter?": "Hogwarts",
    "Which movie series has lightsabers?": "Star Wars",
    "Who is the superhero known as Iron Man?": "Tony Stark",
    "Which animated movie features a snowman named Olaf?": "Frozen",
    "What does CPU stand for?": "Central Processing Unit",
    "Which programming language is known for its snake logo?": "Python",
    "What does WWW stand for?": "World Wide Web",
    "Who founded Microsoft?": "Bill Gates",
    "What device is used to move the cursor on a computer?": "Mouse",
    "How many players are on a football team on the field?": "11",
    "Which sport uses a bat and a ball and has bases?": "Baseball",
    "In which sport would you perform a slam dunk?": "Basketball",
    "Which country hosted the 2016 Summer Olympics?": "Brazil",
    "What color card means a player is sent off in football?": "Red",
    "What has keys but can’t open locks?": "Piano",
    "What comes after Friday?": "Saturday",
    "How many days are in a leap year?": "366",
    "What is 9 x 9?": "81",
    "What is the opposite of cold?": "Hot"
}

def trivia_game():
    questions_list=list(questions.keys())
    total_questions,score=10,0
    selected_questions=random.sample(questions_list,total_questions)
    for idx, question in enumerate(selected_questions):
        print(f"{idx+1}. {question}")
        user_answer=input("Your answer: ").lower().strip()
        correct_answer=questions[question]
        if user_answer==correct_answer.lower():
            print("Correct\n")
            score+=1
        else:
            print(f"Wrong. The correct answer is {correct_answer}.\n")
    print(f"Game over! Your final score is {score}/{total_questions}.")

trivia_game()