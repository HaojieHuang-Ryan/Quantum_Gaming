# Quantum Gaming
This is a super simple game loosely based on Minesweeper Flags and runs on the [IBM Quantum computer](https://quantum-computing.ibm.com/) or [Qiskit simulator](https://qiskit.org/).
## Prepared environment:
1. pip install qiskit[0.24.0]  (New version is not work in some cases)
2. sudo apt-get install python3-tk
3. sudo apt-get install python3-pil python3-pil.imagetk
4. pip install qrandom

## Run the program:
python3 init.py

## Introduction:
![Game Screen](/pictures/1.png)  
The original idea for this quantum game comes from Minesweeper and Catsweeper. Since we considered  probabilistic cases like trap and target, we decided to use quantum instead of classical probability to better apply quantum computing knowledge to this game, and also maintain the playability and entertainment of sweep type game. In our game design, the game panel is 8x8. There are three types of mud blocks, 10 trap mud blocks, 1 target mud block, and the rest are empty mud blocks. To win this game, players should avoid clicking trap mud blocks as much as possible and find out the target mud block. To make this game easier, we add a spell button that can be used to check and link the two unknown blocks at most  three times. And, We set the trap firing rate through the H Gate with a 50 percent probability of 0 and 1, which means that even though the player has hit the trap, there is still a chance of not getting caught. The general idea for the trap in this game is by using  quantum gates. And the qubits are generated by the Quantum Random Number Generator.

## Game Page
![Game Screen](/pictures/2.png)
![Game Screen](/pictures/3.png)  
We need to set ten traps and one target in random location. That's why we use the random number generator.

## Random Generator
Due to the game panel is 8*8, we use 000 to 111 in binary to represent the numbers 0 to 7. So we need to use three qubits and apply Hadamard Gate on each of them to represent one binary. Therefore, each qubit equals 0 or 1 with 50% probability.  
![](/pictures/4.png)
![Code](/pictures/5.png)

## Trap and Empty block
![](/pictures/6.png)  
These mud blocks we can divide them into three kinds. A green trap means you stepped on the trap but it didn't trigger, you can continue the game. Red trap means you triggered the trap and lost the game. The rest we collectively call empty mud. The empty mud contains trap tips, question marks, and pig.
![](/pictures/7.png)  
The principle of realization is that in trap mud blocks, Hadamard Gate is applied on them while clicking to get a positive ket, then the quantum is in a superposition state. Then there is a 50 percent probability to get 1, which means that you survive in traps, and the other 50 percent probability to get 0 means you lose.
![](/pictures/8.png)  
In empty mud blocks, to make this different from the positive ket, one X Gate and one Hadamard Gate are applied to them while clicking to get a negative ket. At this point, you will get a question mark or a number. You can use skills when you feel a question mark affects your decision on where to click.

## Spell (Cheater)
![](/pictures/9.png)  
Therefore we can apply a CNOT Gate on them. When you using the cheater, the empty mud block you click first is the controlled bit, and the second empty mud block you click is the target bit. For CNOT Gate, if two blocks have the same type, you will get the result 1 which is true and if they are different, you will get 0 which is false.To make the result easier to use, we add another X gate on the second bit and measure it. The result will be ket 1 if two blocks have the same type, and you will get two blocks with the same color highlighted. Otherwise, the result will be 0 ket and you will get two blocks with different colors highlighted.

## Reference
### Ideas from Catsweeper Minesweeper(https://github.com/desireevl/quantum-catsweeper)
### Icons (https://www.iconfont.cn)
