import os
import json
import matplotlib.pyplot as plt

output_dir = "forensic_outputs"

def visualize_active_connections():
    """Visualize the active network connections by protocol."""
    protocol_count = {"tcp": 0, "udp": 0}
    
    try:
        # Load the output data from the relevant file
        with open(os.path.join(output_dir, "Network Information", "active_connections_*.json")) as f:
            output_data = json.load(f)
            connections = output_data.get("output", "")
            
            for line in connections.splitlines():
                if line.startswith("tcp"):
                    protocol_count["tcp"] += 1
                elif line.startswith("udp"):
                    protocol_count["udp"] += 1
        
        # Plot the data
        plt.bar(protocol_count.keys(), protocol_count.values(), color=['blue', 'green'])
        plt.title("Active Network Connections by Protocol")
        plt.xlabel("Protocol")
        plt.ylabel("Number of Connections")
        plt.show()
    
    except Exception as e:
        print(f"An error occurred while visualizing active connections: {e}")
