"""Allows the ability to set the background of the scene to be an hdri image."""

import bpy

def add_hdri_background(path: str):
    """Add an hdri background to the scene.

    :param path: The relative path to the hdri image for the background
    :type path: str
    """
    C = bpy.context

    # Get the environment node tree of the current tree
    node_tree = C.scene.world.node_tree
    tree_nodes = node_tree.nodes

    # Clear all the nodes
    tree_nodes.clear()

    # Add a background node
    node_background = tree_nodes.new(type='ShaderNodeBackground')

    # Add environment texture node
    node_environment = tree_nodes.new('ShaderNodeTexEnvironment')

    # Load and assign the image to the node property
    node_environment.image = bpy.data.images.load(path)
    
    # Add output node
    node_output = tree_nodes.new(type='ShaderNodeOutputWorld')
    
    # Link the nodes together
    links = node_tree.links
    link = links.new(node_environment.outputs["Color"], node_background.inputs["Color"])
    link = links.new(node_background.outputs["Background"], node_output.inputs["Surface"])
