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
    # Relation connection is a dict containing k,v pairs (names, relation values)
    relation_connections: dict
    # Relation history is a json file of the overall relation, which tracks changes, effects and connections.
    # In later instances of this app, these could be retrieved by communicating with an external database
    relation_history: json
    # Simple relation trend, if it is going up, shows next tag, if its going down shows tag below
    relation_trend: string
    relation_value: float
    def __post_init__(self):
        self.relation_tag = self.calculate_tag(self.relation_value)

    def calculate_tag(self) -> string:
        if self.relation_value >= 4.5:
            return "Excellent" 
        elif 3.0 <= self.relation_value < 4.5:
            return "Great"
        elif 1.5 <= self.relation_value < 3.0:
            return "Good"
        elif 0.1 <= self.relation_value < 1.5:
            return "Improving"
        elif -0.5 <= self.relation_value < 0.1:
            return "Neutral"
        elif -1.5 <= self.relation_value < -0.5:
            return "Worsening"
        elif -3.0 <= self.relation_value < -1.5:
            return "Bad"
        elif -4.5 <= self.relation_value < -3.0:
            return "Terrible"
        elif -6.0 <= self.relation_value < -4.5:
            return "Hatred"