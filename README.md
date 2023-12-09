# Genetic Algorithm Optimization

This repository contains Python scripts related to optimizing a specific
 objective function using a genetic algorithm. The optimization process
involves individuals encoded as concatenated pairs of values (x, y),
where each value is a 16-bit fixed-point unsigned integer. The objective
 function to maximize is defined as:

#### **f(x, y) = (x + y) * sin(5 * (x^2 + y^2))**


## Problem Description

The problem involves evaluating the fitness of individuals based on the given objective function, recombining individuals with the highest fitness, applying mutation, and determining if the new value should survive to the next generation.

## Importance

Genetic algorithms are optimization techniques inspired by the process of natural selection. They are widely used in various fields to find solutions to complex problems, especially in cases where traditional optimization methods may be impractical or less effective.

## Class Information

This script is part of the assignments for the CPSC 481-05 - Artificial Intelligence course at California State University Fullerton, taught by Professor Kenytt Avery during the Fall 2023 semester.



The repository includes the following scripts:

* `genetic_algorithm.py`: Python script implementing the genetic algorithm for optimizing the objective function.
* `mutation_decisions.txt`: Set of mutation decisions for each bit in the individual.

## Initial Population

The most fit individuals from the current population are:

1. `01001100010110010110010010001000`
2. `00010100110110110100100010001010`
3. `10110101001101100000111110011100`
4. `01010010011000100010000100011001`
5. `11000111000100001110011110100111`

## Fitness Evaluation

The fitness of each individual is evaluated based on the objective function.

## Recombination

The two individuals with the highest fitness are recombined at crossover point 13 to generate a new individual.

## Mutation

A mutation rate of 0.05 is applied to the new individual based on the decisions in `mutation_decisions.txt`.

## Evaluate New Offspring

The fitness of the new offspring is then evaluated to determine if it should survive to the next generation.

## Getting Started

### Prerequisites

* Python 3.x

### Usage

1. Clone the repository:

```bash
git clone https://github.com/abelxmendoza/GeneticAlgorithm-Optimization.git
```

2. Navigate to the repository:

```bash
cd GeneticAlgorithm-Optimization
```

3. Run the genetic algorithm script:

```bash
python3 genetic_algorithm.py
```

## Contributing

If you have suggestions or improvements, feel free to open an issue or create a pull request. Contributions are welcome!

## Acknowledgment

I would like to express my sincere gratitude to Professor Kenytt Avery for teaching CPSC 481-05 - Artificial Intelligence at California State University Fullerton. This exercise has provided valuable insights into genetic algorithms and optimization in the field of artificial intelligence.

Thank you, Professor Avery, for your guidance and support throughout this exercise.

## Documentation

[https://docs.google.com/document/d/1h4M-IueEFTKt-olsMWisFFHuS9oMp9TwNNQRK9h1DY0/edit?usp=sharing](https://docs.google.com/document/d/1h4M-IueEFTKt-olsMWisFFHuS9oMp9TwNNQRK9h1DY0/edit?usp=sharing)

---

![1702155953553](image/README/1702155953553.png)
