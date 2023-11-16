"""Allows the ability to create a dynamic sky object and add it to the scene."""

from typing import List

import addon_utils
import bpy


def add_dynamic_sky(brightness: int=2, sky_colour: (float,float,float,float) = (0.434,0.838,1,1),
                    horizon_colour: (float,float,float,float) = (0.962,0.822,0.822,1)):
    
    addon_utils.enable("lighting_dynamic_sky")
    
    bpy.ops.sky.dyn()
    
    dyn_sky = bpy.data.worlds.get(bpy.context.scene.dynamic_sky_name)
    
    bpy.context.scene.world = dyn_sky
    
    scene_brightness = bpy.context.scene.world.node_tree.nodes.get("Scene_Brightness")
    
    scene_brightness.inputs['Strength'].default_value = brightness

    # Adjust the sky and horizon colours
    
    sky_and_horizon = bpy.data.worlds["Dynamic_1"].node_tree.nodes["Sky_and_Horizon_colors"].inputs
    sky_and_horizon[1].default_value = sky_colour
    sky_and_horizon[2].default_value = horizon_colour

    
