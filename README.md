# Word Evolution

A Python based evolutionary computing project that simulates the process of natural selection by evolving a population of random strings toward a user defined target. Each generation evaluates the fitness of its organisms, selects the best performing individuals, and creates new variations through reproduction and mutation.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Genetic-Algorithm](https://img.shields.io/badge/Genetic%20Algorithm-purple)](https://en.wikipedia.org/wiki/Genetic_algorithm)

## How does it work?

The program first creates a population of random strings. Each string is compared with the target and receives a **score** based on how many characters are correct. The best-performing strings, called **elites**, are selected to create the next generation. Their characters are copied, with a small chance of random mutation.

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

Higher population sizes provide more candidates per generation, while the mutation rate/variation rate controls how much randomness is introduced.

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

The program will display the evolution progress directly in the terminal, including the current generation, best evolved string, similarity percentage, and generation time.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
