# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 19:35:10 2021

@author: ArDC
"""

import math
import numpy as np
import matplotlib.pyplot as plt


N=50 #number of points in each direction
x_start , x_end = -2,2 #bundaries in x direction 
y_start , y_end = -1,1 #boundaries in y direction
x = np.linspace(x_start, x_end, 50) #1Darray in x coordinates
y = np.linspace(y_start, y_end, 50) #1D array in y coordinates

print('x = ', x)
print('y = ', y)

X, Y = np.meshgrid (x,y) #generates a mesh grid


#plot the upper box grid of points

width = 10.0
height = (y_end - y_start) / (x_end - x_start) * width
plt.figure(figsize=(width, height))

plt.xlabel('$x$', fontsize=16)
plt.ylabel('$y$', fontsize=16)
plt.xlim(x_start, x_end)
plt.ylim(y_start, y_end)
plt.scatter(X, Y, s=5, color='blue', marker='o')


########## SOURCE FLOW (Positive Strength) ######################
strength_source=5.0 #strength source
x_source, y_source = -1,0 #location of the source
#compute the velocity field on the mesh grid
u_source = (strength_source / (2 * math.pi) *
 (X - x_source) / ((X - x_source)**2 + (Y - y_source)**2))
v_source = (strength_source / (2 * math.pi) * (Y - y_source) / ((X - x_source)**2 + (Y - y_source)**2))           
            
            
# plot the streamlines
width = 10.0
height = (y_end - y_start) / (x_end - x_start) * width
plt.figure(figsize=(width, height))
plt.xlabel('$x$', fontsize=16)
plt.ylabel('$y$', fontsize=16)
plt.xlim(x_start, x_end)
plt.ylim(y_start, y_end)
plt.streamplot(X, Y, u_source, v_source,
                  density=2, linewidth=1, arrowsize=2, arrowstyle='->')
plt.scatter(x_source, y_source,
               color='Black', s=80, marker='o');

########### SINK FLOW (Negative Strength) #########################

strength_sink = -5.0                     # strength of the sink
x_sink, y_sink = 1.0, 0.0                # location of the sink

# compute the velocity on the mesh grid
u_sink = (strength_sink / (2 * math.pi) *
          (X - x_sink) / ((X - x_sink)**2 + (Y - y_sink)**2))
v_sink = (strength_sink / (2 * math.pi) *
          (Y - y_sink) / ((X - x_sink)**2 + (Y - y_sink)**2))
# plot the streamlines
width = 10.0
height = (y_end - y_start) / (x_end - x_start) * width
plt.figure(figsize=(width, height))
plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)
plt.xlim(x_start, x_end)
plt.ylim(y_start, y_end)
plt.streamplot(X, Y, u_sink, v_sink,
                  density=2.5, linewidth=1, arrowsize=2, arrowstyle='->')
plt.scatter(x_sink, y_sink,
               color='#CD2305', s=80, marker='o');

#Use Super Position to add Sink and Source flow to find a soulution for potential flow

u_pair = u_source + u_sink 
v_pair = v_source + v_sink

# plot the streamlines of the pair source/sink
width = 10.0
height = (y_end - y_start) / (x_end - x_start) * width
plt.figure(figsize=(width, height))
plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)
plt.xlim(x_start, x_end)
plt.ylim(y_start, y_end)
plt.streamplot(X, Y, u_pair, v_pair,
                  density=2.5, linewidth=1, arrowsize=2, arrowstyle='->')
plt.scatter([x_source, x_sink], [y_source, y_sink], 
               color='#CD2305', s=50, marker='o');
           