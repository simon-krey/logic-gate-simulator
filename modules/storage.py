import json
from modules.simulation import Simulation

def save_to_file(path: str, simulation: Simulation):
    obj = {
        "start_nodes": simulation.start_nodes,
        "logic_nodes": simulation.logic_nodes,
        "output_nodes": simulation.output_nodes
    }

    with open(path, "w") as f:
        json.dump(obj, f)

def load_from_file(path: str, simulation: Simulation):
    with open(path, "r") as f:
        obj = json.load(f)
        simulation.start_nodes = obj["start_nodes"]
        simulation.logic_nodes = obj["logic_nodes"]
        simulation.output_nodes = obj["output_nodes"]
