
import time
import random
import sys

SLEEP_BETWEEN_ACTIONS = 1
MAX_VAL = 100
DICE_1_FACE = 6
DICE_2_FACE = 6

snakes = {
    16:6,
    46:25,
    49:11,
    62:19,
    64:60,
    74:53,
    92:88,
    95:75,
    99:80
}

ladders = {
    2:38,
    7:14,
    8:31,
    15:26,
    21:42,
    28:84,
    36:44,
    51:67,
    71:91,
    78:98,
    87:94
}

player_turn_text = [
    "Your turn.",
    "Go.Go.Go....",
    "Lets win this.",
    "Are you ready?",
   
]

snake_bite = [
    "boohoo",
    "bummer",
    "Gosh",
    "Aw..",
    "dang"
]

ladder_jump = [
    "woohoo",
    "Whoopee...",
    "Whoa.......",
    "Yo-ho-ho...",
    "yaayyy"
]


def welcome_msg():
    msg = """
    Welcome to Snake and Ladder Game.
    
    
    
    """
    print(msg)  
  
def get_player_names():
    player_1 = None
    while not player_1:
        player_1 = input("Please enter first player Name : ").strip()

    player_2 = None
    while not player_2:
        player_2 = input("Please enter second player Name : ").strip()

    print("\nMatch will be played between '" + player_1 + "' and '" + player_2 + "'\n")
    return player_1, player_2


def get_dice_value():
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    dice_1_value = random.randint(1, DICE_1_FACE)
    dice_2_value = random.randint(1,DICE_2_FACE)
    dice_value = dice_1_value + dice_2_value
    print("1st Dice value  " + str(dice_1_value))
    print("2nd Dice value  " + str(dice_2_value))
    return dice_value


def got_snake_bite(old_value, current_value, player_name):
    print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")
    print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))


def got_ladder_jump(old_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump).upper() + " ########")
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))


def snake_ladder(player_name, current_value, dice_value):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > MAX_VAL:
        print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value


def check_win(player_name, position):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    if MAX_VAL == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        print("\nThank you for playing the game.\n\n")
        sys.exit(1)


def start():
    welcome_msg()
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    player_1, player_2 = get_player_names()
    time.sleep(SLEEP_BETWEEN_ACTIONS)

    player1_current_position = 0
    player2_current_position = 0

    while True:
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        input_1 = input("\n" + player_1 + ": " + random.choice(player_turn_text) + " Hit the enter to roll your dice: ")
        print("\nRolling dice...")
        dice_value = get_dice_value()
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        print(player_1 + " moving....")
        player1_current_position = snake_ladder(player_1, player1_current_position, dice_value)

        check_win(player_1, player1_current_position)

        input_2 = input("\n" + player_2 + ": " + random.choice(player_turn_text) + " Hit the enter to roll your dice: ")
        print("\nRolling dice...")
        dice_value = get_dice_value()
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        print(player_2 + " moving....")
        player2_current_position = snake_ladder(player_2, player2_current_position, dice_value)

        check_win(player_2, player2_current_position)



if __name__ == "__main__":
    start()
