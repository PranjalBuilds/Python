questions = [
    ['What is the capital of India?', 'Delhi', 'Mumbai', 'Kolkata', 'Chennai', 1],
    ['What is the largest planet in our solar system?', 'Earth', 'Mars', 'Jupiter', 'Saturn', 3],
    ['Who wrote "Romeo and Juliet"?', 'Charles Dickens', 'William Shakespeare', 'Mark Twain', 'J.K. Rowling', 2],
    ['What is the chemical symbol for water?', 'H2O', 'O2', 'CO2', 'N2', 1],
    ['What is the tallest mountain in the world?', 'K2', 'Mount Everest', 'Kanchenjunga', 'Makalu', 2],
    ['Who was the first President of the United States?', 'George Washington', 'Abraham Lincoln', 'John Adams', 'Thomas Jefferson', 1],
    ['Which is the fastest land animal?', 'Cheetah', 'Lion', 'Leopard', 'Tiger', 1],
    ['What is the boiling point of water (in Celsius)?', '90', '100', '110', '120', 2],
    ['Which planet is known as the Red Planet?', 'Mercury', 'Mars', 'Jupiter', 'Venus', 2],
    ['What is the national flower of Japan?', 'Rose', 'Cherry Blossom', 'Lotus', 'Tulip', 2],
    ['Who developed the theory of relativity?', 'Isaac Newton', 'Galileo Galilei', 'Albert Einstein', 'Niels Bohr', 3],
    ['What is the largest mammal?', 'Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus', 2],
    ['Which ocean is the largest?', 'Indian Ocean', 'Atlantic Ocean', 'Pacific Ocean', 'Arctic Ocean', 3],
    ['What is the square root of 144?', '10', '11', '12', '13', 3],
    ['Who painted the Mona Lisa?', 'Vincent van Gogh', 'Leonardo da Vinci', 'Pablo Picasso', 'Claude Monet', 2],
    ['What is the currency of Japan?', 'Yen', 'Won', 'Dollar', 'Euro', 1],
    ['What is the smallest prime number?', '0', '1', '2', '3', 3],
    ['Which metal is liquid at room temperature?', 'Iron', 'Mercury', 'Gold', 'Aluminum', 2],
    ['What is the national bird of the United States?', 'Peacock', 'Eagle', 'Hawk', 'Sparrow', 2],
    ['How many colors are there in a rainbow?', '5', '6', '7', '8', 3],
    ['What is the chemical symbol for gold?', 'Ag', 'Au', 'Gd', 'Pb', 2],
    ['Which desert is the largest in the world?', 'Sahara', 'Arctic', 'Gobi', 'Kalahari', 1],
    ['Who is known as the Father of Computers?', 'Alan Turing', 'Charles Babbage', 'John von Neumann', 'Steve Jobs', 2],
    ['How many continents are there?', '5', '6', '7', '8', 3],
    ['What is the capital of Italy?', 'Milan', 'Rome', 'Florence', 'Naples', 2],
    ['What is the hardest natural substance on Earth?', 'Iron', 'Graphite', 'Diamond', 'Platinum', 3],
    ['What is the chemical symbol for oxygen?', 'O', 'O2', 'Ox', 'O3', 1],
    ['Which country is the largest by area?', 'USA', 'China', 'Canada', 'Russia', 4],
    ['What is the capital of Australia?', 'Sydney', 'Melbourne', 'Canberra', 'Brisbane', 3],
    ['Who discovered penicillin?', 'Alexander Fleming', 'Marie Curie', 'Louis Pasteur', 'Gregor Mendel', 1],
    ['What is the most spoken language in the world?', 'Spanish', 'Mandarin Chinese', 'English', 'Hindi', 2],
    ['Which country is known for the Great Wall?', 'Japan', 'China', 'South Korea', 'Vietnam', 2],
    ['What is the national animal of India?', 'Elephant', 'Peacock', 'Tiger', 'Lion', 3],
    ['Which planet has the most moons?', 'Earth', 'Jupiter', 'Saturn', 'Uranus', 3],
    ['What is the smallest country in the world?', 'Monaco', 'Maldives', 'Vatican City', 'Liechtenstein', 3],
    ['What is the capital of Germany?', 'Munich', 'Frankfurt', 'Berlin', 'Hamburg', 3],
    ['How many legs does a spider have?', '6', '8', '10', '12', 2],
    ['Which element has the atomic number 1?', 'Hydrogen', 'Helium', 'Oxygen', 'Carbon', 1],
    ['Who invented the light bulb?', 'Thomas Edison', 'Nikola Tesla', 'Alexander Bell', 'Michael Faraday', 1],
    ['What is the largest island in the world?', 'Greenland', 'New Guinea', 'Borneo', 'Madagascar', 1],
    ['Which planet is closest to the Sun?', 'Mercury', 'Venus', 'Earth', 'Mars', 1],
    ['Who wrote "The Odyssey"?', 'Socrates', 'Homer', 'Aristotle', 'Plato', 2],
    ['What is the process by which plants make food?', 'Photosynthesis', 'Respiration', 'Transpiration', 'Digestion', 1],
    ['Which gas makes up most of the Earth’s atmosphere?', 'Oxygen', 'Carbon Dioxide', 'Nitrogen', 'Argon', 3],
    ['What is the freezing point of water (in Celsius)?', '0', '100', '32', '-1', 1],
    ['Which is the smallest planet in the solar system?', 'Mercury', 'Mars', 'Venus', 'Pluto', 1],
    ['Who is known as the Iron Man of India?', 'Mahatma Gandhi', 'Subhash Chandra Bose', 'Sardar Patel', 'Bhagat Singh', 3],
    ['What is the capital of Canada?', 'Toronto', 'Vancouver', 'Ottawa', 'Montreal', 3],
    ['What is the speed of light?', '3 x 10^6 m/s', '3 x 10^8 m/s', '3 x 10^10 m/s', '3 x 10^12 m/s', 2]
]

levels = [1000, 2000, 5000, 10000, 20000, 35000, 50000, 75000, 100000, 150000, 200000, 275000, 320000, 400000, 500000, 750000, 1000000]

money = 0
for i in range(len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]} ")
    print(question[0])
    print(f"a. {question[1]}          b. {question[2]} ")
    print(f"c. {question[3]}          d. {question[4]} ")

    reply = int(input("Enter your answer (1-4) or 0 to quit: "))
    
    # Quitting logic
    if reply == 0:
        print(f"You have quit the game. You take home Rs. {money}\n ")
        break

    # Correct answer
    if reply == question[-1]:
        money = levels[i]  # Update money to the current question's amount
        print(f"Correct answer, you have won Rs. {money} ")
    else:
        # Wrong answer
        print("Wrong answer! ")
        print(f"Sorry, you take home Rs. {money} ")
        break
