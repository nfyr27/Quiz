print("Добро пожаловать на викторину!")
print("Ответь на следующие вопросы:")

# Допиши код вместо "..."

questions = ["1. Какая звезда являйтся орентиром для моряка в северном полушарии?",
             "2. Официальное название самой высокой горы мира?",
             "3. Когда, до Петра I, праздновали Новый Год?",
             "4. Какое число является чёртовой дюжиной?(Напиши число)",
             "5. На чём произнёс свою знаменитую речь Владимир Ленин?",
             "6. В грамматике этой страны все существительные должны писаться с большой буквы. Назовине эту страну.",
             "7. Какой самый сложный язык в мире?"]

answers = ["Полярная", "Джамолумгма", "1 сентября", "13", "На броневике", "Германия", "Китайский"]

score = 0

print(questions[0])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[0].lower():
    print("Правильно!")
    score += 1

else:
    print("Неправильно.")

print(questions[1])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[1].lower():
    print("Правильно!")
    score += 1
else:
    print("Неправильно.")

print(questions[2])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[2].lower():
    print("Правильно!")
    score += 1
else:
    print("Неправильно.")

print(questions[3])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[3].lower():
    print("Правильно!")
    score += 1
else:
    print("Неправильно.")

print(questions[4])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[4].lower():
    print("Правильно!")
    score += 1
else:
    print("Неправильно.")

print(questions[5])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[5].lower():
    print("Правильно!")
    score += 1

else:
    print("Неправильно.")

print(questions[6])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[6].lower():
    print("Правильно!")
    score += 1
else:
    print("Неправильно.")

if score > 5:
    print("Это отличный результат! Видимо ты многое знаешь.")
elif score > 3:
    print("Неплохой результат!. Дальше будет ещё лучше.")
else:
    print("Видимо, ты только начинаешь свой путь к знаниям! Ты ещё много чего узнаешь о мире, где мы живём.")