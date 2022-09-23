This is a simple game to demonstrate core Jack functionality.

You control a character that moves about the screen using the keyboard arrow keys.

You collect money by moving the character over the money icons.

You can quit the game at any time using keyboard: q

----

The most difficult part of the implementation was collision detection.

The money objects are placed into an array and this is used to track each object.

Whenever the character moves, the array is iterated over, and each active money item
will have the coordinates checked to see if a collision is detected.  I hope you like
this implementation, it would also be extendable if you were to add additional
money objects.
