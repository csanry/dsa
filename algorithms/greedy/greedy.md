# Greedy Algorithm

- Greedy algorithms approach a problem by selecting the best option available *at the moment*

- It doesn't worry whether the current best result will lead to the overall optimal result

- The algorithm never reverses the earlier decision even the choice is suboptimal

- As a result, the algorithm may not guarantee the best result (globally optimal)

## Characteristics

Problems with the following properties are suitable for greedy algorithms

1. Greedy choice property

    - If an optimal solution to the problem can be found by choosing the best choice at each step without considering the previous steps once chosen

    - The problem is said to have a greedy choice property and can be solved using a greedy approach

2. Optimal substructure

    - If the optimal overall solution to the problem corresponds to the optimal solution to its subproblems

    - The problem has optimal substructure and can be solved using a greedy approach

## Advantages

- Easy to describe

- Typically, better performance

## Algorithm

Given a set of coins of different denominations

```
Available coins
$5 coin
$2 coin
$1 coin
```

Make a change of amount using the smallest possible number of coins
```
eg $18
```

There is no limit to the number of coins you can use

## Approach

- Always select the coin with the largest value (greedy choice property of hoping to hit the target sum quicker)

    - Iteration one: select 5, solution set $\lbrace5\rbrace$

    - Iteration two: select 5, solution set $\lbrace5, 5\rbrace$, sum 10

    - Iteration three: select 5, solution set $\lbrace5, 5, 5\rbrace$, sum 15

    - Iteration four: select 2 (we cannot select 5 as that will go over the target), solution set $\lbrace5, 5, 5, 2\rbrace$, sum 17

    - Iteration five: select 1 (we cannot select 2), solution set $\lbrace5, 5, 5, 2, 1\rbrace$, sum 18

    - The smallest possible number of coins is 5

- This does not always guarantee correctness
