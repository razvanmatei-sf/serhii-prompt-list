"""
Serhii's Dynamic Prompt List Node for ComfyUI
A custom node with dynamic input count for managing prompt lists.
"""

from .prompt_list_node import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

print("\n" + "="*50)
print("📝 Serhii's Dynamic Prompt List Node Loaded")
print("="*50 + "\n")

# Expose the WEB_DIRECTORY for JavaScript loading
import os
WEB_DIRECTORY = os.path.join(os.path.dirname(os.path.realpath(__file__)), "web")
