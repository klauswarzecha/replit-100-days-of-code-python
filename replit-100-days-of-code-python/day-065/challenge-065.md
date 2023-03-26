# Day 065 Challenge

Today is a project day! You're going to use what you've learned about OOP (on Day 64) to store characters for my video game.

1. My game needs to have a character with a name, health and magic points.
1. It needs these values setup when it is initialized.
1. It needs a method to output this data.
1. There should be a sub-class 'player' which inherits from character and also has a number of lives.
1. Player should also have an 'am I alive?' method which checks the player status and reports back yes or no.
1. There should also be an 'enemy' sub-class with additional 'type' and 'strength'.
1. 'enemy' should have two sub-classes:
    1. 'orc' with a 'speed' attribute.
    1. 'vampire' with a 'day/night' tracker
1. Instantiate one player, two vampires and three orcs. You choose their names.
1. Print out their values.