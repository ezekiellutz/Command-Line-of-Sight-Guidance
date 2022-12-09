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

                                                # Creates empty lists that will be appended later on in the code. 
list_missile_position_z = []
list_missile_position_x = []
list_missile_velocity_z = []
list_missile_velocity_x = []
list_target_position_z = []
list_target_position_x = []
list_target_velocity_z = []
list_target_velocity_x = []
list_missile_velocity = []
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
 
missile_position_x = 1  
missile_position_z = 1
missile_velocity = 0.411
target_position_x = 7
target_position_z = 7
target_velocity_x = 0.343
target_velocity_z = -0.006
time_since_launch = 0 

for i in range(100):
    
    time_since_launch = time_since_launch + dt 

    #theta_m = math.atan2(missile_position_z,missile_position_x) #radians
    #theta_t = math.atan2(target_position_z,target_position_x)   #radians
    #sigma_m = theta_m - theta_t


    relative_position_x = target_position_x - missile_position_x 
    relative_position_z = target_position_z - missile_position_z

    phi_m = math.atan2(relative_position_z, relative_position_x)

    missile_velocity_x = missile_velocity * math.cos(phi_m)
    missile_velocity_z = missile_velocity * math.sin(phi_m)

    target_position_z = target_position_z + target_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    target_position_x = target_position_x + target_velocity_x*dt
    
 
    missile_position_z = missile_position_z + missile_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    missile_position_x = missile_position_x + missile_velocity_x*dt
    
   # The commands below append various lists with the value for several variables of interest for each iteration. 
    
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
    
target_velocity_z = 0.001

for i in range(100):
    
    time_since_launch = time_since_launch + dt 

    #theta_m = math.atan2(missile_position_z,missile_position_x) #radians
    #theta_t = math.atan2(target_position_z,target_position_x)   #radians
    #sigma_m = theta_m - theta_t


    relative_position_x = target_position_x - missile_position_x 
    relative_position_z = target_position_z - missile_position_z

    phi_m = math.atan2(relative_position_z, relative_position_x)

    missile_velocity_x = missile_velocity * math.cos(phi_m)
    missile_velocity_z = missile_velocity * math.sin(phi_m)

    target_position_z = target_position_z + target_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    target_position_x = target_position_x + target_velocity_x*dt
    
 
    missile_position_z = missile_position_z + missile_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    missile_position_x = missile_position_x + missile_velocity_x*dt
    
   # The commands below append various lists with the value for several variables of interest for each iteration. 
    
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
    
    
target_velocity_z = 0.002

for i in range(100):
    
    time_since_launch = time_since_launch + dt 

    #theta_m = math.atan2(missile_position_z,missile_position_x) #radians
    #theta_t = math.atan2(target_position_z,target_position_x)   #radians
    #sigma_m = theta_m - theta_t


    relative_position_x = target_position_x - missile_position_x 
    relative_position_z = target_position_z - missile_position_z

    phi_m = math.atan2(relative_position_z, relative_position_x)

    missile_velocity_x = missile_velocity * math.cos(phi_m)
    missile_velocity_z = missile_velocity * math.sin(phi_m)

    target_position_z = target_position_z + target_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    target_position_x = target_position_x + target_velocity_x*dt
    
 
    missile_position_z = missile_position_z + missile_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    missile_position_x = missile_position_x + missile_velocity_x*dt
    
   # The commands below append various lists with the value for several variables of interest for each iteration. 
    
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
    
target_velocity_z = 0.004

for i in range(100):
    
    time_since_launch = time_since_launch + dt 

    #theta_m = math.atan2(missile_position_z,missile_position_x) #radians
    #theta_t = math.atan2(target_position_z,target_position_x)   #radians
    #sigma_m = theta_m - theta_t


    relative_position_x = target_position_x - missile_position_x 
    relative_position_z = target_position_z - missile_position_z

    phi_m = math.atan2(relative_position_z, relative_position_x)

    missile_velocity_x = missile_velocity * math.cos(phi_m)
    missile_velocity_z = missile_velocity * math.sin(phi_m)

    target_position_z = target_position_z + target_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    target_position_x = target_position_x + target_velocity_x*dt
    
 
    missile_position_z = missile_position_z + missile_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    missile_position_x = missile_position_x + missile_velocity_x*dt
    
   # The commands below append various lists with the value for several variables of interest for each iteration. 
    
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
    

target_velocity_z = 0.006

for i in range(100):
    
    time_since_launch = time_since_launch + dt 

    #theta_m = math.atan2(missile_position_z,missile_position_x) #radians
    #theta_t = math.atan2(target_position_z,target_position_x)   #radians
    #sigma_m = theta_m - theta_t


    relative_position_x = target_position_x - missile_position_x 
    relative_position_z = target_position_z - missile_position_z

    phi_m = math.atan2(relative_position_z, relative_position_x)

    missile_velocity_x = missile_velocity * math.cos(phi_m)
    missile_velocity_z = missile_velocity * math.sin(phi_m)

    target_position_z = target_position_z + target_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    target_position_x = target_position_x + target_velocity_x*dt
    
 
    missile_position_z = missile_position_z + missile_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    missile_position_x = missile_position_x + missile_velocity_x*dt
    
   # The commands below append various lists with the value for several variables of interest for each iteration. 
    
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



target_velocity_z = 0.007

for i in range(100):
    
    time_since_launch = time_since_launch + dt 

    #theta_m = math.atan2(missile_position_z,missile_position_x) #radians
    #theta_t = math.atan2(target_position_z,target_position_x)   #radians
    #sigma_m = theta_m - theta_t


    relative_position_x = target_position_x - missile_position_x 
    relative_position_z = target_position_z - missile_position_z

    phi_m = math.atan2(relative_position_z, relative_position_x)

    missile_velocity_x = missile_velocity * math.cos(phi_m)
    missile_velocity_z = missile_velocity * math.sin(phi_m)

    target_position_z = target_position_z + target_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    target_position_x = target_position_x + target_velocity_x*dt
    
 
    missile_position_z = missile_position_z + missile_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    missile_position_x = missile_position_x + missile_velocity_x*dt
    
   # The commands below append various lists with the value for several variables of interest for each iteration. 
    
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
    


target_velocity_z = 0.01

for i in range(100):
    
    time_since_launch = time_since_launch + dt 

    #theta_m = math.atan2(missile_position_z,missile_position_x) #radians
    #theta_t = math.atan2(target_position_z,target_position_x)   #radians
    #sigma_m = theta_m - theta_t


    relative_position_x = target_position_x - missile_position_x 
    relative_position_z = target_position_z - missile_position_z

    phi_m = math.atan2(relative_position_z, relative_position_x)

    missile_velocity_x = missile_velocity * math.cos(phi_m)
    missile_velocity_z = missile_velocity * math.sin(phi_m)

    target_position_z = target_position_z + target_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    target_position_x = target_position_x + target_velocity_x*dt
    
 
    missile_position_z = missile_position_z + missile_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    missile_position_x = missile_position_x + missile_velocity_x*dt
    
   # The commands below append various lists with the value for several variables of interest for each iteration. 
    
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

target_velocity_z = 0.015

for i in range(100):
    
    time_since_launch = time_since_launch + dt 

    #theta_m = math.atan2(missile_position_z,missile_position_x) #radians
    #theta_t = math.atan2(target_position_z,target_position_x)   #radians
    #sigma_m = theta_m - theta_t


    relative_position_x = target_position_x - missile_position_x 
    relative_position_z = target_position_z - missile_position_z

    phi_m = math.atan2(relative_position_z, relative_position_x)

    missile_velocity_x = missile_velocity * math.cos(phi_m)
    missile_velocity_z = missile_velocity * math.sin(phi_m)

    target_position_z = target_position_z + target_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    target_position_x = target_position_x + target_velocity_x*dt
    
 
    missile_position_z = missile_position_z + missile_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    missile_position_x = missile_position_x + missile_velocity_x*dt
    
   # The commands below append various lists with the value for several variables of interest for each iteration. 
    
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

target_velocity_z = 0.02

for i in range(100):
    
    time_since_launch = time_since_launch + dt 

    #theta_m = math.atan2(missile_position_z,missile_position_x) #radians
    #theta_t = math.atan2(target_position_z,target_position_x)   #radians
    #sigma_m = theta_m - theta_t


    relative_position_x = target_position_x - missile_position_x 
    relative_position_z = target_position_z - missile_position_z

    phi_m = math.atan2(relative_position_z, relative_position_x)

    missile_velocity_x = missile_velocity * math.cos(phi_m)
    missile_velocity_z = missile_velocity * math.sin(phi_m)

    target_position_z = target_position_z + target_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    target_position_x = target_position_x + target_velocity_x*dt
    
 
    missile_position_z = missile_position_z + missile_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    missile_position_x = missile_position_x + missile_velocity_x*dt
    
   # The commands below append various lists with the value for several variables of interest for each iteration. 
    
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


target_velocity_z = 0.025

for i in range(100):
    
    time_since_launch = time_since_launch + dt 

    #theta_m = math.atan2(missile_position_z,missile_position_x) #radians
    #theta_t = math.atan2(target_position_z,target_position_x)   #radians
    #sigma_m = theta_m - theta_t


    relative_position_x = target_position_x - missile_position_x 
    relative_position_z = target_position_z - missile_position_z

    phi_m = math.atan2(relative_position_z, relative_position_x)

    missile_velocity_x = missile_velocity * math.cos(phi_m)
    missile_velocity_z = missile_velocity * math.sin(phi_m)

    target_position_z = target_position_z + target_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    target_position_x = target_position_x + target_velocity_x*dt
    
 
    missile_position_z = missile_position_z + missile_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    missile_position_x = missile_position_x + missile_velocity_x*dt
    
   # The commands below append various lists with the value for several variables of interest for each iteration. 
    
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


target_velocity_z = 0.03

for i in range(100):
    
    time_since_launch = time_since_launch + dt 

    #theta_m = math.atan2(missile_position_z,missile_position_x) #radians
    #theta_t = math.atan2(target_position_z,target_position_x)   #radians
    #sigma_m = theta_m - theta_t


    relative_position_x = target_position_x - missile_position_x 
    relative_position_z = target_position_z - missile_position_z

    phi_m = math.atan2(relative_position_z, relative_position_x)

    missile_velocity_x = missile_velocity * math.cos(phi_m)
    missile_velocity_z = missile_velocity * math.sin(phi_m)

    target_position_z = target_position_z + target_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    target_position_x = target_position_x + target_velocity_x*dt
    
 
    missile_position_z = missile_position_z + missile_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    missile_position_x = missile_position_x + missile_velocity_x*dt
    
   # The commands below append various lists with the value for several variables of interest for each iteration. 
    
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

target_velocity_z = 0.04

for i in range(100):
    
    time_since_launch = time_since_launch + dt 

    #theta_m = math.atan2(missile_position_z,missile_position_x) #radians
    #theta_t = math.atan2(target_position_z,target_position_x)   #radians
    #sigma_m = theta_m - theta_t


    relative_position_x = target_position_x - missile_position_x 
    relative_position_z = target_position_z - missile_position_z

    phi_m = math.atan2(relative_position_z, relative_position_x)

    missile_velocity_x = missile_velocity * math.cos(phi_m)
    missile_velocity_z = missile_velocity * math.sin(phi_m)

    target_position_z = target_position_z + target_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    target_position_x = target_position_x + target_velocity_x*dt
    
 
    missile_position_z = missile_position_z + missile_velocity_z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    missile_position_x = missile_position_x + missile_velocity_x*dt
    
   # The commands below append various lists with the value for several variables of interest for each iteration. 
    
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
    
""""""""""""""""""""""""""""""""""""
"""         DataFrames           """
""""""""""""""""""""""""""""""""""""
    
# Converts the lists used to hold various variables of interest during the engagement into dataframes.

df_missile_position_Z = pd.DataFrame(list_missile_position_z, columns=['Missile Z-Axis Position (km)'])
df_missile_position_X = pd.DataFrame(list_missile_position_x, columns=['Missile X-Axis Position (km)'])
df_missile_velocity_Z = pd.DataFrame(list_missile_velocity_z, columns=['Missile Z-Axis Velocity (km/s)'])
df_missile_velocity_X = pd.DataFrame(list_missile_velocity_x, columns=['Missile X-Axis Velocity (km/s)'])
df_target_position_Z = pd.DataFrame(list_target_position_z, columns=['Target Z-Axis Position (km)'])
df_target_position_X = pd.DataFrame(list_target_position_x, columns=['Target X-Axis Position (km)'])
df_target_velocity_Z = pd.DataFrame(list_target_velocity_z, columns=['Target Z-Axis Velocity (km/s)'])
df_target_velocity_X = pd.DataFrame(list_target_velocity_x, columns=['Target X-Axis Velocity (km/s)'])
df_missile_heading_angle = pd.DataFrame(list_missile_heading_angle, columns=['Missile Heading Angle (rad)'])
df_missile_velocity = pd.DataFrame(list_missile_velocity, columns=['Missile Velocity (km/s)'])
df_time_since_launch = pd.DataFrame(list_time_since_launch, columns=['Time since Missile Launch (s)'])


# Joins all dataframes to a master dataframe.
df_master = df_time_since_launch.join(df_missile_position_Z, how='outer')
df_master = df_master.join(df_missile_position_X, how='outer')
df_master = df_master.join(df_target_position_Z, how='outer')
df_master = df_master.join(df_target_position_X, how='outer')
df_master = df_master.join(df_missile_velocity, how='outer')
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
plt.title('Simulated Engagement')
plt.legend(['Target Aircraft', 'SAM'], loc='lower right')
plt.savefig('Engagement Scenario.jpg', bbox_inches='tight')
plt.show()