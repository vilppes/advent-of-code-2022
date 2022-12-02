"""
choice:
Rock 1, Paper 2, Scissors 3
outcome:
loss: 0, draw: 3, win: 6


Rock(A) Paper(Y)
Paper(B) Rock(X)
Scissors(C) Scissors(Z)

The Elf finishes helping with the tent and sneaks back over to you. 
"Anyway, the second column says how the round needs to end: 
X means you need to lose, 
Y means you need to end the round in a draw
Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:
"""
characters = ["A","B","C"]
player_characters = ["X","Y","Z"]
character_properties = [[["Y"],["Z"],["X"]],[["Z"],["X"],["Y"]],[["X"],["Y"],["Z"]]]
def check_game_status(game_char_list):
    opponent_character = characters.index(game_char_list[0])
    opponent_character_loses = character_properties[opponent_character][0][0]
    opponent_character_wins = character_properties[opponent_character][1][0]
    opponent_character_ties = character_properties[opponent_character][2][0]
    player_character = game_char_list[1].split("\n")[0]
    if player_character == opponent_character_loses:
        return 6
    elif player_character == opponent_character_wins:
        return 0
    elif player_character == opponent_character_ties:
        return 3
    return 0

def main():
    total_score = 0
    f = open("input.txt", "r")
    for x in f:
        total_score += check_game_status(x.split(" ")) + (player_characters.index(x.split(" ")[1].split("\n")[0])+1)
        pass
    print("your score: ", total_score)
if __name__ == "__main__":
    main()