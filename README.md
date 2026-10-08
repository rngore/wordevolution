# Word Evolution

A Python based evolutionary computing project that simulates the process of natural selection by evolving a population of random strings toward a user defined target. Each generation evaluates the fitness of its organisms, selects the best performing individuals, and creates new variations through reproduction and mutation. The project is designed as a practical demonstration of how genetic algorithms can be used to solve an optimization problem through repeated improvement rather than directly calculating the solution.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Genetic-Algorithm](https://img.shields.io/badge/Genetic%20Algorithm-purple)](https://en.wikipedia.org/wiki/Genetic_algorithm)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## How does it work?

Word Evolution starts with a population of completely random strings. Each string has the same length as the target and is generated using uppercase letters and spaces. The program then evaluates how closely each string resembles the target by comparing the characters at corresponding positions.
The organisms with the highest similarity scores are selected as the elite population. These individuals are used as parents for the next generation. During reproduction, their characters are copied to create new organisms, while the mutation rate determines the probability that individual characters will be randomly changed.
This process continues over multiple generations. As better-performing organisms are repeatedly selected for reproduction, the population generally becomes increasingly similar to the target. The simulation stops when an organism exactly matches the target.
This process repeats until the target is successfully evolved.

```text
Population → Fitness → Selection → Mutation → New Generation
     ↑                                           │
     └─────────────── Repeat ────────────────────┘
```

## Configuration

You can tweak these values in `main.py` or you can change the `variation_rate` when running the simulation:

```python
population_size = 100 # number of organisms in each generation
elite_count = 10 # top 10 selected organisms based on similarities
variation_rate = 0.10 # mutation rate
```
The mutation rate is provided when the program starts:
```text
Mutation rate (Default: 10%):
```
The population size determines how many organisms are generated in each generation. Increasing the population provides more possible candidates but also increases the amount of computation performed per generation.
The elite count determines how many of the strongest organisms are allowed to reproduce. A smaller elite group creates stronger selection pressure, while a larger group preserves more variation within the population.
The mutation rate determines how frequently characters are randomly changed during reproduction. A lower mutation rate allows successful characteristics to remain stable, while a higher mutation rate introduces more variation into the population

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/rngore/wordevolution.git
cd word-evolution
```

### 2. Run the program

```bash
python main.py
```

Enter a target when prompted:

```text
Target: HELLO WORLD
```
### Limitations & Future improvements

Word Evolution is intentionally a simplified genetic algorithm designed to demonstrate evolutionary concepts. Its fitness function only evaluates whether characters are present in the correct positions. It does not consider word meaning, grammar, character frequency, or other properties of natural language.
Because the algorithm relies on random initialization and mutation, different executions can require different numbers of generations to reach the same target. Longer targets can also require substantially more generations depending on the chosen population size and mutation rate.

Potential improvements include more advanced selection strategies, crossover between multiple parents, adaptive mutation rates, improved fitness functions, performance benchmarking, support for larger character sets, and additional configuration options. Implementing grammar and ways to consider word meaning.


