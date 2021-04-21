# -*- coding: utf-8 -*-

"""
JBI010: YouTube Trending Videos

Copyright (c) 2020 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.
"""

import csv
import pytest
import random
from typing import List
from youtube_core import *
from youtube_types import Video
from youtube_utils import *


@pytest.fixture
def dataset() -> List[Video]:
    path = get_absolute_path('data/youtube-trends-us.csv')
    videos = read_dataset(path)
    return videos

@pytest.fixture
def items() -> List[Tuple[str, str]]:
    items = list()
    path = get_absolute_path('data/youtube-trends-us.csv')

    with open(path, encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)

        for row in reader:
            title = row['title']
            channel = row['channel_title']
            tup = (title, channel)
            items.append(tup)

    return items

# -----------------------------------------
# Task 4
# -----------------------------------------


def test_read_dataset_length(dataset) -> None:
    expected = 40949
    output = len(dataset)

    msg = f'[Task 4] The length of the dataset is incorrect. Expected: {expected} - Obtained: {output}'
    assert expected == output, msg


def test_read_dataset(dataset, items) -> None:
    videos = list()

    for v in dataset:
        tup = (v.title, v.channel)
        videos.append(tup)

    msg = f'[Task 4] The content of the dataset is incorrect.'
    assert set(items) == set(videos), msg


# -----------------------------------------
# Task 5
# -----------------------------------------


def test_compute_median_diff_dates(dataset) -> None:
    output = compute_median_diff_dates(dataset)
    expected = 5

    msg = f'[Task 5] The median day between publication and trend is incorrect. Expected: {expected} - Obtained: {output}'
    assert output == expected, msg


def test_find_viral_videos_length(dataset) -> None:
    output = len(find_viral_videos(dataset))
    expected = 16608

    msg = f'[Task 5] The number of viral videos is incorrect. Expected: {expected} - Obtained: {output}'
    assert output == expected, msg


# -----------------------------------------
# Task 6
# -----------------------------------------


def test_compute_measures_likes(dataset) -> None:
    median, mean, stdev = compute_measures_likes(dataset)
    expected = (18091, 74266.7, 228885.34)

    msg = f'[Task 6] The median number of likes is incorrect. Expected: {expected[0]} - Obtained: {median}'
    assert median == expected[0], msg


def test_compute_measures_dislikes(dataset) -> None:
    median, mean, stdev = compute_measures_dislikes(dataset)
    expected = (631, 3711.4, 29029.71)

    msg = f'[Task 6] The median number of dislikes is incorrect. Expected: {expected[0]} - Obtained: {median}'
    assert median == expected[0], msg


def test_compute_measures_comments(dataset) -> None:
    median, mean, stdev = compute_measures_comments(dataset)
    expected = (1856, 8446.8, 37430.49)

    msg = f'[Task 6] The median number of comments is incorrect. Expected: {expected[0]} - Obtained: {median}'
    assert median == expected[0], msg

