# -*- coding: utf-8 -*-

"""
JBI010: YouTube Trending Videos

Copyright (c) 2020 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.
"""

import datetime
import pytest
from youtube_types import *


# -----------------------------------------
# Task 1
# -----------------------------------------

def test_video() -> None:
    created = True

    try:
        v = Video('Free Guy Trailer 2', 'Ryan Reynolds', datetime.date(2020, 10, 5), datetime.date(2020, 10, 6),
                  ['FreeGuy'], 4673924, 252673, 2499, 20465, [])
    except:
        created = False

    msg = '[Task 1] Cannot create a Video object'
    assert created, msg


def test_video_str() -> None:
    v = Video('Free Guy Trailer 2', 'Ryan Reynolds', datetime.date(2020, 10, 5), datetime.date(2020, 10, 6),
              ['FreeGuy'], 4673924, 252673, 2499, 20465, [])
    expected = 'Free Guy Trailer 2 published by Ryan Reynolds'
    output = str(v)

    msg = f'[Task 1] The string representation of the video is incorrect. Expected: {expected} - Obtained: {output}'
    assert expected.strip().lower() == output.strip().lower(), msg


def test_video_eq() -> None:
    v1 = Video('Free Guy Trailer 2', 'Ryan Reynolds', datetime.date(2020, 10, 5), datetime.date(2020, 10, 6),
              ['FreeGuy'], 4673924, 252673, 2499, 20465, [])
    v2 = Video('Free Guy Trailer 2', 'Ryan Reynolds', datetime.date(2020, 10, 2), datetime.date(2020, 10, 6),
              ['FreeGuy'], 0, 0, 0, 0, [])

    msg = '[Task 1] The output of the __eq__ is incorrect.'
    assert v1 == v2, msg


def test_video_le() -> None:
    v1 = Video('Free Guy Trailer 2', 'Ryan Reynolds', datetime.date(2020, 10, 5), datetime.date(2020, 10, 6),
               ['FreeGuy'], 4673924, 252673, 2499, 20465, [])
    v2 = Video('Free Guy Trailer 2', 'Ryan Reynolds', datetime.date(2020, 10, 2), datetime.date(2020, 10, 6),
               ['FreeGuy'], 0, 0, 0, 0, [])

    msg = '[Task 1] The output of the __ge__ is incorrect.'
    assert v1 <= v2, msg



# -----------------------------------------
# Task 2
# -----------------------------------------

@pytest.mark.parametrize("publish_time, expected",[('2017-11-13T07:30:00.000Z', (2017, 11, 13)),
                                                   ('2017-11-15T18:19:50.000Z', (2017, 11, 15)),
                                                   ('2015-12-14T21:44:29.000Z', (2015, 12, 14)),
                                                   ('2018-01-08T17:00:34.000Z', (2018, 1, 8))])
def test_extract_publish_date(publish_time, expected) -> None:
    publish_date = extract_publish_date(publish_time)

    msg = f'[Task 2] The publish date year is incorrect. Expected: {expected[0]} - Obtained: {publish_date.year}'
    assert publish_date.year == expected[0], msg


@pytest.mark.parametrize("trending_str, expected", [('17.31.01', (2017, 1, 31)), ('18.12.01', (2018, 1, 12)),
                                                    ('18.25.01', (2018, 1, 25)),('18.29.04', (2018, 4, 29))])
def test_extract_trending_date(trending_str, expected) -> None:
    trending_date = extract_trending_date(trending_str)

    msg = f'[Task 2] The trending date year is incorrect. Expected: {expected[0]} - Obtained: {trending_date.year}'
    assert trending_date.year == expected[0], msg


# -----------------------------------------
# Task 3
# -----------------------------------------

@pytest.mark.parametrize("tags_str, expected", [('[none]', []),
                                                ('david guetta|"sia"|"flames"', ['david guetta', 'sia', 'flames']),
                                                ('Mario Dedivanovic|"KKW BEAUTY"|"CONCEALER"', ['mario dedivanovic', 'kkw beauty', 'concealer'])])
def test_extract_tags(tags_str, expected) -> None:
    tags = extract_tags(tags_str)
    msg = f'[Task 3] The tags list is incorrect. Expected: {expected} - Obtained: {tags}'
    assert set(tags) == set(expected), msg


desc1 = "It probably doesn‚Äôt surprise you to hear that I often get asked about the reality of the popular doctor tv shows like Grey‚Äôs Anatomy, House, ER, Good Doctor, Scrubs, etc. In this video, I tackle the most perpetuated tv medical drama myths about working as a doctor in a hospital. It's pretty funny because technically I am a TV doctor because I work in news but I hope to you it's clear I am referring to fictional tv doctors! \n\n\nIf you watch until the end you‚Äôll know that I have never watched a full Grey‚Äôs Anatomy episode and if you guys get this video to 10k likes, I will watch a full episode and record my reactions as a stand-alone YT video! I'll call it Real Doctor Watches Grey's Anatomy! Now go smash those like and share buttons!!! Also, don‚Äôt forget that I will be doing a monthly video reading the comments you leave so go ahead, jump into the comments section. Love you all!\n\n\nSUBSCRIBE for new videos every Sunday ‚ñ∂  https://goo.gl/87kYq6 \n\nLet‚Äôs connect:\n\nIG https://goo.gl/41ZS7w\nTwitter https://goo.gl/kzmGs5\nFacebook https://goo.gl/QH4nJS\n\nContact Email: DoctorMikeMedia@Gmail.com\n\nMusic:\n\nLakey Inspired\nhttps://soundcloud.com/lakeyinspired\n\nJoakim Karud\nhttps://soundcloud.com/joakimkarud"
desc2 = "Jarvis Landry, Michael Thomas, Davante Adams, and Keenan Allen compete in the best hands competition at the 2018 Pro Bowl Skills Showdown.\n\nWatch full games with NFL Game Pass: https://www.nfl.com/gamepass?campaign=sp-nf-gd-ot-yt-3000342\n\nSign up for Fantasy Football! http://www.nfl.com/fantasyfootball\n\nSubscribe to NFL: http://j.mp/1L0bVBu\n\nThe NFL YouTube channel is your home for immediate in-game highlights from your favorite teams and players, full NFL games, behind the scenes access and more!\n\nCheck out our other channels:\nNFL Network http://www.youtube.com/nflnetwork\nNFL Films http://www.youtube.com/nflfilms\n\nFor all things NFL, visit the league's official website at http://www.nfl.com/\n\nWatch NFL Now: https://www.nfl.com/now\nListen to NFL podcasts: http://www.nfl.com/podcasts\nWatch the NFL network: http://nflnonline.nfl.com/\nDownload the NFL mobile app: https://www.nfl.com/apps\n2017 NFL Schedule: http://www.nfl.com/schedules\nBuy tickets to watch your favorite team:  http://www.nfl.com/tickets\nShop NFL: http://www.nflshop.com/source/bm-nflcom-Header-Shop-Tab\n\nLike us on Facebook: https://www.facebook.com/NFL\nFollow us on Twitter: https://twitter.com/NFL\nFollow us on Instagram: https://instagram.com/nfl/\nFind us on Snapchat"
desc3 = "No links to report here"

links1 = ['https://goo.gl/87kYq6', 'https://goo.gl/41ZS7w', 'https://goo.gl/kzmGs5', 'https://goo.gl/QH4nJS',
          'https://soundcloud.com/lakeyinspired', 'https://soundcloud.com/joakimkarud']
links2 = ['https://www.nfl.com/gamepass?campaign=sp-nf-gd-ot-yt-3000342', 'http://www.nfl.com/fantasyfootball', 'http://j.mp/1L0bVBu',
          'http://www.youtube.com/nflnetwork', 'http://www.youtube.com/nflfilms', 'http://www.nfl.com/', 'https://www.nfl.com/now',
          'http://www.nfl.com/podcasts', 'http://nflnonline.nfl.com/', 'https://www.nfl.com/apps', 'http://www.nfl.com/schedules',
          'http://www.nfl.com/tickets', 'http://www.nflshop.com/source/bm-nflcom-Header-Shop-Tab', 'https://www.facebook.com/NFL',
          'https://twitter.com/NFL', 'https://instagram.com/nfl/']
links3 = []


def normalize_link(link: str) -> str:
    if link[len(link) - 1] == '/':
        link = link[:len(link) - 1]

    return link


@pytest.mark.parametrize("description, expected", [(desc1, links1), (desc2, links2), (desc3, links3)])
def test_extract_links(description, expected) -> None:
    links = extract_links(description)

    links = {normalize_link(l) for l in links}
    expected = {normalize_link(e) for e in expected}

    msg = f'[Task 3] The values of the list of links is incorrect. Expected: {expected} - Obtained: {links}'
    assert links == expected, msg