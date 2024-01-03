# The dumbest algorithm that I've conceived.

This program generates a number sequence for you to use in your next money-burning session

**Functionality**
+ Generates a sequence of numbers that fits the ruleset of a specified lottery type
+ Checks the generated sequence for supposedly unlikely sequences
+ Regenerates a new sequence if it is determined to be unlikely to appear (though they are all equally likely to appear, tbh)
+ Outputs the sequence for the delusional gambler to use for their next lottery ticket :P (aka me ahahaha i need help)

**Specs**
+ Supports: Mega Million
+ Raises your chance of winning by ~0.0%

**Generation Details**
+ Removes past winning numbers
+ Removes patterns with linear increments (ex. 1, 3, 5, 7, 9)
+ Removes all even/odd

**Additional**
+ analyze_csv.py graphs the past winning numbers of mega millions since 2002.
+ matplotlib is required to use this function.