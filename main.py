import random
import string
import time

char = string.ascii_uppercase + " "


def generate_population(population_size, target):
    return [genword(len(target)) for _ in range(population_size)]


def get_average_similarity(population, target):
    return sum(similarity(word, target) for word in population) / len(population)


def reproduce(elites, population_size, variation_rate):
    new_population = []

    for _ in range(population_size):
        parent = random.choice(elites)
        child = ""

        for letter in parent:
            if random.random() < variation_rate:
                child += random.choice(char)
            else:
                child += letter

        new_population.append(child)

    return new_population


def genword(length):
    return ''.join(random.choice(char) for _ in range(length))


def similarity(word, target):
    score = 0
    for i in range(len(target)):
        if word[i] == target[i]:
            score += 1
    return score


def main():
    target = input("Target: ").upper()

    if not target:
        print("Target cannot be empty.")
        return

    if any(c not in char for c in target):
        print("Use only uppercase letters (A-Z) and spaces.")
        return

    population_size = 100
    elite_count = 10

    inp_mutrate = input("Mutation rate (Default: 10%): ").strip(" %")

    if inp_mutrate == '':
        variation_rate = 0.10
    else:
        try:
            variation_rate = int(inp_mutrate) / 100
            if not 0 <= variation_rate <= 1:
                print("Mutation rate must be between 0% and 100%.")
                return
        except ValueError:
            print("Please enter a valid mutation rate.")
            return

    # Generate initial population
    population = generate_population(population_size, target)

    generation = 0
    total_organisms = population_size
    start_time = time.perf_counter()

    print("\n" + "=" * 77)
    print("                    WORD EVOLUTION SIMULATION")
    print("=" * 77)
    print(f"Target: {target}")
    print(f"Population: {population_size}")
    print(f"Elites: {elite_count}")
    print(f"Mutation rate: {variation_rate * 100:.1f}%")
    print("=" * 77)

    # Main evolution loop
    while True:
        generation_start = time.perf_counter()

        # Rank population from best to worst
        population.sort(
            key=lambda word: similarity(word, target),
            reverse=True
        )

        elites = population[:elite_count]
        best = population[0]

        best_similarity = similarity(best, target)
        average_similarity = get_average_similarity(population, target)

        accuracy = (best_similarity / len(target)) * 100
        average_accuracy = (average_similarity / len(target)) * 100

        generation_time = time.perf_counter() - generation_start
        elapsed_time = time.perf_counter() - start_time

        # Print generation information
        print(
            f"Generation: {generation:6} | "
            f"Best: {best!r} | "
            f"Similarity: {accuracy:6.2f}% | "
            f"Gen Time: {generation_time:.5f}s | "
        )

        if best == target:
            break

        population = reproduce(elites, population_size, variation_rate)
        
        total_organisms += population_size
        generation += 1

    total_time = time.perf_counter() - start_time

    print("\n" + "=" * 77)
    print("                    SIMULATION COMPLETE")
    print("=" * 77)
    print(f"Target word       : {target}")
    print(f"Evolved word      : {best}")
    print(f"Final similarity  : {accuracy:.2f}%")
    print(f"Generations       : {generation}")
    print(f"Population size   : {population_size}")
    print(f"Total organisms   : {total_organisms:,}")
    print(f"Mutation rate     : {variation_rate * 100:.1f}%")
    print(f"Total time        : {total_time:.5f} seconds")
    print("=" * 77)


if __name__ == "__main__":
    main()
