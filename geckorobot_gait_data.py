# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 18:46:52 2018

@author: nini
"""

import math
import numpy as np
class Robot:
    Author='IBSS'
    l1=65
    l2=40
    l3=40#three parts of one leg
    origin_x=65
    origin_y=40
    origin_z=-40#start point
    def ik(self,px,py,pz):#Input the target positon
        alpha=math.asin(-self.l3/(px**2+pz**2)**0.5)-math.atan2(pz,px)
        beta=math.asin((self.l1**2-self.l2**2-self.l3**2+px**2+py**2+pz**2)/(2*self.l1*(-self.l3**2+px**2+py**2+pz**2)**0.5))-math.atan2((px**2+pz**2-self.l3**2)**0.5,py)
        gamma=math.asin((self.l1**2+self.l2**2+self.l3**2-px**2-py**2-pz**2)/(2*self.l1*self.l2))
        return alpha,beta,gamma
    def genetate_2d_gait_oneleg(self,width=20,height=20):#generate the target positon list
        y_list_temp=list(np.linspace(0,width,50))
        z_list_temp=[-(4*height)*y**2/(width**2)+(4*height)*y/width for y in y_list_temp]
        y_list=np.array([self.origin_y+item for item in y_list_temp])
        z_list=np.array([self.origin_z+item for item in z_list_temp])
        x_list=np.array([self.origin_x for item in y_list_temp])
        return x_list,y_list,z_list
geckorobot=Robot()
px_list,py_list,pz_list=geckorobot.genetate_2d_gait_oneleg()
angle_list=[]#To Restore all the angle data
for i in range(len(px_list)):
    angle_list.append([rad*180/3.14 for rad in geckorobot.ik(px_list[i],py_list[i],pz_list[i])])
    #command_list.append([rad*200/3.14+150 for rad in geckorobot.ik(px_list[i],py_list[i],pz_list[i])])
angle_array=np.array(angle_list)
angle_array[:,0]=-angle_array[:,0]#inverse the data if needed
angle_array[:,1]=-angle_array[:,1]
angle_array[:,2]=-angle_array[:,2]