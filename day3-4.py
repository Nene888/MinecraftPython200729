# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:32:20 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z = mc.player.getTilePos()
for i in range(200):
    mc.setBlock(x,y-1,z+i,57)