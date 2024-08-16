import os
import json
import logging
from datetime import datetime
from config import load_commands
from utils import run_command, save_output, display_output, generate_report
from visualization import visualize_active_connections

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a directory to store all the forensic outputs
output_dir = "forensic_outputs"
os.makedirs(output_dir, exist_ok=True)

def gather_forensic_data(commands, selected_domains):
    """Run commands and store their outputs in a structured way."""
    for domain, cmds in commands.items():
        if domain not in selected_domains:
            continue
        
        print(f"\nGathering data for domain: {domain}")
        for name, cmd in cmds.items():
            print(f"Running command: {cmd}")
            output = run_command(cmd)
            save_output(domain, name, output)
            display_output(name, output)

def show_menu(commands):
    """Display a menu for the user to choose domains."""
    print("Select the domains you want to investigate:")
    domain_choices = list(commands.keys())
   
    for idx, domain in enumerate(domain_choices, start=1):
        print(f"{idx}. {domain}")
   
    choices = input("Enter the numbers separated by commas (e.g., 1,3,5) or 'all' to run all: ").strip()
   
    if choices.lower() == 'all':
        selected_domains = domain_choices
    else:
        try:
            selected_indices = [int(x.strip()) - 1 for x in choices.split(",")]
            selected_domains = [domain_choices[i] for i in selected_indices if 0 <= i < len(domain_choices)]
        except ValueError:
            print("Invalid input. Exiting.")
            return []
   
    return selected_domains

def main():
    """Main function to run the forensic tool."""
    try:
        commands = load_commands()
        selected_domains = show_menu(commands)
       
        if not selected_domains:
            print("No valid selection made. Exiting.")
            return
       
        gather_forensic_data(commands, selected_domains)
       
        generate_report(commands, selected_domains)
        visualize_active_connections()
       
        print(f"\n[INFO] Forensics data collection complete. Check the '{output_dir}' directory for output files.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print("An unexpected error occurred. Check the logs for details.")

if __name__ == "__main__":
    main()
