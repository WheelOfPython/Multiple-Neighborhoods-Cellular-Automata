# Multiple-Neighborhoods-Cellular-Automata
Trying to understand the Multiple Neighborhoods Cellular Automata algorithm. (Not complete)

# The Idea
Seems like MNCA can produce very fascinating results, when it comes to simulating microbial life.<br>
So that's my goal, to reproduce the increadable videos of MNCA I've seen on the internet.

# The Algorithm
From what I understand, instead of just summing up the living cells adjacent to every cell in order to decide if it lives or dies, like
Conway's Game of Life, with this algorithm, each cell is assinged a random value between 0 and 1 and with each step this value is decreased or stays the same by summing up all the values, not of the adjacent cells, but of the cells falling in diffrent patterns around the cell of intrest.<br>
By doing this, you get more complex behaviors and a gradient of colors, instead of just black and white.

# My Script
I've written the same algorithm in two scrpits, one in Python and one in p5.js, which can be run here: https://editor.p5js.org/ <br>
They're very basic and not at all rigorous, so I didn't bother writing any explanatory comments. <br>
They're more of an archive for me but I've made it public, just in case someone is interested.

# Results
This is the MNCA produced by the Python script:<br>
<p align="center">
  <img src="https://github.com/WheelOfPython/Multiple-Neighborhoods-Cellular-Automata/blob/main/res/output.gif?raw=true">
</p>
Doesn't seem very interesting but it's reminiscent of the real MNCAs.



# About MNCA
I've learned about MNCA from this YT video: Complex Behaviour from Simple Rules: 3 Simulations by Sebastian Lague

I couldn't find much information regarding MNCA on the first page of Google, so my implematation is based on this one:
https://softologyblog.wordpress.com/2018/03/09/multiple-neighborhoods-cellular-automata/
