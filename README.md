# Word Evolution
A Python-based evolutionary computing project that simulates the process of natural selection by evolving a population of random strings toward a user-defined target. Each generation evaluates the fitness of its organisms, selects the best-performing individuals, and creates new variations through reproduction and mutation. Also includes a real-time Matplotlib visualization to track the progress of the best and average solutions across generations.
## How it works:
The program first creates a population of random strings. Each string is compared with the target and receives a **score** based on how many characters are correct. The best-performing strings, called **elites**, are selected to create the next generation. Their characters are copied, with a small chance of random mutation.

This process repeats until the target is successfully evolved.

```text
Population → Fitness → Selection → Mutation → New Generation
     ↑                                           │
     └─────────────── Repeat ────────────────────┘
```
## Matplotlib visualisation
<img width="1366" height="655" alt="evolution1" src="https://github.com/user-attachments/assets/99eba968-3ea4-45f8-8770-21d6466c5b19" />

## ⚙️ Configuration

You can adjust these values in `main.py`:

```python
population_size = 100
elite_count = 10
mutation_rate = 0.10
```
Higher population sizes provide more candidates per generation, while the mutation rate controls how much randomness is introduced.
## 📥 Installation
### 1. Clone the repository
```bash
git clone https://github.com/rngore/wordevolution.git
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
## 🛠️ Built With

* Python
* Matplotlib
* Genetic Algorithms

