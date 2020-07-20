#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "Areiahna Cooks, Facilitator JT, SE Coach Ybrayym, https://stackoverflow.com/questions/19010793/how-to-use-timeit-when-timing-a-function, https://www.w3schools.com/python/python_howto_remove_duplicates.asp"

import cProfile
import pstats
import functools
import timeit
import re


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    def performance_measurement(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        results = func(*args, **kwargs)
        pr.disable()
        stats = pstats.Stats(pr).sort_stats('cumulative')
        stats.print_stats()
        return results
    return performance_measurement


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    movies = [movie.lower() for movie in movies]
    movies.sort()
    duplicates = [movie1 for movie1, movie2 in zip(
        movies[:-1], movies[1:])if movie1 == movie2]
    return duplicates


def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    t = timeit.Timer(stmt='find_duplicate_movies("movies.txt")',
                     setup='from __main__ import find_duplicate_movies')
    total_repeats = t.repeat(repeat=7, number=3)

    average = min(total_repeats)/float(3)

    return f'Best time across 7 repeats of 3 runs per repeat: {average}'


def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))
    print(timeit_helper())


if __name__ == '__main__':
    main()
