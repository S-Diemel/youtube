# -*- coding: utf-8 -*-

"""
JBI010: YouTube Trending Videos

Copyright (c) 2020 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.
"""
import numpy
import csv
import statistics
from typing import Iterable, Generator, List, Tuple
from youtube_types import *


def read_dataset(path):
    """
    Reads the dataset and returns a list with Video objects
    """
    # TODO: [Task 4] Define read_dataset
    data = []

    dataset = open(path, encoding='utf-8-sig')
    reader = csv.reader(dataset)
    for line in reader:  # Creates list with lists in it of lines in the dataset
        data.append(line)

    data = data[1:]  # Deletes the first line

    videos_lst = []

    for lst in data: # For loop that create of each line a Video object and adds it to videos_lst
        title = lst[2]
        channel = lst[3]
        publish_date = extract_publish_date(lst[5])
        trending_date = extract_trending_date(lst[1])
        tags = extract_tags(lst[6])
        views = int(lst[7])
        likes = int(lst[8])
        dislikes = int(lst[9])
        comments = int(lst[10])
        links = extract_links(lst[15])
        video = Video(title, channel, publish_date, trending_date, tags,
                      views, likes, dislikes, comments, links)
        videos_lst.append(video)

    return videos_lst


def compute_median_diff_dates(videos):
    """
    Computes the median of days it took before a video reached trending
    """
    # TODO: [Task 5] Define compute_median_diff_dates
    days = [int((video.trending_date - video.publish_date).days) for video in videos]
    median = statistics.median(days)
    return median


def find_viral_videos(videos):
    """
    Creates a list with videos that reached trending in less days than median
    """
    # TODO: [Task 5] Define find_viral_videos
    median = compute_median_diff_dates(videos)
    viral_lst = [video for video in videos if int((video.trending_date - video.publish_date).days) < median]
    return viral_lst


def compute_measures_likes(videos):
    """
    Computes the median, mean and standard deviation of number of likes on videos
    """
    # TODO: [Task 6] Define compute_measures_likes
    likes = [video.likes for video in videos]
    median = int(statistics.median(likes))
    mean = round(statistics.mean(likes), 2)
    stdev = round(statistics.pstdev(likes), 2)
    return median, mean, stdev


def compute_measures_dislikes(videos):
    """
    Computes the median, mean and standard deviation of number of dislikes on videos
    """
    # TODO: [Task 6] Define compute_measures_dislikes
    dislikes = [video.dislikes for video in videos]
    median = int(statistics.median(dislikes))
    mean = round(statistics.mean(dislikes), 2)
    stdev = round(statistics.pstdev(dislikes), 2)
    return median, mean, stdev


def compute_measures_comments(videos):
    """
    Computes the median, mean and standard deviation of number of comments on videos
    """
    # TODO: [Task 6] Define compute_measures_comments
    comments = [video.comments for video in videos]
    median = int(statistics.median(comments))
    mean = round(statistics.mean(comments), 2)
    stdev = round(statistics.pstdev(comments), 2)
    return median, mean, stdev

# hello
