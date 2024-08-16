import json
import yaml

def load_commands(config_file='commands.yaml'):
    """Load commands from a configuration file (YAML or JSON)."""
    if config_file.endswith('.yaml') or config_file.endswith('.yml'):
        with open(config_file, 'r') as file:
            commands = yaml.safe_load(file)
    elif config_file.endswith('.json'):
        with open(config_file, 'r') as file:
            commands = json.load(file)
    else:
        raise ValueError("Unsupported configuration file format. Use YAML or JSON.")
    
    return commands
