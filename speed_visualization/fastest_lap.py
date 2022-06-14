# Show the track map colored by speed
# Show the time for the fastest lap
# Create a graph to show the braking
# Show the lowest gear for each coner on the breaking graph
import fastf1 as ff1
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection

ff1.Cache.enable_cache('c:/users/abishek/appdata/local/pip/cache') # optional but recommended


def select_driver_lap_fastest(driver,session):
    """ Returns the fastest lap for a given driver"""
    lap = session.laps.pick_driver(driver).pick_fastest()
    return lap

def get_position_data(lap):
    """ Returns the data for the position on the track """
    x_pos = lap.telemetry['X']      # values for x-axis
    y_pos = lap.telemetry['Y']      # values for y-axis

def main():
    print("Visualistion of the speed on the track for a given driver", end="\n\n")

    colormap = mpl.cm.plasma    
    grand_prix = "Sao Paulo Grand Prix" #input("Select a Grand Prix: ")
    year = int(input("Select a year: "))
    driver = input("Select a driver: ")
    session = input("Select a session, (FP1, FP2, FP3, Q1, Q2, Q3, R): ")

    session = ff1.get_session(year, grand_prix, session)
    session.load()

    lap = select_driver_lap_fastest(driver,session)


main()
