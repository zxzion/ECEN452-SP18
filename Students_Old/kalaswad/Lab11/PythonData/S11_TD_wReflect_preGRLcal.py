import numpy as np
import matplotlib.pyplot as plt
import csv

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for x, y1, y2, y3
x = []      #frequency
y1 = []

##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('S11_TD_wReflect_preGRLcal.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        x.append(float(row['Time(s)']))
        y1.append(float(row['S11 Log Mag(dB)']))

##Plotting
plt.figure(3) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(x, y1, 'b', label="S11 reflect preGRL") #plot y1 vs. x, solid-blue, add lable for legend

ax1.set_xlim(min(x), max(x)) #set x-axis limits
ax1.legend(loc=2) #add legend at location #1 (top-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('S11 Time Domain Reflect Pre-GRL') #add plot title
plt.xlabel('Time [s]') #add x-axis title
plt.ylabel('Magnitude [dB]') #add y-axis title

plt.show() #required to display plots