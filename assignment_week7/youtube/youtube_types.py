# -*- coding: utf-8 -*-

"""
JBI010: YouTube Trending Videos

Copyright (c) 2020 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.
"""

import datetime
import re
from typing import List, Tuple


# TODO: [Task 1] Define class Video
class Video:
    """
    represents a Youtube video
    """

    def __init__(self, title: str, channel: str, publish_date: datetime.date, trending_date: datetime.date,
                 tags: list, views: int, likes: int, dislikes: int, comments: int, links: list):
        """
        Creates a new Video object and initializes it
        """
        self.title = title
        self.channel = channel
        self.publish_date = publish_date
        self.trending_date = trending_date
        self.tags = tags
        self.views = views
        self.likes = likes
        self.dislikes = dislikes
        self.comments = comments
        self.links = links

    def __str__(self):
        """
        Creates a string of title and channel of a Video object
        """
        return f'{self.title} published by {self.channel}'

    def __eq__(self, other) -> bool:
        """
        Look whether the title of a Video object is equal to with something else
        """
        return self.title == other

    def __ge__(self, other) -> bool:
        """
        Look whether the title of a Video object is equal or greater than something else
        """
        return self.title >= other

    def __gt__(self, other) -> bool:
        """
        Look whether the title of a Video object is greater than with something else
        """
        return self.title > other

    def __le__(self, other) -> bool:
        """
        Look whether the title of a Video object is equal or less than with something else
        """
        return self.title <= other

    def __lt__(self, other) -> bool:
        """
        Look whether the title of a Video object is less than with something else
        """
        return self.title < other

    def __ne__(self, other) -> bool:
        """
        Look whether the title of a Video object is not equal to with something else
        """
        return self.title != other


def extract_publish_date(publish_time):
    """
    Finds numbers of a publish date in a string and converges it into a datetime object
    """
    # TODO: [Task 2] Define extract_publish_date
    year = int(re.findall('(\d+)-', publish_time)[0])
    month = int(re.findall('(\d+)-', publish_time)[1])
    day = int(re.findall('(\d+)T', publish_time)[0])
    date = datetime.date(year, month, day)
    return date


def extract_trending_date(trending_date):
    """
    Finds numbers of a trending date in a string and converges it into a datetime object
    """
    # TODO: [Task 2] Define extract_trending_date
    year = 2000 + int(re.findall('(\d+)\.', trending_date)[0])
    day = int(re.findall('(\d+)\.', trending_date)[1])
    month = int(re.findall('\.(\d+)', trending_date)[1])
    date = datetime.date(year, month, day)
    return date


def extract_tags(tags_str):
    """
    Finds tags in a string and converges them into a list
    """
    # TODO: [Task 3] Define extract_tags
    if tags_str == '[none]':
        return []
    else:
        tags_lst_upper = re.findall('([^\|\"]+)', tags_str)

        tags_lst_lower = []

        for tag in tags_lst_upper: # For loop that makes the tags lowercase
            lower_tag = tag.lower()
            tags_lst_lower.append(lower_tag)
        return tags_lst_lower


def extract_links(description):
    """
    Finds all links in a description string
    """
    # TODO: [Task 3] Define extract_links
    links_lst = re.findall('http\S+', description)
    return links_lst
