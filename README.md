# CPSC1050-Project-2
The Quest For Watermelon
This is a game about trying to get your watermelon back from the big bad dude<br/>
It is recommended to have at least 11 lines in your terminal visible while playing<br/>
You play by writing out inputs in the terminal in the form of: Action Direction Repetition<br/>
The actions are help, move, attack, inspect, pickup and quit<br/>
Directions are up, down, left and right. It defaults to down if you write something else<br/>
Repetition is an integer for how many times you want the action to be done. It defaults to 1 and is not necessary for the input<br/>
Warning: you cannot stop an action that has started until all repetitions are done<br/>
If you win the game, you are given the number of each type of action that you have done as well as the number of invalid actions<br/>
Try to get the lowest total<br/>

Some gameplay things:<br/>
Enemies attack orthogonally after you do each action, that means they will hit you if you end your move next to them<br/>
You get three health back after defeating an enemy<br/>
Attack damage is your strength<br/>
Enemies are E's on the map<br/>
Items are I on the map. You can pick them up from the space next to them<br/>
You are P on the map<br/>
You go between rooms by moving to a spot with a T on it<br/>
Everything else is a wall<br/>
You can only move to spaces that are empty or have a T on them<br/>