# Genetic Algorithm Optimization

This repository contains a Python script, "genetic_algorithm.py," that implements a genetic algorithm for optimizing a given objective function. The algorithm works with individuals encoded as concatenated pairs of values (x, y), represented by 16-bit fixed-point unsigned integers. The objective function to be maximized is given by:

f(x,y)=(x+y)⋅sin⁡(5⋅(x2+y2))**f**(**x**,**y**)**=**(**x**+**y**)**⋅**sin**(**5**⋅**(**x**2**+**y**2**))

## Problem Description

The problem involves evaluating the fitness of individuals based on the given objective function, recombining individuals with the highest fitness, applying mutation, and determining if the new value should survive to the next generation.

## Importance

Genetic algorithms are optimization techniques inspired by the process of natural selection. They are widely used in various fields to find solutions to complex problems, especially in cases where traditional optimization methods may be impractical or less effective.

## Class Information

This script is part of the assignments for the CPSC 481-05 - Artificial Intelligence course at California State University Fullerton, taught by Professor Kenytt Avery during the Fall 2023 semester.

## Acknowledgment

Special thanks to Professor Kenytt Avery for providing the class with engaging assignments that contribute to a deeper understanding of artificial intelligence concepts.

---
