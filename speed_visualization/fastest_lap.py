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

def main():
    print("Visualistion of the speed on the track for a given driver", end="\n\n")

    colormap = mpl.cm.plasma    
    grand_prix = "Sao Paulo Grand Prix" #input("Select a Grand Prix: ")
    year = 2021                         #int(input("Select a year: "))
    driver = "HAM"                      #input("Select a driver: ")
    session = "R"                       #input("Select a session, (FP1, FP2, FP3, Q1, Q2, Q3, R): ")

    session = ff1.get_session(year, grand_prix, session)
    session.load()

    lap = select_driver_lap_fastest(driver,session)

    x_pos = lap.telemetry['X']      # values for x-axis
    y_pos = lap.telemetry['Y'] 
    tack_color = lap.telemetry['Speed']
    
    
    pos_array = np.array([x_pos, y_pos]) #Create a numpy array of the positions
    points = pos_array.T.reshape(-1, 1, 2) #Reshape the array to be (numlines) x (points per line) x 2 (for x and y)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

main()

