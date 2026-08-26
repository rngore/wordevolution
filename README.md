# 🧬 Word Evolution
A Python-based genetic algorithm that evolves random strings toward a user-defined target. It demonstrates **fitness evaluation, selection, reproduction, and mutation** with a real-time Matplotlib graph.

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/word-evolution.git
cd word-evolution
```

### 2. Install the dependency

```bash
pip install matplotlib
```

### 3. Run the program

```bash
python main.py
```

Enter a target when prompted:

```text
Target: HELLO WORLD
```

## 🧠 How It Works

The program first creates a population of random strings. Each string is compared with the target and receives a **fitness score** based on how many characters are correct.

The best-performing strings, called **elites**, are selected to create the next generation. Their characters are copied, with a small chance of random mutation.

This process repeats until the target is successfully evolved.

```text
Random Population → Fitness → Select Elites → Mutate & Reproduce → New Generation
                                      ↑                                  │
                                      └──────────── Repeat ───────────────┘
```

## 📊 Visualization

The live Matplotlib graph displays:

* **Best Similarity** — fitness of the best organism.
* **Average Similarity** — average fitness of the population.
* **Generation** — current evolutionary cycle.

## ⚙️ Configuration

You can adjust these values in `main.py`:

```python
population_size = 100
elite_count = 10
mutation_rate = 0.10
```

Higher population sizes provide more candidates per generation, while the mutation rate controls how much randomness is introduced.

## 🧪 Example

```text
Target: HELLO

Best: XQZPA  → 0%
Best: HEKLO  → 80%
Best: HELLO  → 100%
```

The exact evolution and number of generations will vary because the algorithm uses randomness.

## 🛠️ Built With

* Python
* Matplotlib
* Genetic Algorithms

