#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utilities for acceleration
"""
from UliEngineering.EngineerIO import normalize_numeric
from UliEngineering.Units import Unit
import numpy as np
import scipy.constants

__all__ = ["rpm_to_Hz", "rpm_to_rps", "hz_to_rpm", "angular_speed",
           "rotation_linear_speed", "centrifugal_force"]

def rpm_to_Hz(rpm) -> Unit("Hz"):
    """
    Compute the rotational speed in Hz given the rotational speed in rpm
    """
    rpm = normalize_numeric(rpm)
    return rpm / 60.

def hz_to_rpm(hz) -> Unit("rpm"):
    """
    Compute the rotational speed in rpm given the rotational speed in Hz
    """
    hz = normalize_numeric(hz)
    return hz * 60.

rpm_to_rps = rpm_to_Hz

def angular_speed(speed: Unit("Hz")) -> Unit("1/s"):
    """
    Compute ω, the angular speed of a centrifugal system
    """
    speed = normalize_numeric(speed)
    return 2*np.pi*speed

def rotation_linear_speed(radius: Unit("m"), speed: Unit("Hz")) -> Unit("m/s"):
    """
    Compute the linear speed at a given [radius] for a centrifugal system rotating at [speed].
    """
    radius = normalize_numeric(radius)
    return radius * angular_speed(speed)

def centrifugal_force(radius: Unit("m"), speed: Unit("Hz"), mass: Unit("g")) -> Unit("N"):
    """
    Compute the centrifugal force of a [mass] rotation at [speed] at radius [radius]
    """
    radius = normalize_numeric(radius)
    mass = normalize_numeric(mass) / 1000.0 # mass needs to be Kilograms TODO Improve
    return mass * angular_speed(speed)**2 * radius