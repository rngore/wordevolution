import random
import string
import time
import matplotlib.pyplot as plt

char = string.ascii_uppercase + " " #This will help to generate all 24 uppercased alphabets and a Space (" ")
                                    #But not puntuation, numbers, etc.

def genword(length): #Generate a random word of length
    return ''.join(random.choice(char) for _ in range(length)) #integrate all random char into a generated word

def similarity(word, target): #Determines similarity score compared to target
    score = 0
    for i in range(len(target)):
        if word[i] == target[i]:
            score += 1
    return score

def main():
    target = input("Target: ").upper() #TARGET
    population_size = 100 #no. of organisms in each generation
    elite_count = 10 #selecting best 10 from population_size
    variation_rate = 0.10 #10% chance of randomly being mutated
    population = [] 
    for _ in range(population_size):
        population.append(genword(len(target))) #Add 100 organisms to first poplation w.r.t other
    generation = 0
    total_organisms = population_size
    generation_history = [] #Graph info - [0, 1, 2, 3, 4]
    best_similarity_history = [] #Graph info - eg.[20, 35, 50 , 70, 90] contains accuracy
    average_similarity_history = [] #Graph info - eg.[8, 15, 27, 40, 65] contains avg_accuracy
    start_time = time.perf_counter() #Timer for result

    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 7))

    while True: #Main evolution loop
        generation_start = time.perf_counter() #Timer for generation
        population.sort(key=lambda word: similarity(word, target), reverse=True) #Sorting the population generated from highest -> lowest
        elites = population[:elite_count] #Survived words
        best = population[0] #Highest priority generated word
        best_similarity = similarity(best, target) #Best similarity score
        average_similarity = sum(similarity(word, target) for word in population) / len(population)
        accuracy = (best_similarity / len(target)) * 100
        average_accuracy = (average_similarity / len(target)) * 100
        generation_time = (time.perf_counter() - generation_start)
        total_time = (time.perf_counter() - start_time)
        #Saving data
        generation_history.append(generation)
        best_similarity_history.append(accuracy)
        average_similarity_history.append(average_accuracy)

        ax.clear() #graph
        ax.plot(generation_history, best_similarity_history, label="Best Similarity", linewidth=2)
        ax.plot(generation_history, average_similarity_history, label="Average Similarity", linestyle="--")
        ax.set_xlim(0, max(10, generation + 1))
        ax.set_ylim(0, 105)
        ax.set_xlabel("Generation")
        ax.set_ylabel("Similarity (%)")
        ax.set_title("Word Evolution", fontsize=18)
        ax.grid(True, alpha=0.3)
        ax.legend()
        #Info
        information = (
            f"Target: {target}\n\n"
            f"Best: {best}\n"
            f"Similarity: {accuracy:.2f}%\n"
            f"Generation: {generation}\n"
            f"Population: {population_size}\n"
            f"Elites: {elite_count}\n"
            f"Variation: {variation_rate * 100:.1f}%\n\n"
            f"Organisms: {total_organisms:,}\n"
            f"Generation Time: {generation_time:.6f}s\n"
            f"Total Time: {total_time:.4f}s"
        )
        ax.text(1.02, 0.50, information, transform=ax.transAxes,fontsize=10,verticalalignment="center",
            bbox=dict(
                boxstyle="round",
                alpha=0.1))
        plt.tight_layout()
        plt.pause(0.001)
        if best == target: #target 
            plt.ioff()
            plt.show()
            break
        new_population = [] #The old population is replaced my new population
        for _ in range(population_size):
            parent = random.choice(elites) #choosing elite from top ten
            child = ""
            for letter in parent: #Variation
                if random.random() < variation_rate:
                    child += random.choice(char) #replacing the alphabet in parent with random char (Mutation)
                else:
                    child += letter
            new_population.append(child) 
        population = new_population #replace the old population
        total_organisms += population_size
        generation += 1

main()