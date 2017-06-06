"""
CHALLENGE 2 - BOWLING (https://contest.tuenti.net/Challenges?id=2)

You have probably heard about bowling before, but you may not know how to score a bowling game correctly.
A game of bowling consists of ten frames, in which the player has the chance to knock down ten pins. The player has two
rolls in each frame, which means he can throw the ball twice. If the player knocks down all ten pins on the first roll,
they don't need a second roll for the frame. This kind of frame is called a "strike". If the player knocks down some
pins on the first roll and all remaining pins on the second roll (i.e.: 6 and 4), we call the frame a "spare". For each
frame, the player is awarded as many points as pins knocked down. For instance, if the player knocks down 3 and 5 pins
the score awarded for the frame is 8. If the frame is a spare, the pins knocked down on the next roll are awarded as a
bonus. If the frame is a strike, the pins knocked down on the next two rolls are awarded as a bonus. The 10th frame is
a bit special: if it ends up being spare or a strike, the player gets one or two extra rolls. These extra rolls are
solely used to add extra points to the strike/spare and don't provide any points by themselves. Take a look here
(http://slocums.homestead.com/gamescore.html) for more information.

You have been asked to program a simple firmware for your local bowling alley. You need to calculate the score of each
frame based on the number of pins knocked down on each roll of a game.


INPUT
The first line will contain an integer C, the number of cases for our problem.
Each case starts with a line with an integer R, the number of rolls. A line with R integers follows, each indicating the
pins knocked down in the roll Ri.


OUTPUT
For each case, a line starting with "Case #x: " followed by 10 integers separated by spaces, indicating the score of
each frame. Every line is followed by a new line character.


EXAMPLES
Case 1:
20
5 4 1 3 0 7 4 5 3 0 2 5 2 4 5 0 7 1 4 4

Case 2:
19
9 0 4 0 8 0 4 5 7 0 10 4 1 7 1 6 3 5 4

Case 3:
17
10 7 2 9 1 10 10 7 1 8 0 7 0 10 10 4 2

Case 4:
12
10 10 10 10 10 10 10 10 10 10 10 10

Case 1 is very straightforward as there aren't any strikes or spares.
In Case 2, there is a strike in the 6th frame, which gets 10 + 4 + 1 points.
In Case 3, there are a few strikes and spares. Pay special attention to the last frame: it gets 10 + 4 + 2 points.
In Case 4 is the perfect bowling game: every frame is worth 30 points.


SAMPLE INPUT
4
20
5 4 1 3 0 7 4 5 3 0 2 5 2 4 5 0 7 1 4 4
19
9 0 4 0 8 0 4 5 7 0 10 4 1 7 1 6 3 5 4
17
10 7 2 9 1 10 10 7 1 8 0 7 0 10 10 4 2
12
10 10 10 10 10 10 10 10 10 10 10 10


SAMPLE OUTPUT
Case #1: 9 13 20 29 32 39 45 50 58 66
Case #2: 9 13 21 30 37 52 57 65 74 83
Case #3: 19 28 48 75 93 101 109 116 140 156
Case #4: 30 60 90 120 150 180 210 240 270 300

"""

# Preparing the input
fin = open('submitInput.txt')
fout = open('submitOutput.txt', 'w')

lines = fin.readlines()
cases = int(lines[0])

for i in range(1, cases+1):
    fout.write('Case #{}:'.format(i))

    # Pins knocked down in each roll
    rolls = [int(roll) for roll in lines[2*i].split(" ")]

    score = 0  # Total score achieved on this play
    j = 0   # Indicates the roll we're currently counting
    current_frame = 0  # Current frame

    while True:

        # STRIKE: Adding the current frame and the two following rolls
        if rolls[j] == 10:
            score += rolls[j] + rolls[j+1] + rolls[j+2]
            j += 1  # The next roll is part of a new frame, so we'll need to count it again

        # SPARE: Adding the current frame and the next roll
        elif (rolls[j] + rolls[j+1] == 10):
            score += rolls[j] + rolls[j+1] + rolls[j+2]
            j += 2  # The next roll is part of the current frame, so we'll skip it

        # ELSE: Adding the current frame
        else:
            score +=  rolls[j] + rolls[j+1]
            j += 2  # The next roll is part of the current frame, so we'll skip it

        current_frame += 1

        fout.write(' {}'.format(score))

        # Stop condition: no more rolls left or we've already completed frame 10.
        if j >= len(rolls) or current_frame == 10:
            break


    fout.write('\n')

fin.close()
fout.close()