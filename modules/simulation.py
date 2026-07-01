from modules.gates import gates

class Simulation:
    def __init__(self):
        self.updating = False
        self.next_update_layer = 0

        self.start_nodes = [

        ]

        self.logic_nodes = [
            # {"type" : "and", "layer" : 0, "inputs": [-1, -2], "outputs": [3], "out_active": False, "pos": [0, 0]}
        ]
  
        self.output_nodes = [

        ]

    def update(self):
        def get_active(in_index: int):
            if in_index < 0:
                in_index = in_index * -1 - 1
                return self.start_nodes[in_index]["out_active"]

            else:
                return self.logic_nodes[in_index]["out_active"]
            
        def get_gate_fn(gate_str: str):
            return gates[gate_str]

        if self.updating == False:
            self.updating = True
            self.next_update_layer = 0

        for node in self.logic_nodes:
            if node["layer"] == self.next_update_layer:
                inputs = [get_active(in_index) for in_index in node["inputs"]]
                node["out_active"] = get_gate_fn(node["type"])(*inputs)

        self.next_update_layer += 1

