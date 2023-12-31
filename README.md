# Projectile Simulation
Simulates the trajectory of a projectile in real-time.

**Author:** Edwin Wagha (me)

**Dependencies:** Python, Matplotlib

## Class: Projectile
- Represents a projectile with speed, launch angle, and height.
- Calculates position, velocity, drag force, and acceleration due to drag.

## Function: plot_trajectory_realtime
- Plots the trajectory of the projectile.

## Usage:
1. Run the script.
2. Enter initial speed, launch angle, and initial height.
3. Watch the real-time plot of the projectile's trajectory.

**Note:** Adjust the plotting range based on the projectile's maximum range.

## Error with matplpotlib

 - If you encounter an error with matplotlib
 **ImportError: DLL load failed while importing _cext: The specified module could not be found**

 - Execute the following in your terminal: **pip install msvc-runtime**



![Simulation Preview](image.png)
