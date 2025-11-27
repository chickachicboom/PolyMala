from polymer_information_model import PolymerInformation
from polymer_introduction import polymer_introduction
from polymer_quiz_model import PolymerQuiz
from polymer_model import polymers_bank, quiz1_bank

polymala_on = True

print("\n\n\nWelcome to PolyMala!\n\n\n\nYour trusty (and slighty spicy) companion on a journey to learn all about polymers. Think of polymers like a mala--once you get to taste them, they're delicious, memorable, and maybe just a little bit addictive.\n\nSo, tell me...do you already want to know what polymers are?\nIf not, no worries--PolyMala isn't that spicy.\n")
print("Here's what you can do next:\n\n- Press 1: 'Wait...what is a polymer?' (A friendly intro!)\n- Press 2: 'Give me the basic knowledge--spicy but not too spicy.'\n- Press 3: 'I'm ready! Hit me with the polymer quiz!'\n- Press 0: 'Sorry, Mala isn't my thing. Maybe later when I want to try something spicy.' (Quit PolyMala.)")

menu = int(input())
polymer_information = PolymerInformation(polymers_bank)
polymer_quiz = PolymerQuiz(quiz1_bank,polymers_bank)

while polymala_on:
    if menu == 0:
        polymala_on = False
    elif menu == 1:
        polymer_introduction()
        print("🌶️  Ready to Level Up Your Polymer Knowledge?\n\nNow that you’ve learned what polymers are, how about we explore the different types of polymers—mala-skewer style?\n\n- Press 1: Let's review the lesson again\n- Press 2: Let’s dive in and see how each type packs its own flavor, just like ingredients at a mala stall!\n- Press 3: If you already know your linear-from-branched and your addition-from-condensation (or at least know your mushrooms-from-tofu), you can jump straight into the Polymer Quiz!\n- Press 0: Close PolyMala")
        menu = int(input())
    elif menu == 2:
        print("\n\n\nI'm curious about mala...but I'm even more curious about polymers!\n- Press 1: Browse one by one.\n- Press 2: See the whole sizzling menu.\n- Press 0: Go back to the main menu.")
        sub_menu = int(input())

        if sub_menu == 0:
            polymer_information_on = False
        elif sub_menu == 1:
            print("\n\nHere's the full spread of mala--oops, I mean all the polymers we have!\n\n")
            polymer_information.polymer_table()   
        else:
            print("\n\nBehold the entire lineup of spicy mala-style polymers--like buying out the hotpot stall!\n\n")
            while polymer_information.still_has_polymer():
                polymer_information.polymer_table_all()
            polymer_information.list = 0

        print("\n\nWanna continue exploring polymala?\n- Press 1: Go back to the basic.\n- Press 2: Craving another polymer dish.\n- Press 3: Ready to test your taste bud.\n- Press 0: Close PolyMala.")
        menu = int(input())
    else:
        polymer_quiz_on = True

        print("\n\nLet’s kick off our Polymer Quiz!")
        print("\n\nIf polymers were mala hotpot, you’re about to pick the flavor level you can handle. Ready to swirl your brain like noodles in chili oil? Let’s go!")
        print("\nWant to learn what polymers are, how they form, and why they’re basically the long, stretchy noodles of the chemistry world?\n- Press 1: Jump in before it gets too spicy!\n\nPrefer exploring different kinds of polymers, their properties, and what they’re used for — like choosing toppings for your mala bowl?\n- Press 2: Begin the flavor adventure!")
        sub_menu = int(input())

        if sub_menu == 0:
            polymer_quiz_on = False
        elif sub_menu == 1:
            while polymer_quiz.still_has_quiz():
                    polymer_quiz.polymer_quiz_1()
            polymer_quiz.list = 0

            if polymer_quiz.score == 10:
                print(f"\n\nYou score full marks (10/10).\nAmazing! You’re officially a Mala Master of Polymers! Your knowledge is boiling hot and full of flavor!")
            elif polymer_quiz.score >= 5:
                print(f"\n\nYour score is {polymer_quiz.score}/10 (Good)\nNot bad at all! Like a mild mala level—you feel the spice, but there’s room to fire it up. Give it another go!")
            else:
                print(f"\n\nYour score is {polymer_quiz.score}/10 (Needs improvement)\nNo worries! Even the best mala broth needs time to simmer. Practice a bit more and you’ll be polymer-spicy in no time!")
            polymer_quiz.score = 0
                    
        elif sub_menu == 2:
            print("\n\nThere are 10 questions waiting for you—each one asking about the abbreviation, type, properties, and uses of different polymers.\nThink of it as choosing ingredients for your perfect mala hotpot—but instead of spicy peppers, we’re mixing in spicy science!\n\n")

            while polymer_quiz.still_has_quiz():
                    polymer_quiz.polymer_quiz_2()
            polymer_quiz.list = 0

            if polymer_quiz.score == 40:
                print(f"\n\nYou score full marks (40/40).\nAmazing! You’re officially a Mala Master of Polymers! Your knowledge is boiling hot and full of flavor!")
            elif polymer_quiz.score >= 20:
                print(f"\n\nYour score is {polymer_quiz.score}/40 (Good)\nNot bad at all! Like a mild mala level—you feel the spice, but there’s room to fire it up. Give it another go!")
            else:
                print(f"\n\nYour score is {polymer_quiz.score}/40 (Needs improvement)\nNo worries! Even the best mala broth needs time to simmer. Practice a bit more and you’ll be polymer-spicy in no time!")
            polymer_quiz.score = 0
                    
        print("\n\nFeel like you can handle a hotter round? Want to stir the pot again for a better score?")
        print("\n- Press 1: Return to the beginner-friendly mala broth.\n- Press 2: Return to explore mala flovors.\n- Press 3: Start the quiz again\n- Press 0: Close PolyMala.")
                    
        menu = int(input())