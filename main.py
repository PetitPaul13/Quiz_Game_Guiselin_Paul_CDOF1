# main.py

# Définition des questions
questions = [
    {
        "question": "Quel empereur romain a légalisé le christianisme dans l'Empire romain ?",
        "choices": ["A) Néron", "B) Auguste", "C) Constantin", "D) Trajan"],
        "answer": "C"
    },
    {
        "question": "Quelle est la plus ancienne civilisation connue dans le monde ?",
        "choices": ["A) Égyptienne", "B) Mésopotamienne", "C) Indus", "D) Chinoise"],
        "answer": "B"
    },
    {
        "question": "Qui a découvert l'Amérique en 1492 ?",
        "choices": ["A) Marco Polo", "B) Christophe Colomb", "C) Leif Erikson", "D) Vasco de Gama"],
        "answer": "B"
    },
    {
        "question": "Quelle guerre s'est terminée par le Traité de Versailles en 1919 ?",
        "choices": ["A) La Guerre de Sept Ans", "B) La Guerre de Trente Ans", "C) La Première Guerre mondiale", "D) La Seconde Guerre mondiale"],
        "answer": "C"
    },
    {
        "question": "Quel roi d'Angleterre a signé la Magna Carta en 1215 ?",
        "choices": ["A) Richard Cœur de Lion", "B) Henri VIII", "C) Jean sans Terre", "D) Édouard Ier"],
        "answer": "C"
    },
    {
        "question": "Quelle est la plus ancienne civilisation connue dans le monde ?",
        "choices": ["A) Égyptienne", "B) Mésopotamienne", "C) Indus", "D) Chinoise"],
        "answer": "B"
    },
    {
        "question": "Quelle est la plus ancienne civilisation connue dans le monde ?",
        "choices": ["A) Égyptienne", "B) Mésopotamienne", "C) Indus", "D) Chinoise"],
        "answer": "B"
    },
    {
        "question": "Quelle est la plus ancienne civilisation connue dans le monde ?",
        "choices": ["A) Égyptienne", "B) Mésopotamienne", "C) Indus", "D) Chinoise"],
        "answer": "B"
    },
    {
        "question": "Quelle est la plus ancienne civilisation connue dans le monde ?",
        "choices": ["A) Égyptienne", "B) Mésopotamienne", "C) Indus", "D) Chinoise"],
        "answer": "B"
    },
    {
        "question": "Quelle est la plus ancienne civilisation connue dans le monde ?",
        "choices": ["A) Égyptienne", "B) Mésopotamienne", "C) Indus", "D) Chinoise"],
        "answer": "B"
    },
    {
        "question": "Quelle est la plus ancienne civilisation connue dans le monde ?",
        "choices": ["A) Égyptienne", "B) Mésopotamienne", "C) Indus", "D) Chinoise"],
        "answer": "B"
    },
    {
        "question": "Quel empereur romain a légalisé le christianisme dans l'Empire romain ?",
        "choices": ["A) Néron", "B) Auguste", "C) Constantin", "D) Trajan"],
        "answer": "C"
    },
    {
        "question": "Quelle est la plus ancienne civilisation connue dans le monde ?",
        "choices": ["A) Égyptienne", "B) Mésopotamienne", "C) Indus", "D) Chinoise"],
        "answer": "B"
    },
    {
        "question": "Quelle est la plus ancienne civilisation connue dans le monde ?",
        "choices": ["A) Égyptienne", "B) Mésopotamienne", "C) Indus", "D) Chinoise"],
        "answer": "B"
    },
    {
        "question": "Quelle est la plus ancienne civilisation connue dans le monde ?",
        "choices": ["A) Égyptienne", "B) Mésopotamienne", "C) Indus", "D) Chinoise"],
        "answer": "B"
    },
    {
        "question": "Quelle est la plus ancienne civilisation connue dans le monde ?",
        "choices": ["A) Égyptienne", "B) Mésopotamienne", "C) Indus", "D) Chinoise"],
        "answer": "B"
    },
    {
        "question": "Quel empereur romain a légalisé le christianisme dans l'Empire romain ?",
        "choices": ["A) Néron", "B) Auguste", "C) Constantin", "D) Trajan"],
        "answer": "C"
    },
    {
        "question": "Quelle est la plus ancienne civilisation connue dans le monde ?",
        "choices": ["A) Égyptienne", "B) Mésopotamienne", "C) Indus", "D) Chinoise"],
        "answer": "B"
    },
    {
        "question": "Quelle est la plus ancienne civilisation connue dans le monde ?",
        "choices": ["A) Égyptienne", "B) Mésopotamienne", "C) Indus", "D) Chinoise"],
        "answer": "B"
    },
    {
        "question": "Quelle est la plus ancienne civilisation connue dans le monde ?",
        "choices": ["A) Égyptienne", "B) Mésopotamienne", "C) Indus", "D) Chinoise"],
        "answer": "B"
    },


]

score = 0  # Initialisation du score

# Fonction pour poser les questions et vérifier les réponses
def ask_question(question):
    print(question["question"])
    for choice in question["choices"]:
        print(choice)
    user_answer = input("Entrez la lettre de votre réponse: ").upper()
    if user_answer == question["answer"]:
        return True
    else:
        return False

# Boucle pour poser chaque question
for question in questions:
    if ask_question(question):
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

# Affichage du score final
print(f"Votre score final est de {score} sur {len(questions)}.")
