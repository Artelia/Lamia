import numpy as np
import pandas as pd


table_EXF5_6 =
    [
        [1, 1, 1, 1],
        [1, 2, 3, 4],
        [1, 3, 4, 4],
    ]

def compte_exf(node, **kwargs):
    # we start with indicator on T, estimator for BV will be develop later
    estimator = {}
    # EXF1-O-BV is on BV
    # EXF2-E/R-T depend of observation or estimation, if over "radier" = 1, if "radier" or unknows = 2, if under "radier" = 3
    estimation["EXF2"] = kwargs.get("EXF2", 2)
    # EXF3-O-T not often measured
    if not kwargs.get("EXF3", None):
        estimation["EXF3"] = kwargs.get("EXF2", None)
    elif kwargs.get("EXF3", None) > 10:
        estimation["EXF3"] = 4
    elif kwargs.get("EXF3", None) > 5:
        estimation["EXF3"] = 3
    elif kwargs.get("EXF3", None) > 2:
        estimation["EXF3"] = 2
    else:
        estimation["EXF3"] = 1
    # EXF4-E/O-T is on T
    P = 5
    alpha = 0.2
    LT = kwargs.get("longueur_troncon", 100)
    N = 0
    # loop on deformation
        # if BABB, BAFA, BAFC, BAFD, BAFE, BAFF, BAFG, BAFH, BAIZ, BAN add total observated_length
        # if BAA, BADA, BAE add nb_observation * P * alpha
        # if BABC, BAFB add observated_length * alpha ** 2
        # if BACA, BADB, BADC, BAHB, BAHC, BAHD, BAIA, BAI#, BAJ, BBA, BBBA add nb_observation * P * alpha ** 2
        # if BAFI, BAFZ add observated_length * alpha ** 3
        # if BACB, BACC, BADD, BAO, BAP add nb_observation * P * alpha ** 3
        # == N
    D = N / LT
    S1 = 0.5
    S2 = 2.
    S3 = 7.
    if not D <= S1:
        estimation["EXF4"] = 1
    elif not D <= S2:
        estimation["EXF4"] = 2
    elif not D <= S3:
        estimation["EXF4"] = 3
    else:
        estimation["EXF4"] = 4
    # EXF5-C-T is on T
    if not kwargs.get("EDS-E-T", None) or not estimation["EXF2"]:
        estimation["EXF5"] = None
    else:
        estimation["EXF5"] = table_EXF5_6[int(estimation["EXF5"]), int(kwargs.get("EDS-E-T", None))]
    # EXF5-E/O-T is on T
    if not estimation["EXF2"] or not estimation["EXF4"]:
        estimation["EXF6"] = None
    else:
        estimation["EXF6"] = table_EXF5_6[int(estimation["EXF2"]), int(estimation["EXF4"])]
    # EXF7-C-T is on T
    if not estimation["EXF5"]:
        estimation["EXF7"] = None
    elif not estimation["EXF1"] or not estimation["EXF3"] or np.nanmin((estimation["EXF1"], estimation["EXF3"], 0)) <= 2:
        estimation["EXF7"] = estimation["EXF5"]
    else:
        estimation["EXF7"] = np.min((estimation["EXF5"] + 1, 4))
    # EXF8-C-T is on T
    if not estimation["EXF6"]:
        estimation["EXF8"] = None
    elif not estimation["EXF1"] or not estimation["EXF3"] or np.nanmin((estimation["EXF1"], estimation["EXF3"], 0)) <= 2:
        estimation["EXF8"] = estimation["EXF6"]
    else:
        estimation["EXF8"] = np.min((estimation["EXF6"] + 1, 4))
    node.estimation["EXF"] = estimation