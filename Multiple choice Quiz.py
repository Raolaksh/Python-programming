from Question import question

question_prompt = [
    "who is the son of minato namekaze?\n(a) sasuke\n(b) naruto\n(c) kakashi\n\n",
    "who is the yellow flash of the hidden leaf?\n(a) Tsunade\n(b) orochimaru\n (c) minato\n\n",
    "who is the ultimate defence of sand village?\n(a) sukaku\n(b) their army\n(c) gara\n\n"
]

question = [
    question(question_prompt[0], "b"),
    question(question_prompt[1], "c"),
    question(question_prompt[2], "c"),
]

def run_test(questions):
     score = 0
     for question in questions:
         answer = input(question.prompt)
         if answer == question.answer:
             score += 1
     print("you got " + str(score + "/" + str(len(questions)) + " correct")

run_test(questions)
