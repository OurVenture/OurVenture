from dataclasses import dataclass
import json
from dataclasses import dataclass
import string

"""
Everything needed to display a relationship, int value between members, modifiers and list of interactions
"""

@dataclass
class Relation:
    # Relation tag is a summary of the relation in a single value
    relation_tag: string