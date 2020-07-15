#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "Areiahna Cooks, https://stackoverflow.com/questions/19010793/how-to-use-timeit-when-timing-a-function"

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    # Be sure to review the lesson material on decorators.
    # You need to understand how they are constructed and used.
    raise NotImplementedError("Complete this decorator function")


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Returns True if title is within movies list."""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    t = timeit.Timer('main()', 'from __main__ import main')
    averages = t.repeat(repeat=3, number=7)
    minimun = 0
    big = 0
    for average in averages:
        if average > big:
            big = average
        else:
            minimun = average
    print(averages)
    print(minimun)


def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))


if __name__ == '__main__':

    timeit_helper()
