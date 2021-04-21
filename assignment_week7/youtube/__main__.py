# -*- coding: utf-8 -*-

"""
JBI010: YouTube Trending Videos

Copyright (c) 2020 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.

* Author: Stijn Diemel
* TU/e ID number: 1645749
* Date: 2020-10-14
"""

from youtube_core import *
from youtube_utils import *


path = get_absolute_path('data/youtube-trends-us.csv')
videos = read_dataset(path)


def show_menu() -> None:
    """
    Prints the menu of the command-line program.
    """
    print('Welcome to the YouTube Trending Videos program!')
    print('The program offers the following options:\n')
    print('0- Display options again')
    print('1- Compute median of days between publication and trend')
    print('2- Find viral videos')
    print('3- Compute statistics for number of likes')
    print('4- Compute statistics for number of dislikes')
    print('5- Compute statistics for number of comments')
    print('6 - Exit the YouTube Trending Videos Program\n')


def option1() -> None:
    """
    Computes the median days between the publication and
    trend of all videos.
    """
    median = compute_median_diff_dates(videos)
    print(f'Median days between publication and trend: {median}')


def option2() -> None:
    """
    Prints the string representation of all viral videos.
    """
    print('List of viral videos:')
    viral = find_viral_videos(videos)

    for v in viral:
        print(str(v))

    print()
    print(f'Found {len(viral)} viral videos out of {len(videos)}')


def print_measures(measures: Tuple) -> None:
    """
    Prints the median, mean and standard deviation by extracting
    them from the tuple received as parameter.
    :param measures: tuple of three elements: median, mean and stdev
    """
    median, mean, stdev = measures
    print(f'Median: {median}')
    print(f'Mean: {mean}')
    print(f'Standard Deviation: {stdev}')


def option3() -> None:
    """
    Prints central tendency and variability measures related
    to the number of likes of trending videos.
    """
    print('Likes stats:')
    measures = compute_measures_likes(videos)
    print_measures(measures)


def option4() -> None:
    """
    Prints central tendency and variability measures related
    to the number of dislikes of trending videos.
    """
    print('Dislikes stats:')
    measures = compute_measures_dislikes(videos)
    print_measures(measures)


def option5() -> None:
    """
    Prints central tendency and variability measures related
    to the number of comments of trending videos.
    """
    print('Comments stats:')
    measures = compute_measures_comments(videos)
    print_measures(measures)

def option6() -> None:
    """
    Exits the YouTube Trending Video Program.
    """
    raise SystemExit


def request_input() -> None:
    """
    Requests the user to enter an option between 0 and 5.
    """
    option = input('Enter the number of your option: ')
    msg_err = 'Please, enter an option between 0 and 5.'

    try:
        option = int(option)
        switcher = {
            0: show_menu,
            1: option1,
            2: option2,
            3: option3,
            4: option4,
            5: option5,
            6: option6
        }

        func = switcher.get(option, lambda: msg_err)
        func()
        print('')

    except ValueError:
        print(msg_err)


if __name__ == '__main__':
    show_menu()

    while True:
        request_input()

