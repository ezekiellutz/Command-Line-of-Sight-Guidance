# -*- coding: utf-8 -*-
"""
@date: Friday, December 9th, 2022
@author: Ezekiel Zechariah Lutz
@time: 15:43:32
"""

""""""""""""""""""""""""""""""""""""
"""           Libraries          """
""""""""""""""""""""""""""""""""""""
import pandas as pd
import math
import matplotlib.pyplot as plt

""""""""""""""""""""""""""""""""""""
"""            Lists             """
""""""""""""""""""""""""""""""""""""

                                                 # Creates empty lists to hold parameters of interest that will be appended later on in the code . 
list_missile_position_z = []
list_missile_position_x = []
list_missile_velocity_z = []
list_missile_velocity_x = []
list_target_position_z = []
list_target_position_x = []
list_target_velocity_z = []
list_target_velocity_x = []
list_time_since_launch= []
list_missile_heading_angle = []

""""""""""""""""""""""""""""""""""""
"""     Engagement Parameters    """
""""""""""""""""""""""""""""""""""""

engagement_duration  = 120                       # Duration of the engagement, units in seconds.
dt = 0.1                                         # Delta Time (dt), represents update rate of engagement, units in seconds.
total_updates = int(engagement_duration/dt)      # Total number of updates/data points for the engagement.


""""""""""""""""""""""""""""""""""""
"""      Initial Parameters      """
""""""""""""""""""""""""""""""""""""
 
missile_position_x = 1                           # Position of the missile in the x-axis (range) relative to the surface-to-air missile launcher, units in kilometers.
missile_position_z = 1                           # Position of the missile in the z-axis (altitude) relative to the surface-to-air missile launcher, units in kilometers.
missile_velocity = 0.411                         # Total magnitude of the missile's velocity vector, units in kilometers/second.
target_position_x = 7                            # Position of the target in the x-axis (range) relative to the surface-to-air missile launcher, units in kilometers.
target_position_z = 7                            # Position of the target in the z-axis (altitude) relative to the surface-to-air missile launcher, units in kilometers.                       
target_velocity_x = 0.343                        # Target velocity in the x-axis (range), units in kilometers/second.
target_velocity_z = -0.006                       # Target velocity in the z-axis (altitude), units in kilometers/second.
time_since_launch = 0                            # Time since missile launch, units in seconds.

for i in range(100):
    
    time_since_launch = time_since_launch + dt                      # Updates the time since launch by the update rate, units in seconds.

    relative_position_x = target_position_x - missile_position_x    # Calculates the position of the target relative to the missile in the x-axis (range), units in kilometers.
    relative_position_z = target_position_z - missile_position_z    # Calculates the position of the target relative to the missile in the z-axis (altitude), units in kilometers.

    phi_m = math.atan2(relative_position_z, relative_position_x)    # Calculates the angle between the line-of-sight between the missile and the target and the velocity vector of the missile, units in radians.

    missile_velocity_x = missile_velocity * math.cos(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the x-axis, units in kilometers/second.
    missile_velocity_z = missile_velocity * math.sin(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the z-axis, units in kilometers/second.

    target_position_x = target_position_x + target_velocity_x*dt    # Updates the position of the target in the x-axis based on the velocity change above, units in kilometers.    
    target_position_z = target_position_z + target_velocity_z*dt    # Updates the position of the target in the z-axis based on the velocity change above, units in kilometers.

    missile_position_z = missile_position_z + missile_velocity_z*dt # Updates the position of the missile in the x-axis based on the velocity change above, units in kilometers.    
    missile_position_x = missile_position_x + missile_velocity_x*dt # Updates the position of the missile in the z-axis based on the velocity change above, units in kilometers.    
    
                                                  # The following section appends their corresponding lists with the value for several parameters of interest for each iteration. 
    
    list_missile_position_z.append(missile_position_z)
    list_missile_position_x.append(missile_position_x)
    list_missile_velocity_z.append(missile_velocity_z)
    list_missile_velocity_x.append(missile_velocity_x)
    list_target_position_z.append(target_position_z)
    list_target_position_x.append(target_position_x)
    list_target_velocity_z.append(target_velocity_z)
    list_target_velocity_x.append(target_velocity_x)
    list_missile_heading_angle.append(phi_m)
    list_time_since_launch.append(time_since_launch)
    
    closing_distance = ((relative_position_x)**2 + (relative_position_z)**2)**0.5  # Calculates the closing distance between the missile and the target, units in kilometers.
    
    detonate = math.isclose(closing_distance, 0, abs_tol=0.1)      # Performs a check before each new iteration to see if the closing distance from the missile to the target is less than 100 meters. Returns a boolean variable (either 'TRUE' or 'FALSE').
    
    if detonate == True:                                           # If the distance between the missile and the target is within 100 meters, the missile "detonates" and the simulation ends.   
        print("BOOM!")
        break


"""
NOTE ON THE FOLLOWING SECTION:
    
The following section of code repeats the alogrithm in iterations of 100 (roughly 10 second sections of time) until detonation is reached.

This is done in an effort to illustrate how command-line-of-sight (CLOS) guidance always has its velocity vector pointing towards the 
target, and has the effect of having the missile "follow" the target and intercepts it in a highly reactive, rather than proactive, manner.

This "breaking-up" of the code is not needed if the target moves in a linear way, because the velocity of the target doesn't change over time.
The effects of CLOS are more difficult to observe and understand with linear motion, and are more apparent in non-linear motion. 

"""





target_velocity_z = 0.003       # Updates the velocity of the target in the z-axis, units in kilometers/second.

for i in range(100):
    
    time_since_launch = time_since_launch + dt                      # Updates the time since launch by the update rate, units in seconds.

    relative_position_x = target_position_x - missile_position_x    # Calculates the position of the target relative to the missile in the x-axis (range), units in kilometers.
    relative_position_z = target_position_z - missile_position_z    # Calculates the position of the target relative to the missile in the z-axis (altitude), units in kilometers.

    phi_m = math.atan2(relative_position_z, relative_position_x)    # Calculates the angle between the line-of-sight between the missile and the target and the velocity vector of the missile, units in radians.

    missile_velocity_x = missile_velocity * math.cos(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the x-axis, units in kilometers/second.
    missile_velocity_z = missile_velocity * math.sin(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the z-axis, units in kilometers/second.

    target_position_x = target_position_x + target_velocity_x*dt    # Updates the position of the target in the x-axis based on the velocity change above, units in kilometers.    
    target_position_z = target_position_z + target_velocity_z*dt    # Updates the position of the target in the z-axis based on the velocity change above, units in kilometers.

    missile_position_z = missile_position_z + missile_velocity_z*dt # Updates the position of the missile in the x-axis based on the velocity change above, units in kilometers.    
    missile_position_x = missile_position_x + missile_velocity_x*dt # Updates the position of the missile in the z-axis based on the velocity change above, units in kilometers.    
    
                                                  # The following section appends their corresponding lists with the value for several parameters of interest for each iteration. 
    
    list_missile_position_z.append(missile_position_z)
    list_missile_position_x.append(missile_position_x)
    list_missile_velocity_z.append(missile_velocity_z)
    list_missile_velocity_x.append(missile_velocity_x)
    list_target_position_z.append(target_position_z)
    list_target_position_x.append(target_position_x)
    list_target_velocity_z.append(target_velocity_z)
    list_target_velocity_x.append(target_velocity_x)
    list_missile_heading_angle.append(phi_m)
    list_time_since_launch.append(time_since_launch)
    
    closing_distance = ((relative_position_x)**2 + (relative_position_z)**2)**0.5  # Calculates the closing distance between the missile and the target, units in kilometers.
    
    detonate = math.isclose(closing_distance, 0, abs_tol=0.1)      # Performs a check before each new iteration to see if the closing distance from the missile to the target is less than 100 meters. Returns a boolean variable (either 'TRUE' or 'FALSE').
    
    if detonate == True:                                           # If the distance between the missile and the target is within 100 meters, the missile "detonates" and the simulation ends.   
        print("BOOM!")
        break


"""
NOTE ON THE FOLLOWING SECTION:
    
The following section of code repeats the alogrithm in iterations of 100 (roughly 10 second sections of time) until detonation is reached.

This is done in an effort to illustrate how command-line-of-sight (CLOS) guidance always has its velocity vector pointing towards the 
target, and has the effect of having the missile "follow" the target and intercepts it in a highly reactive, rather than proactive, manner.

This "breaking-up" of the code is not needed if the target moves in a linear way, because the velocity of the target doesn't change over time.
The effects of CLOS are more difficult to observe and understand with linear motion, and are more apparent in non-linear motion. 

"""





target_velocity_z = 0.005       # Updates the velocity of the target in the z-axis, units in kilometers/second.

for i in range(100):
    
    time_since_launch = time_since_launch + dt                      # Updates the time since launch by the update rate, units in seconds.

    relative_position_x = target_position_x - missile_position_x    # Calculates the position of the target relative to the missile in the x-axis (range), units in kilometers.
    relative_position_z = target_position_z - missile_position_z    # Calculates the position of the target relative to the missile in the z-axis (altitude), units in kilometers.

    phi_m = math.atan2(relative_position_z, relative_position_x)    # Calculates the angle between the line-of-sight between the missile and the target and the velocity vector of the missile, units in radians.

    missile_velocity_x = missile_velocity * math.cos(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the x-axis, units in kilometers/second.
    missile_velocity_z = missile_velocity * math.sin(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the z-axis, units in kilometers/second.

    target_position_x = target_position_x + target_velocity_x*dt    # Updates the position of the target in the x-axis based on the velocity change above, units in kilometers.    
    target_position_z = target_position_z + target_velocity_z*dt    # Updates the position of the target in the z-axis based on the velocity change above, units in kilometers.

    missile_position_z = missile_position_z + missile_velocity_z*dt # Updates the position of the missile in the x-axis based on the velocity change above, units in kilometers.    
    missile_position_x = missile_position_x + missile_velocity_x*dt # Updates the position of the missile in the z-axis based on the velocity change above, units in kilometers.    
    
                                                  # The following section appends their corresponding lists with the value for several parameters of interest for each iteration. 
    
    list_missile_position_z.append(missile_position_z)
    list_missile_position_x.append(missile_position_x)
    list_missile_velocity_z.append(missile_velocity_z)
    list_missile_velocity_x.append(missile_velocity_x)
    list_target_position_z.append(target_position_z)
    list_target_position_x.append(target_position_x)
    list_target_velocity_z.append(target_velocity_z)
    list_target_velocity_x.append(target_velocity_x)
    list_missile_heading_angle.append(phi_m)
    list_time_since_launch.append(time_since_launch)
    
    closing_distance = ((relative_position_x)**2 + (relative_position_z)**2)**0.5  # Calculates the closing distance between the missile and the target, units in kilometers.
    
    detonate = math.isclose(closing_distance, 0, abs_tol=0.1)      # Performs a check before each new iteration to see if the closing distance from the missile to the target is less than 100 meters. Returns a boolean variable (either 'TRUE' or 'FALSE').
    
    if detonate == True:                                           # If the distance between the missile and the target is within 100 meters, the missile "detonates" and the simulation ends.   
        print("BOOM!")
        break


"""
NOTE ON THE FOLLOWING SECTION:
    
The following section of code repeats the alogrithm in iterations of 100 (roughly 10 second sections of time) until detonation is reached.

This is done in an effort to illustrate how command-line-of-sight (CLOS) guidance always has its velocity vector pointing towards the 
target, and has the effect of having the missile "follow" the target and intercepts it in a highly reactive, rather than proactive, manner.

This "breaking-up" of the code is not needed if the target moves in a linear way, because the velocity of the target doesn't change over time.
The effects of CLOS are more difficult to observe and understand with linear motion, and are more apparent in non-linear motion. 

"""





target_velocity_z = 0.006       # Updates the velocity of the target in the z-axis, units in kilometers/second.

for i in range(100):
    
    time_since_launch = time_since_launch + dt                      # Updates the time since launch by the update rate, units in seconds.

    relative_position_x = target_position_x - missile_position_x    # Calculates the position of the target relative to the missile in the x-axis (range), units in kilometers.
    relative_position_z = target_position_z - missile_position_z    # Calculates the position of the target relative to the missile in the z-axis (altitude), units in kilometers.

    phi_m = math.atan2(relative_position_z, relative_position_x)    # Calculates the angle between the line-of-sight between the missile and the target and the velocity vector of the missile, units in radians.

    missile_velocity_x = missile_velocity * math.cos(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the x-axis, units in kilometers/second.
    missile_velocity_z = missile_velocity * math.sin(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the z-axis, units in kilometers/second.

    target_position_x = target_position_x + target_velocity_x*dt    # Updates the position of the target in the x-axis based on the velocity change above, units in kilometers.    
    target_position_z = target_position_z + target_velocity_z*dt    # Updates the position of the target in the z-axis based on the velocity change above, units in kilometers.

    missile_position_z = missile_position_z + missile_velocity_z*dt # Updates the position of the missile in the x-axis based on the velocity change above, units in kilometers.    
    missile_position_x = missile_position_x + missile_velocity_x*dt # Updates the position of the missile in the z-axis based on the velocity change above, units in kilometers.    
    
                                                  # The following section appends their corresponding lists with the value for several parameters of interest for each iteration. 
    
    list_missile_position_z.append(missile_position_z)
    list_missile_position_x.append(missile_position_x)
    list_missile_velocity_z.append(missile_velocity_z)
    list_missile_velocity_x.append(missile_velocity_x)
    list_target_position_z.append(target_position_z)
    list_target_position_x.append(target_position_x)
    list_target_velocity_z.append(target_velocity_z)
    list_target_velocity_x.append(target_velocity_x)
    list_missile_heading_angle.append(phi_m)
    list_time_since_launch.append(time_since_launch)
    
    closing_distance = ((relative_position_x)**2 + (relative_position_z)**2)**0.5  # Calculates the closing distance between the missile and the target, units in kilometers.
    
    detonate = math.isclose(closing_distance, 0, abs_tol=0.1)      # Performs a check before each new iteration to see if the closing distance from the missile to the target is less than 100 meters. Returns a boolean variable (either 'TRUE' or 'FALSE').
    
    if detonate == True:                                           # If the distance between the missile and the target is within 100 meters, the missile "detonates" and the simulation ends.   
        print("BOOM!")
        break


"""
NOTE ON THE FOLLOWING SECTION:
    
The following section of code repeats the alogrithm in iterations of 100 (roughly 10 second sections of time) until detonation is reached.

This is done in an effort to illustrate how command-line-of-sight (CLOS) guidance always has its velocity vector pointing towards the 
target, and has the effect of having the missile "follow" the target and intercepts it in a highly reactive, rather than proactive, manner.

This "breaking-up" of the code is not needed if the target moves in a linear way, because the velocity of the target doesn't change over time.
The effects of CLOS are more difficult to observe and understand with linear motion, and are more apparent in non-linear motion. 

"""





target_velocity_z = 0.008       # Updates the velocity of the target in the z-axis, units in kilometers/second.

for i in range(100):
    
    time_since_launch = time_since_launch + dt                      # Updates the time since launch by the update rate, units in seconds.

    relative_position_x = target_position_x - missile_position_x    # Calculates the position of the target relative to the missile in the x-axis (range), units in kilometers.
    relative_position_z = target_position_z - missile_position_z    # Calculates the position of the target relative to the missile in the z-axis (altitude), units in kilometers.

    phi_m = math.atan2(relative_position_z, relative_position_x)    # Calculates the angle between the line-of-sight between the missile and the target and the velocity vector of the missile, units in radians.

    missile_velocity_x = missile_velocity * math.cos(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the x-axis, units in kilometers/second.
    missile_velocity_z = missile_velocity * math.sin(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the z-axis, units in kilometers/second.

    target_position_x = target_position_x + target_velocity_x*dt    # Updates the position of the target in the x-axis based on the velocity change above, units in kilometers.    
    target_position_z = target_position_z + target_velocity_z*dt    # Updates the position of the target in the z-axis based on the velocity change above, units in kilometers.

    missile_position_z = missile_position_z + missile_velocity_z*dt # Updates the position of the missile in the x-axis based on the velocity change above, units in kilometers.    
    missile_position_x = missile_position_x + missile_velocity_x*dt # Updates the position of the missile in the z-axis based on the velocity change above, units in kilometers.    
    
                                                  # The following section appends their corresponding lists with the value for several parameters of interest for each iteration. 
    
    list_missile_position_z.append(missile_position_z)
    list_missile_position_x.append(missile_position_x)
    list_missile_velocity_z.append(missile_velocity_z)
    list_missile_velocity_x.append(missile_velocity_x)
    list_target_position_z.append(target_position_z)
    list_target_position_x.append(target_position_x)
    list_target_velocity_z.append(target_velocity_z)
    list_target_velocity_x.append(target_velocity_x)
    list_missile_heading_angle.append(phi_m)
    list_time_since_launch.append(time_since_launch)
    
    closing_distance = ((relative_position_x)**2 + (relative_position_z)**2)**0.5  # Calculates the closing distance between the missile and the target, units in kilometers.
    
    detonate = math.isclose(closing_distance, 0, abs_tol=0.1)      # Performs a check before each new iteration to see if the closing distance from the missile to the target is less than 100 meters. Returns a boolean variable (either 'TRUE' or 'FALSE').
    
    if detonate == True:                                           # If the distance between the missile and the target is within 100 meters, the missile "detonates" and the simulation ends.   
        print("BOOM!")
        break


"""
NOTE ON THE FOLLOWING SECTION:
    
The following section of code repeats the alogrithm in iterations of 100 (roughly 10 second sections of time) until detonation is reached.

This is done in an effort to illustrate how command-line-of-sight (CLOS) guidance always has its velocity vector pointing towards the 
target, and has the effect of having the missile "follow" the target and intercepts it in a highly reactive, rather than proactive, manner.

This "breaking-up" of the code is not needed if the target moves in a linear way, because the velocity of the target doesn't change over time.
The effects of CLOS are more difficult to observe and understand with linear motion, and are more apparent in non-linear motion. 

"""





target_velocity_z = 0.01       # Updates the velocity of the target in the z-axis, units in kilometers/second.

for i in range(100):
    
    time_since_launch = time_since_launch + dt                      # Updates the time since launch by the update rate, units in seconds.

    relative_position_x = target_position_x - missile_position_x    # Calculates the position of the target relative to the missile in the x-axis (range), units in kilometers.
    relative_position_z = target_position_z - missile_position_z    # Calculates the position of the target relative to the missile in the z-axis (altitude), units in kilometers.

    phi_m = math.atan2(relative_position_z, relative_position_x)    # Calculates the angle between the line-of-sight between the missile and the target and the velocity vector of the missile, units in radians.

    missile_velocity_x = missile_velocity * math.cos(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the x-axis, units in kilometers/second.
    missile_velocity_z = missile_velocity * math.sin(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the z-axis, units in kilometers/second.

    target_position_x = target_position_x + target_velocity_x*dt    # Updates the position of the target in the x-axis based on the velocity change above, units in kilometers.    
    target_position_z = target_position_z + target_velocity_z*dt    # Updates the position of the target in the z-axis based on the velocity change above, units in kilometers.

    missile_position_z = missile_position_z + missile_velocity_z*dt # Updates the position of the missile in the x-axis based on the velocity change above, units in kilometers.    
    missile_position_x = missile_position_x + missile_velocity_x*dt # Updates the position of the missile in the z-axis based on the velocity change above, units in kilometers.    
    
                                                  # The following section appends their corresponding lists with the value for several parameters of interest for each iteration. 
    
    list_missile_position_z.append(missile_position_z)
    list_missile_position_x.append(missile_position_x)
    list_missile_velocity_z.append(missile_velocity_z)
    list_missile_velocity_x.append(missile_velocity_x)
    list_target_position_z.append(target_position_z)
    list_target_position_x.append(target_position_x)
    list_target_velocity_z.append(target_velocity_z)
    list_target_velocity_x.append(target_velocity_x)
    list_missile_heading_angle.append(phi_m)
    list_time_since_launch.append(time_since_launch)
    
    closing_distance = ((relative_position_x)**2 + (relative_position_z)**2)**0.5  # Calculates the closing distance between the missile and the target, units in kilometers.
    
    detonate = math.isclose(closing_distance, 0, abs_tol=0.1)      # Performs a check before each new iteration to see if the closing distance from the missile to the target is less than 100 meters. Returns a boolean variable (either 'TRUE' or 'FALSE').
    
    if detonate == True:                                           # If the distance between the missile and the target is within 100 meters, the missile "detonates" and the simulation ends.   
        print("BOOM!")
        break


"""
NOTE ON THE FOLLOWING SECTION:
    
The following section of code repeats the alogrithm in iterations of 100 (roughly 10 second sections of time) until detonation is reached.

This is done in an effort to illustrate how command-line-of-sight (CLOS) guidance always has its velocity vector pointing towards the 
target, and has the effect of having the missile "follow" the target and intercepts it in a highly reactive, rather than proactive, manner.

This "breaking-up" of the code is not needed if the target moves in a linear way, because the velocity of the target doesn't change over time.
The effects of CLOS are more difficult to observe and understand with linear motion, and are more apparent in non-linear motion. 

"""





target_velocity_z = 0.015       # Updates the velocity of the target in the z-axis, units in kilometers/second.

for i in range(100):
    
    time_since_launch = time_since_launch + dt                      # Updates the time since launch by the update rate, units in seconds.

    relative_position_x = target_position_x - missile_position_x    # Calculates the position of the target relative to the missile in the x-axis (range), units in kilometers.
    relative_position_z = target_position_z - missile_position_z    # Calculates the position of the target relative to the missile in the z-axis (altitude), units in kilometers.

    phi_m = math.atan2(relative_position_z, relative_position_x)    # Calculates the angle between the line-of-sight between the missile and the target and the velocity vector of the missile, units in radians.

    missile_velocity_x = missile_velocity * math.cos(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the x-axis, units in kilometers/second.
    missile_velocity_z = missile_velocity * math.sin(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the z-axis, units in kilometers/second.

    target_position_x = target_position_x + target_velocity_x*dt    # Updates the position of the target in the x-axis based on the velocity change above, units in kilometers.    
    target_position_z = target_position_z + target_velocity_z*dt    # Updates the position of the target in the z-axis based on the velocity change above, units in kilometers.

    missile_position_z = missile_position_z + missile_velocity_z*dt # Updates the position of the missile in the x-axis based on the velocity change above, units in kilometers.    
    missile_position_x = missile_position_x + missile_velocity_x*dt # Updates the position of the missile in the z-axis based on the velocity change above, units in kilometers.    
    
                                                  # The following section appends their corresponding lists with the value for several parameters of interest for each iteration. 
    
    list_missile_position_z.append(missile_position_z)
    list_missile_position_x.append(missile_position_x)
    list_missile_velocity_z.append(missile_velocity_z)
    list_missile_velocity_x.append(missile_velocity_x)
    list_target_position_z.append(target_position_z)
    list_target_position_x.append(target_position_x)
    list_target_velocity_z.append(target_velocity_z)
    list_target_velocity_x.append(target_velocity_x)
    list_missile_heading_angle.append(phi_m)
    list_time_since_launch.append(time_since_launch)
    
    closing_distance = ((relative_position_x)**2 + (relative_position_z)**2)**0.5  # Calculates the closing distance between the missile and the target, units in kilometers.
    
    detonate = math.isclose(closing_distance, 0, abs_tol=0.1)      # Performs a check before each new iteration to see if the closing distance from the missile to the target is less than 100 meters. Returns a boolean variable (either 'TRUE' or 'FALSE').
    
    if detonate == True:                                           # If the distance between the missile and the target is within 100 meters, the missile "detonates" and the simulation ends.   
        print("BOOM!")
        break


"""
NOTE ON THE FOLLOWING SECTION:
    
The following section of code repeats the alogrithm in iterations of 100 (roughly 10 second sections of time) until detonation is reached.

This is done in an effort to illustrate how command-line-of-sight (CLOS) guidance always has its velocity vector pointing towards the 
target, and has the effect of having the missile "follow" the target and intercepts it in a highly reactive, rather than proactive, manner.

This "breaking-up" of the code is not needed if the target moves in a linear way, because the velocity of the target doesn't change over time.
The effects of CLOS are more difficult to observe and understand with linear motion, and are more apparent in non-linear motion. 

"""





target_velocity_z = 0.02       # Updates the velocity of the target in the z-axis, units in kilometers/second.

for i in range(100):
    
    time_since_launch = time_since_launch + dt                      # Updates the time since launch by the update rate, units in seconds.

    relative_position_x = target_position_x - missile_position_x    # Calculates the position of the target relative to the missile in the x-axis (range), units in kilometers.
    relative_position_z = target_position_z - missile_position_z    # Calculates the position of the target relative to the missile in the z-axis (altitude), units in kilometers.

    phi_m = math.atan2(relative_position_z, relative_position_x)    # Calculates the angle between the line-of-sight between the missile and the target and the velocity vector of the missile, units in radians.

    missile_velocity_x = missile_velocity * math.cos(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the x-axis, units in kilometers/second.
    missile_velocity_z = missile_velocity * math.sin(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the z-axis, units in kilometers/second.

    target_position_x = target_position_x + target_velocity_x*dt    # Updates the position of the target in the x-axis based on the velocity change above, units in kilometers.    
    target_position_z = target_position_z + target_velocity_z*dt    # Updates the position of the target in the z-axis based on the velocity change above, units in kilometers.

    missile_position_z = missile_position_z + missile_velocity_z*dt # Updates the position of the missile in the x-axis based on the velocity change above, units in kilometers.    
    missile_position_x = missile_position_x + missile_velocity_x*dt # Updates the position of the missile in the z-axis based on the velocity change above, units in kilometers.    
    
                                                  # The following section appends their corresponding lists with the value for several parameters of interest for each iteration. 
    
    list_missile_position_z.append(missile_position_z)
    list_missile_position_x.append(missile_position_x)
    list_missile_velocity_z.append(missile_velocity_z)
    list_missile_velocity_x.append(missile_velocity_x)
    list_target_position_z.append(target_position_z)
    list_target_position_x.append(target_position_x)
    list_target_velocity_z.append(target_velocity_z)
    list_target_velocity_x.append(target_velocity_x)
    list_missile_heading_angle.append(phi_m)
    list_time_since_launch.append(time_since_launch)
    
    closing_distance = ((relative_position_x)**2 + (relative_position_z)**2)**0.5  # Calculates the closing distance between the missile and the target, units in kilometers.
    
    detonate = math.isclose(closing_distance, 0, abs_tol=0.1)      # Performs a check before each new iteration to see if the closing distance from the missile to the target is less than 100 meters. Returns a boolean variable (either 'TRUE' or 'FALSE').
    
    if detonate == True:                                           # If the distance between the missile and the target is within 100 meters, the missile "detonates" and the simulation ends.   
        print("BOOM!")
        break


"""
NOTE ON THE FOLLOWING SECTION:
    
The following section of code repeats the alogrithm in iterations of 100 (roughly 10 second sections of time) until detonation is reached.

This is done in an effort to illustrate how command-line-of-sight (CLOS) guidance always has its velocity vector pointing towards the 
target, and has the effect of having the missile "follow" the target and intercepts it in a highly reactive, rather than proactive, manner.

This "breaking-up" of the code is not needed if the target moves in a linear way, because the velocity of the target doesn't change over time.
The effects of CLOS are more difficult to observe and understand with linear motion, and are more apparent in non-linear motion. 

"""




    
target_velocity_z = 0.024       # Updates the velocity of the target in the z-axis, units in kilometers/second.

for i in range(100):
    
    time_since_launch = time_since_launch + dt                      # Updates the time since launch by the update rate, units in seconds.

    relative_position_x = target_position_x - missile_position_x    # Calculates the position of the target relative to the missile in the x-axis (range), units in kilometers.
    relative_position_z = target_position_z - missile_position_z    # Calculates the position of the target relative to the missile in the z-axis (altitude), units in kilometers.

    phi_m = math.atan2(relative_position_z, relative_position_x)    # Calculates the angle between the line-of-sight between the missile and the target and the velocity vector of the missile, units in radians.

    missile_velocity_x = missile_velocity * math.cos(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the x-axis, units in kilometers/second.
    missile_velocity_z = missile_velocity * math.sin(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the z-axis, units in kilometers/second.

    target_position_x = target_position_x + target_velocity_x*dt    # Updates the position of the target in the x-axis based on the velocity change above, units in kilometers.    
    target_position_z = target_position_z + target_velocity_z*dt    # Updates the position of the target in the z-axis based on the velocity change above, units in kilometers.

    missile_position_z = missile_position_z + missile_velocity_z*dt # Updates the position of the missile in the x-axis based on the velocity change above, units in kilometers.    
    missile_position_x = missile_position_x + missile_velocity_x*dt # Updates the position of the missile in the z-axis based on the velocity change above, units in kilometers.    
    
                                                  # The following section appends their corresponding lists with the value for several parameters of interest for each iteration. 
    
    list_missile_position_z.append(missile_position_z)
    list_missile_position_x.append(missile_position_x)
    list_missile_velocity_z.append(missile_velocity_z)
    list_missile_velocity_x.append(missile_velocity_x)
    list_target_position_z.append(target_position_z)
    list_target_position_x.append(target_position_x)
    list_target_velocity_z.append(target_velocity_z)
    list_target_velocity_x.append(target_velocity_x)
    list_missile_heading_angle.append(phi_m)
    list_time_since_launch.append(time_since_launch)
    
    closing_distance = ((relative_position_x)**2 + (relative_position_z)**2)**0.5  # Calculates the closing distance between the missile and the target, units in kilometers.
    
    detonate = math.isclose(closing_distance, 0, abs_tol=0.1)      # Performs a check before each new iteration to see if the closing distance from the missile to the target is less than 100 meters. Returns a boolean variable (either 'TRUE' or 'FALSE').
    
    if detonate == True:                                           # If the distance between the missile and the target is within 100 meters, the missile "detonates" and the simulation ends.   
        print("BOOM!")
        break


"""
NOTE ON THE FOLLOWING SECTION:
    
The following section of code repeats the alogrithm in iterations of 100 (roughly 10 second sections of time) until detonation is reached.

This is done in an effort to illustrate how command-line-of-sight (CLOS) guidance always has its velocity vector pointing towards the 
target, and has the effect of having the missile "follow" the target and intercepts it in a highly reactive, rather than proactive, manner.

This "breaking-up" of the code is not needed if the target moves in a linear way, because the velocity of the target doesn't change over time.
The effects of CLOS are more difficult to observe and understand with linear motion, and are more apparent in non-linear motion. 

"""




    
target_velocity_z = 0.029       # Updates the velocity of the target in the z-axis, units in kilometers/second.

for i in range(100):
    
    time_since_launch = time_since_launch + dt                      # Updates the time since launch by the update rate, units in seconds.

    relative_position_x = target_position_x - missile_position_x    # Calculates the position of the target relative to the missile in the x-axis (range), units in kilometers.
    relative_position_z = target_position_z - missile_position_z    # Calculates the position of the target relative to the missile in the z-axis (altitude), units in kilometers.

    phi_m = math.atan2(relative_position_z, relative_position_x)    # Calculates the angle between the line-of-sight between the missile and the target and the velocity vector of the missile, units in radians.

    missile_velocity_x = missile_velocity * math.cos(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the x-axis, units in kilometers/second.
    missile_velocity_z = missile_velocity * math.sin(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the z-axis, units in kilometers/second.

    target_position_x = target_position_x + target_velocity_x*dt    # Updates the position of the target in the x-axis based on the velocity change above, units in kilometers.    
    target_position_z = target_position_z + target_velocity_z*dt    # Updates the position of the target in the z-axis based on the velocity change above, units in kilometers.

    missile_position_z = missile_position_z + missile_velocity_z*dt # Updates the position of the missile in the x-axis based on the velocity change above, units in kilometers.    
    missile_position_x = missile_position_x + missile_velocity_x*dt # Updates the position of the missile in the z-axis based on the velocity change above, units in kilometers.    
    
                                                  # The following section appends their corresponding lists with the value for several parameters of interest for each iteration. 
    
    list_missile_position_z.append(missile_position_z)
    list_missile_position_x.append(missile_position_x)
    list_missile_velocity_z.append(missile_velocity_z)
    list_missile_velocity_x.append(missile_velocity_x)
    list_target_position_z.append(target_position_z)
    list_target_position_x.append(target_position_x)
    list_target_velocity_z.append(target_velocity_z)
    list_target_velocity_x.append(target_velocity_x)
    list_missile_heading_angle.append(phi_m)
    list_time_since_launch.append(time_since_launch)
    
    closing_distance = ((relative_position_x)**2 + (relative_position_z)**2)**0.5  # Calculates the closing distance between the missile and the target, units in kilometers.
    
    detonate = math.isclose(closing_distance, 0, abs_tol=0.1)      # Performs a check before each new iteration to see if the closing distance from the missile to the target is less than 100 meters. Returns a boolean variable (either 'TRUE' or 'FALSE').
    
    if detonate == True:                                           # If the distance between the missile and the target is within 100 meters, the missile "detonates" and the simulation ends.   
        print("BOOM!")
        break


"""
NOTE ON THE FOLLOWING SECTION:
    
The following section of code repeats the alogrithm in iterations of 100 (roughly 10 second sections of time) until detonation is reached.

This is done in an effort to illustrate how command-line-of-sight (CLOS) guidance always has its velocity vector pointing towards the 
target, and has the effect of having the missile "follow" the target and intercepts it in a highly reactive, rather than proactive, manner.

This "breaking-up" of the code is not needed if the target moves in a linear way, because the velocity of the target doesn't change over time.
The effects of CLOS are more difficult to observe and understand with linear motion, and are more apparent in non-linear motion. 

"""





target_velocity_z = 0.034       # Updates the velocity of the target in the z-axis, units in kilometers/second.

for i in range(100):
    
    time_since_launch = time_since_launch + dt                      # Updates the time since launch by the update rate, units in seconds.

    relative_position_x = target_position_x - missile_position_x    # Calculates the position of the target relative to the missile in the x-axis (range), units in kilometers.
    relative_position_z = target_position_z - missile_position_z    # Calculates the position of the target relative to the missile in the z-axis (altitude), units in kilometers.

    phi_m = math.atan2(relative_position_z, relative_position_x)    # Calculates the angle between the line-of-sight between the missile and the target and the velocity vector of the missile, units in radians.

    missile_velocity_x = missile_velocity * math.cos(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the x-axis, units in kilometers/second.
    missile_velocity_z = missile_velocity * math.sin(phi_m)         # Applies an acceleration to the missile in an attempt null the value calculated for phi above in the z-axis, units in kilometers/second.

    target_position_x = target_position_x + target_velocity_x*dt    # Updates the position of the target in the x-axis based on the velocity change above, units in kilometers.    
    target_position_z = target_position_z + target_velocity_z*dt    # Updates the position of the target in the z-axis based on the velocity change above, units in kilometers.

    missile_position_z = missile_position_z + missile_velocity_z*dt # Updates the position of the missile in the x-axis based on the velocity change above, units in kilometers.    
    missile_position_x = missile_position_x + missile_velocity_x*dt # Updates the position of the missile in the z-axis based on the velocity change above, units in kilometers.    
    
                                                  # The following section appends their corresponding lists with the value for several parameters of interest for each iteration. 
    
    list_missile_position_z.append(missile_position_z)
    list_missile_position_x.append(missile_position_x)
    list_missile_velocity_z.append(missile_velocity_z)
    list_missile_velocity_x.append(missile_velocity_x)
    list_target_position_z.append(target_position_z)
    list_target_position_x.append(target_position_x)
    list_target_velocity_z.append(target_velocity_z)
    list_target_velocity_x.append(target_velocity_x)
    list_missile_heading_angle.append(phi_m)
    list_time_since_launch.append(time_since_launch)
    
    closing_distance = ((relative_position_x)**2 + (relative_position_z)**2)**0.5  # Calculates the closing distance between the missile and the target, units in kilometers.
    
    detonate = math.isclose(closing_distance, 0, abs_tol=0.1)      # Performs a check before each new iteration to see if the closing distance from the missile to the target is less than 100 meters. Returns a boolean variable (either 'TRUE' or 'FALSE').
    
    if detonate == True:                                           # If the distance between the missile and the target is within 100 meters, the missile "detonates" and the simulation ends.   
        print("BOOM!")
        break


"""
NOTE ON THE FOLLOWING SECTION:
    
The following section of code repeats the alogrithm in iterations of 100 (roughly 10 second sections of time) until detonation is reached.

This is done in an effort to illustrate how command-line-of-sight (CLOS) guidance always has its velocity vector pointing towards the 
target, and has the effect of having the missile "follow" the target and intercepts it in a highly reactive, rather than proactive, manner.

This "breaking-up" of the code is not needed if the target moves in a linear way, because the velocity of the target doesn't change over time.
The effects of CLOS are more difficult to observe and understand with linear motion, and are more apparent in non-linear motion. 

"""




  
""""""""""""""""""""""""""""""""""""
"""         DataFrames           """
""""""""""""""""""""""""""""""""""""
    
# Converts the lists used to the parameters of interest during the engagement into dataframes.

df_missile_position_Z = pd.DataFrame(list_missile_position_z, columns=['Missile Z-Axis Position (km)'])
df_missile_position_X = pd.DataFrame(list_missile_position_x, columns=['Missile X-Axis Position (km)'])
df_missile_velocity_Z = pd.DataFrame(list_missile_velocity_z, columns=['Missile Z-Axis Velocity (km/s)'])
df_missile_velocity_X = pd.DataFrame(list_missile_velocity_x, columns=['Missile X-Axis Velocity (km/s)'])
df_target_position_Z = pd.DataFrame(list_target_position_z, columns=['Target Z-Axis Position (km)'])
df_target_position_X = pd.DataFrame(list_target_position_x, columns=['Target X-Axis Position (km)'])
df_target_velocity_Z = pd.DataFrame(list_target_velocity_z, columns=['Target Z-Axis Velocity (km/s)'])
df_target_velocity_X = pd.DataFrame(list_target_velocity_x, columns=['Target X-Axis Velocity (km/s)'])
df_missile_heading_angle = pd.DataFrame(list_missile_heading_angle, columns=['Missile Heading Angle (rad)'])
df_time_since_launch = pd.DataFrame(list_time_since_launch, columns=['Time since Missile Launch (s)'])


# Joins all dataframes to a master dataframe.
df_master = df_time_since_launch.join(df_missile_position_Z, how='outer')
df_master = df_master.join(df_missile_position_X, how='outer')
df_master = df_master.join(df_target_position_Z, how='outer')
df_master = df_master.join(df_target_position_X, how='outer')
df_master = df_master.join(df_missile_velocity_Z, how='outer')
df_master = df_master.join(df_missile_velocity_X, how='outer')
df_master = df_master.join(df_target_velocity_Z, how='outer')
df_master = df_master.join(df_target_velocity_X, how='outer')
df_master = df_master.join(df_missile_heading_angle, how='outer')


""""""""""""""""""""""""""""""""""""
"""       Export to Excel        """
""""""""""""""""""""""""""""""""""""

# Outputs the master dataframe to an excel spreadsheet that can be reviewed.
                                                              
df_master.to_excel('engagement_file.xlsx', index = False)       


""""""""""""""""""""""""""""""""""""
"""        Plot Creation         """
""""""""""""""""""""""""""""""""""""

# Creates and saves to the local directory a plot showing the flight path of the target and missile during the engagement.

fig = plt.plot(list_target_position_x, list_target_position_z, color='royalblue'), plt.plot(list_missile_position_x, list_missile_position_z, color='red'), plt.plot(list_missile_position_x[0], list_missile_position_x[0], color='red', marker='^', markersize='10'), plt.plot(list_target_position_x[0], list_target_position_z[0], color='royalblue', marker='s', markersize='10'), plt.plot(list_missile_position_x[-1], list_missile_position_z[-1], color='gold', marker='*', markersize='15'), plt.plot(list_missile_position_x[-1], list_missile_position_z[-1], color='gold', marker='x', markersize='20')
plt.xticks(rotation=45, ha="right", rotation_mode="anchor")     
plt.ylabel('Altitude (km)')
plt.xlabel('Range (km)')
plt.title('Engagement Scenario (CLOS)')
plt.legend(['Target Aircraft', 'SAM'], loc='lower right')
plt.savefig('Engagement Scenario.jpg', bbox_inches='tight')
plt.show()
