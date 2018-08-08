from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print("Oops, how did you end up here?")
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n----------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):
    quips = ["You won't let a minor setback like this stop you, will you?",
            "Too bad, try again.",
            "Practice makes perfect, you know."]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class DarkCorridor(Scene):

    def enter(self):
        print("You find yourself in a spooky, dark corridor.")
        print("Howls and strange clangs reverberate through deep recesses.")
        print("You have no idea how you got there or where you are.")
        print("What you do know is that you want to get out of there. Now.")
        print("You could just run blindly up or down the corridor. Maybe you'll get lucky.")
        print("Or you could try to open one of these doors. Who knows what you'll find?")

        action = input("> ")

        if action in "run for your life":
            print("You break into a run towards a sliver of light, down the corridor.")
            print("This attracts the attention of some of the denizens of that place.")
            print("A werewolf comes out of nowhere and pounces on you.")
            print("Ouch. You don't want to know what happened after that.")
            return 'death'
        elif action in "try to open a door":
            print("You try to open some doors, hoping to find a way out.")
            print("After a few tries, one of the doors clicks open.")
            print("You open the door and walk into a dimly lit room.")
            return 'arsenal_room'
        else:
            print("So, you just stood there? Oh, crap, are you still there, dude?")
            return "dark_corridor"

class ArsenalRoom(Scene):
    def enter(self):
        print("The room you discovered is vast and full of shadows.")
        print("Torchlight is reflected on sharp metal, glinting near your head.")
        print("You realize that there are dozens of old weapons hanging from pegs on the walls.")
        print("You get the feeling that you'll need a weapon soon.")
        print("The only question is: which one to pick?")
        print("An axe, a sword or a lance?")

        choice = input("> ")

        if choice == "axe":
            print("Who ever heard of fighting vampires with an axe?")
            print("Get something pointy, man! Stake through the heart, remember?")
            return "arsenal_room"
        elif choice == "lance":
            print("That might work. It certainly qualifies as pointy.")
            print("However, it's too long to wield in corridors and narrow spaces.")
            return "arsenal_room"
        elif choice == "sword":
            print("OK, I guess a sword works best.")
            print("Short enough to wield, pointy enough to stab.")
            return "draculas_bedroom"
        else:
            print("There are no stakes, dude, he's not that stupid.")
            return "arsenal_room"

class DraculasBedroom(Scene):
    def enter(self):
        print("There's a door on the other side of the room. You decide to try to open it.")
        print("Holding the sword in your right hand, you try the doorknob with your left.")
        print("The door easily and slowly opens with a creak.")
        print("Heart pounding like a war drum in your chest, you step inside the room.")
        print("Suddenly, a cold gust of wind hits you and closes the door shut behind you.")
        print("There's a musty odor in the air, and a strange mist instantly envelops you.")
        print("Torchlight illuminates a large, richly decorated room, full of antique furniture.")
        print("However, there is one piece of furniture that quickly attracts your attention.")
        print("You instantly get shivers down your spine and stop breathing for a few seconds.")
        print("In the middle of the room, there's a huge coffin, or maybe a sarcophagus.")
        print("Its lid is off and it gapes wide open, empty and dark.")
        print("No sense in hanging around and waiting for the master of the house to return, right?")
        print("You look for a way out and notice there are three doors to the right.")
        print("Which one do you choose? Door number 1, door number 2 or door number 3?")

        choice = int(input("> "))

        if choice == 1:
            print("You try to open door number 1 and it swings open.")
            print("It's pitch dark beyond the doorway. You can't see a thing.")
            print("You take a step and realize, too late, that there's no floor.")
            print("You fall to your death into the murky depths below.")
            return 'death'
        elif choice == 2:
            print("You try to open door number 2 and it easily swings open.")
            print("A huge, blueish-gray, hairy hand grabs you and drags you into the darkness.")
            print("The last thing you see is a couple of bolts in a thick neck.")
            return "death"
        elif choice == 3:
            print("You try the doorknob on door number 3 and the door opens with a creak.")
            print("You discover a spiral stairwell that only goes up.")
            return "tower"
        else:
            print("There are just these 3 options, dude. No others.")
            return "draculas_bedroom"

class Tower(Scene):
    def enter(self):
        print("You go up the narrow staircase, tightly clenching the sword's hilt.")
        print("There are small windows here and there, letting in the light of the moon.")
        print("A loud, leathery flapping noise resounds from somewhere above you.")
        print("This makes you halt for a second, and your blood runs cold.")
        print("You feel like you're getting closer to some sort of confrontation.")
        print("But with who or what, you couldn't say.")
        print("All of a sudden, the staircase stops in front of a wooden door, slightly ajar.")
        print("You gingerly push the door, opening it a little more, and clasp the sword with both hands.")
        print("On the far side of a room, there's a black silhouette, standing in front of a large window. ")
        print("It seems to be shaped like a man, but unnaturally tall and thin.")
        print("He has his back to you. His tattered black cape is fluttering in the wind and moonlight.")
        print("As you take a step towards him, he suddenly turns and his stare freezes you in place.")
        print("You snap out of it and notice there are 3 suspicious-looking flagstones between you and him.")
        print("You feel like one of them might be a trap door. Which one do you choose to step on?")
        print("Number 1, number 2 or number 3?")

        choice = input("> ")

        if choice == 1:
            print("It turns out that it was a trap door and you fall into an unfathomably deep, dark pit.")
            return 'dungeon'
        else:
            print("It turns out that it was a trap door and you fall into an unfathomably deep, dark pit.")
            return "dungeon"

class Dungeon(Scene):
    def enter(self):
        print("You wake up with a start on a damp, cold, stone floor.")
        print("You have no idea how you survived that fall.")
        print("You vaguely remember something or someone catching you as you fell and passed out.")
        print("You look around you, trying to get your bearings. You see cells with locked doors.")
        print("It's a dungeon, and moonlight shines in through a small window up high.")
        print("Your sword's gone. You start searching for something you can use as a weapon.")
        print("You can't find anything and time is up. You feel a presence nearby.")
        print("He's there, watching you from the shadows.")
        print("He steps towards you, and he seems to be floating above the floor.")
        print("He speaks with a voice as deep as the sea: 'You won't need a weapon'.")
        print("'You will need sharp wits. If you answer right on all counts, you are free to go'.")
        print("'But if you answer wrong too many times, you shall never leave this place'.")
        print("'How do I know you'll keep your word?' you ask.")
        print("'You don't. First question.'")
        print("'What is (5.0*(8+(16-2.0)/(4+1))/2)%4?'")

        counter = 0
        answer = input("> ")

        if answer == str(3.0):
            print("'Correct. Second question.'")
            counter += 1
        else:
            print("'Wrong. Strike one, mortal.'")
            counter -= 1

        print("'What are the first 6 digits of pi?'")

        answer2 = float(input("> "))

        if answer2 == 3.14159:
            print("'Correct. Third question.'")
            counter += 1
        else:
            print("'Wrong. You should start worrying right about now.'")
            counter -= 1

        print("What is 2*(30-9)-2*(18+15)+3*(10+12)?")

        answer3 = int(input("> "))

        if answer3 == 42:
            print("'Correct.''")
            counter += 1
        elif answer3 != 42:
            print("'Incorrect.'")
            counter -= 1

        if counter < 3:
            print("The vampire's voice booms menacingly inside the dungeon.")
            print("'You are mine now. You'll stay here with the rest of the children of the night.'")
            print("In an instant, the vampire is right next to you and bites your neck.")
            print("Your neck hurts for a second and then you feel nothing at all.")
            print("You get a new perspective on life or, rather, undeath.")
            return "death"
        elif counter == 3:
            print("'You are free to go, mortal. Come back anytime. There's the way out.'")
            print("You hesitantly take a step towards the door he's pointing to.")
            print("You walk out of the dungeon and then something grabs you and pulls you into the darkness.")
            print("The vampire's evil laugh echoes through the halls of stone.")
            print("'Did you really think I'd set you free, fool? You're mine forever!'")
            print("The end.")
            exit(1)
        else:
            print("The end.")


class Map(object):

    scenes = {
    'dark_corridor': DarkCorridor(),
    'arsenal_room': ArsenalRoom(),
    'draculas_bedroom': DraculasBedroom(),
    'tower': Tower(),
    'dungeon': Dungeon(),
    'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

the_map = Map('dark_corridor')
the_game = Engine(the_map)
the_game.play()
