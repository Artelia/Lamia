#!/usr/bin/env python
#coding:utf-8
# Purpose:
# Created: 27.03.2010

__author__ = "mozman <mozman@gmx.at>"

import math

HALF_PI = math.pi / 2.
THREE_PI_HALF = 1.5 * math.pi
DOUBLE_PI = math.pi * 2.

def rotate_2d(point, angle):
    """ rotate point around origin point about angle """
    x = point[0] * math.cos(angle) - point[1] * math.sin(angle)
    y = point[1] * math.cos(angle) + point[0] * math.sin(angle)
    return (x, y)

def equals_almost(v1, v2, places=7):
    """compare two float values
       places: significant decimal places
    """
    return round(v1, places) == round(v2, places)

def normalize_angle(angle):
    """ return an angle between 0 and 2*pi """
    angle = math.fmod(angle, DOUBLE_PI)
    if angle < 0:
        angle += DOUBLE_PI
    return angle

def is_vertical_angle(angle, places=7):
    """ returns True for 1/2pi and 3/2pi """
    angle = normalize_angle(angle)
    return (equals_almost(angle, HALF_PI, places) or
            equals_almost(angle, THREE_PI_HALF, places))

def get_angle(p1, p2):
    """calc angle between the line p1-p2 and the x-axis
    input: points as tuples
    result: angle in radians
    """
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return math.atan2(dy, dx)

def right_of_line(point, p1, p2):
    """ True if the point self is right of the line p1 -> p2
    """
    return not left_of_line(point, p1, p2)

def left_of_line(point, p1, p2):
    """ True if the point self is left of the line p1 -> p2
    """
    # check if a and b are on the same vertical line
    if p1[0] == p2[0]:
        # compute # on which site of the line self should be
        should_be_left = p1[1] < p2[1]
        if should_be_left:
            return point[0] < p1[0]
        else:
            return point[0] > p1[0]
    else:
        # get pitch of line
        pitch = (p2[1] - p1[1]) / (p2[0] - p1[0])

        # get y-value at c's x-position
        y = pitch * (point[0] - p1[0]) + p1[1]

        # compute if point should be above or below the line
        should_be_above = p1[0] < p2[0]
        if should_be_above :
            return point[1] > y
        else:
            return point[1] < y
