# CPSC1050-Project-2
The Quest For Watermelon
This is a game about trying to get your watermelon back from the big bad dude\n
It is recommended to have at least 11 lines in your terminal visible while playing\n
You play by writing out inputs in the terminal in the form of: Action Direction Repetition\n
The actions are help, move, attack, inspect, pickup and quit
Directions are up, down, left and right. It defaults to down if you write something else
Repetition is an integer for how many times you want the action to be done. It defaults to 1 and is not necessary for the input
Warning: you cannot stop an action that has started until all repetitions are done
If you win the game, you are given the number of each type of action that you have done as well as the number of invalid actions
Try to get the lowest total

Some gameplay things:
Enemies attack orthogonally after you do each action, that means they will hit you if you end your move next to them
You get three health back after defeating an enemy
Attack damage is your strength
Enemies are E's on the map
Items are I on the map. You can pick them up from the space next to them
You are P on the map
You go between rooms by moving to a spot with a T on it
Everything else is a wall
You can only move to spaces that are empty or have a T on them