import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def get_jobs_from_user():
    num_jobs = int(input("Enter the number of jobs: "))
    num_machines = int(input("Enter the number of machines: "))
    
    jobs = []
    for job_id in range(num_jobs):
        print(f"Enter operations for job {job_id+1}:")
        operations = []
        for op_id in range(num_machines):
            machine = int(input(f"  Operation {op_id+1} machine: "))
            time = int(input(f"  Operation {op_id+1} processing time: "))
            operations.append((machine, time))
        jobs.append(operations)
    
    return num_jobs, num_machines, jobs

class JobShopGA:
    
    def __init__(self, jobs, num_machines, population_size=50, generations=100, crossover_rate=0.8, mutation_rate=0.1):
        self.jobs = jobs
        self.num_machines = num_machines
        self.population_size = population_size
        self.generations = generations
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            chromosome = list(range(len(self.jobs)))
            random.shuffle(chromosome)
            population.append(chromosome)
        return population

    def fitness(self, chromosome):
        machine_times = [0] * self.num_machines
        job_times = [0] * len(self.jobs)
        for job_idx in chromosome:
            for machine, time in self.jobs[job_idx]:
                start_time = max(machine_times[machine], job_times[job_idx])
                machine_times[machine] = start_time + time
                job_times[job_idx] = machine_times[machine]
        return max(machine_times)

    def selection(self, population, fitnesses):
        total_fitness = sum(fitnesses)
        selection_probs = [f / total_fitness for f in fitnesses]
        return population[np.random.choice(len(population), p=selection_probs)]

    def crossover(self, parent1, parent2):
        if random.random() > self.crossover_rate:
            return parent1[:], parent2[:]
        cut_point = random.randint(1, len(parent1) - 1)
        child1 = [-1] * len(parent1)
        child2 = [-1] * len(parent2)
        child1[:cut_point] = parent1[:cut_point]
        child2[:cut_point] = parent2[:cut_point]
        pos = cut_point
        for job in parent2:
            if job not in child1:
                child1[pos] = job
                pos += 1
        pos = cut_point
        for job in parent1:
            if job not in child2:
                child2[pos] = job
                pos += 1
        return child1, child2

    def mutate(self, chromosome):
        if random.random() < self.mutation_rate:
            idx1, idx2 = random.sample(range(len(chromosome)), 2)
            chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]

    def run(self):
        population = self.initialize_population()
        best_fitness = float('inf')
        best_schedule = None

        for generation in range(self.generations):
            fitnesses = [self.fitness(chromosome) for chromosome in population]
            new_population = []
            for _ in range(self.population_size // 2):
                parent1 = self.selection(population, fitnesses)
                parent2 = self.selection(population, fitnesses)
                child1, child2 = self.crossover(parent1, parent2)
                self.mutate(child1)
                self.mutate(child2)
                new_population.extend([child1, child2])

            population = new_population
            min_fitness = min(fitnesses)
            if min_fitness < best_fitness:
                best_fitness = min_fitness
                best_schedule = population[fitnesses.index(min_fitness)]

        return best_schedule, best_fitness

    def create_gantt_chart(self, schedule):
        machine_times = [0] * self.num_machines
        job_times = [0] * len(self.jobs)
        tasks = []

        for job_idx in schedule:
            for machine, time in self.jobs[job_idx]:
                start_time = max(machine_times[machine], job_times[job_idx])
                machine_times[machine] = start_time + time
                job_times[job_idx] = machine_times[machine]
                tasks.append((machine, start_time, time, job_idx))

        fig, gnt = plt.subplots()
        gnt.set_ylim(0, 10 * self.num_machines)
        gnt.set_xlim(0, max(machine_times) + 10)
        gnt.set_xlabel('Time')
        gnt.set_ylabel('Machines')

        gnt.set_yticks([i * 10 + 5 for i in range(self.num_machines)])
        gnt.set_yticklabels([f'Machine {i+1}' for i in range(self.num_machines)])

        for task in tasks:
            machine, start, duration, job = task
            gnt.broken_barh([(start, duration)], (machine * 10, 9), facecolors=(f"C{job % 10}"))

        patches = [mpatches.Patch(color=f"C{i % 10}", label=f'Job {i+1}') for i in range(len(self.jobs))]
        plt.legend(handles=patches)
        plt.show()

# Main program
num_jobs, num_machines, jobs = get_jobs_from_user()
ga = JobShopGA(jobs, num_machines)
best_schedule, best_makespan = ga.run()
print("Best Schedule:", best_schedule)
print("Best Makespan:", best_makespan)
ga.create_gantt_chart(best_schedule)
