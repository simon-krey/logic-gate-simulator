def gate_and(in1: bool, in2: bool):
    if in1 and in2:
        return True
    
    return False

def gate_not(in1: bool):
    return not in1

gates = {
    "and": gate_and,
    "not": gate_not 
}
