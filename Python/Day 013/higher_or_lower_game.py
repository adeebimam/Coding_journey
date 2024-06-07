import random

def winner(celeb1, celeb2):
    if celeb1['followers'] > celeb2['followers']:
        return celeb1
    else:
        return celeb2
    
def result(winner, choice):
    if winner == choice:
        return "right"
    else:
        return "wrong"

def choice_func(choice):
    if choice == "a":
        selected_choice = celeb1
    else:
        selected_choice = celeb2
    return selected_choice

points = 0

celebs = [
    {"name": "Cristiano Ronaldo", "country": "Portugal", "field": "football player", "followers": 570},
    {"name": "Lionel Messi", "country": "Argentina", "field": "football player", "followers": 453},
    {"name": "Kylie Jenner", "country": "United States", "field": "entertainer", "followers": 394},
    {"name": "Selena Gomez", "country": "United States", "field": "entertainer", "followers": 380},
    {"name": "Dwayne 'The Rock' Johnson", "country": "United States", "field": "entertainer", "followers": 375},
    {"name": "Kim Kardashian", "country": "United States", "field": "entertainer", "followers": 366},
    {"name": "Ariana Grande", "country": "United States", "field": "entertainer", "followers": 355},
    {"name": "Beyoncé", "country": "United States", "field": "entertainer", "followers": 295},
    {"name": "Khloé Kardashian", "country": "United States", "field": "entertainer", "followers": 296},
    {"name": "Justin Bieber", "country": "Canada", "field": "entertainer", "followers": 284},
    {"name": "Kendall Jenner", "country": "United States", "field": "entertainer", "followers": 288},
    {"name": "National Geographic", "country": "United States", "field": "media", "followers": 287},
    {"name": "Taylor Swift", "country": "United States", "field": "entertainer", "followers": 284},
    {"name": "Jennifer Lopez", "country": "United States", "field": "entertainer", "followers": 248},
    {"name": "Neymar Jr.", "country": "Brazil", "field": "football player", "followers": 211},
    {"name": "Nike", "country": "United States", "field": "brand", "followers": 262},
    {"name": "Virat Kohli", "country": "India", "field": "cricketer", "followers": 256},
    {"name": "Nicki Minaj", "country": "United States", "field": "entertainer", "followers": 222},
    {"name": "Miley Cyrus", "country": "United States", "field": "entertainer", "followers": 215},
    {"name": "Kourtney Kardashian", "country": "United States", "field": "entertainer", "followers": 217},
    {"name": "Kevin Hart", "country": "United States", "field": "entertainer", "followers": 163},
    {"name": "Zendaya", "country": "United States", "field": "entertainer", "followers": 171},
    {"name": "Demi Lovato", "country": "United States", "field": "entertainer", "followers": 154},
    {"name": "Ellen DeGeneres", "country": "United States", "field": "entertainer", "followers": 149},
    {"name": "Real Madrid CF", "country": "Spain", "field": "football club", "followers": 146},
    {"name": "Billie Eilish", "country": "United States", "field": "entertainer", "followers": 108},
    {"name": "Rihanna", "country": "Barbados", "field": "entertainer", "followers": 155},
    {"name": "FC Barcelona", "country": "Spain", "field": "football club", "followers": 114},
    {"name": "NASA", "country": "United States", "field": "government", "followers": 98},
    {"name": "Shakira", "country": "Colombia", "field": "entertainer", "followers": 79},
    {"name": "LeBron James", "country": "United States", "field": "basketball player", "followers": 162},
    {"name": "Chris Brown", "country": "United States", "field": "entertainer", "followers": 125},
    {"name": "Cardi B", "country": "United States", "field": "entertainer", "followers": 152},
    {"name": "Shawn Mendes", "country": "Canada", "field": "entertainer", "followers": 72},
    {"name": "Gigi Hadid", "country": "United States", "field": "model", "followers": 82},
    {"name": "Emma Watson", "country": "United Kingdom", "field": "actress", "followers": 74},
    {"name": "Priyanka Chopra", "country": "India", "field": "entertainer", "followers": 88},
    {"name": "Huda Kattan", "country": "United States", "field": "beauty influencer", "followers": 52},
    {"name": "Niall Horan", "country": "Ireland", "field": "entertainer", "followers": 42},
    {"name": "David Beckham", "country": "United Kingdom", "field": "football player", "followers": 78},
    {"name": "Gal Gadot", "country": "Israel", "field": "actress", "followers": 98},
    {"name": "Camila Cabello", "country": "Cuba", "field": "entertainer", "followers": 66},
    {"name": "Zayn Malik", "country": "United Kingdom", "field": "entertainer", "followers": 48},
    {"name": "Snoop Dogg", "country": "United States", "field": "entertainer", "followers": 77},
    {"name": "Vin Diesel", "country": "United States", "field": "actor", "followers": 80},
    {"name": "Anitta", "country": "Brazil", "field": "entertainer", "followers": 64},
    {"name": "Shakira", "country": "Colombia", "field": "entertainer", "followers": 87},
    {"name": "Katy Perry", "country": "United States", "field": "entertainer", "followers": 96},
    {"name": "Will Smith", "country": "United States", "field": "entertainer", "followers": 67},
    {"name": "Victoria Beckham", "country": "United Kingdom", "field": "fashion designer", "followers": 28}
]


print("\nGreetings! Welcome to our Higher or Lower game.")
print("Two personalities will be compared, and you have to guess who has more Instagram followers.")
print("Type 'A' or 'B' to make your choice. If you're right, you proceed to the next round. Otherwise, the game is over.\n")

celeb1 = random.choice(celebs)
celeb2 = random.choice(celebs)

while celeb1 == celeb2:
    celeb2 = random.choice(celebs)

running = True
while running:

    print(f"Compare A: {celeb1['name']}, a {celeb1['field']}.")
    print("vs")
    print(f"Compare B: {celeb2['name']}, a {celeb2['field']}\n")

    winn = winner(celeb1, celeb2)

    choice_input = input("Who has more followers, A or B? ").lower()

    choice_answer = choice_func(choice_input)

    answer = result(winn, choice_answer)

    if answer == "right":
        points += 1
        print(f"\nCorrect! {choice_answer['name']} has more followers.")
        print(f"Your current points: {points}\n")
        celeb1 = celeb2
        celeb2 = random.choice(celebs)
        while celeb1 == celeb2:
            celeb2 = random.choice(celebs)
    else:
        print(f"\nWrong! The correct answer was {winn['name']} with {winn['followers']} million followers.")
        print(f"Your final score is {points}. Thanks for playing!")
        running = False

print("\nThank you for playing! See you next time.")
