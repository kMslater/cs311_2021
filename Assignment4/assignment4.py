import random
import string
import time

######################################
#  Class Defines a Graph Node Object #
######################################
class Node: 

    # Constructor Method
    def __init__(self, layer_index, node_index):
        
        self.children = []
        self.children_connection_weights = []
        self.node_name = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        self.layer_index = layer_index
        self.node_index = node_index

    # Method Recursively Creates Children for each Node
    # @params self, current node layer, nodes per layer map
    def make_children(self, current_layer, nodes_per_layer_map):
  
        if current_layer == len(nodes_per_layer_map) + 1: return

        for index in range(nodes_per_layer_map[current_layer - 1]): self.children.append(Node(current_layer, index))

        first_born = self.children[0]
        first_born.make_children((current_layer + 1), nodes_per_layer_map)
 
        for index in range(1, len(self.children)): self.children[index].children = first_born.children[:]

    # Method Recursively Adjusts the Weight of each child
    # @params self
    def adjust_child_weights(self):

        # Check if parent node or child
        if not self.children: return

        # Initialize new connection weights array
        self.children_connection_weights = []

        # Append new weights with a 0 to 1 value
        for index in range(len(self.children)): 

            self.children_connection_weights.append(random.uniform(0, 1))
            self.children[index].adjust_child_weights()

    # Method calculates and prints the proper index for each layer
    # @params self
    def OUTPUT_indent(self):

        indent = self.layer_index * '  '
        print(indent, end='')

    # Method Recursively Outputs All Children without displaying their weights
    # @params self
    def OUTPUT_children_without_weights(self):

        # Indent the output.
        self.OUTPUT_indent()

        # Check if parent node else print children
        if not self.children: 

            # Output the node name
            print(self.node_name)

        else: 

            # Output all children
            print(self.node_name + " is connected to")
            for child in self.children: child.OUTPUT_children_without_weights()

    # Method Recursively Outputs All Children and displays their weights
    # @params self
    def OUTPUT_children_with_weights(self):
        
        # Indent the output.
        self.OUTPUT_indent()

        if len(self.children) == 0:

            # Output the node name
            print(self.node_name)

        else:  

            # Output output node name and its relative connected node
            print(self.node_name + " is connected to")
            
            for index, child in enumerate(self.children):
                
                # Indent the output.
                self.OUTPUT_indent()

                # Output the weight of the node
                print("with weight " + str(self.children_connection_weights[index]))
                child.OUTPUT_children_with_weights()


print("\n[INFO] Initializing Graph Format!")
time.sleep(0.5)

INPUT_NODES = [4, 3, 2]  

print("[INFO] Initializing Master Node!")
time.sleep(0.5)

master_node = Node(0, 0)

print("[INFO] Creating Children!")
time.sleep(0.5)

# Process Children Creation
master_node.make_children(1, INPUT_NODES)

print("[INFO] Adjusting Child Weights!")
time.sleep(0.5)

# Adjust Children Weights
master_node.adjust_child_weights()

print("[INFO] Ouputing the Children Without Weights!\n")
time.sleep(1)

# Ouput Children without weights
master_node.OUTPUT_children_without_weights()

time.sleep(0.5)
print("\n[INFO] Ouputing the Children With Weights!\n")
time.sleep(1)

# Ouput Children with weights
master_node.OUTPUT_children_with_weights()

time.sleep(0.5)
print("\n[INFO] Closing the Program!\n")
time.sleep(1)
