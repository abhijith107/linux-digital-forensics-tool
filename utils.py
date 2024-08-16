import subprocess
import os
import json
import logging
from datetime import datetime

output_dir = "forensic_outputs"

def run_command(command):
    """Run a shell command with sudo and return its output."""
    try:
        full_command = f"sudo {command}"
        result = subprocess.run(full_command, shell=True, capture_output=True, text=True, check=True)
        return {"output": result.stdout.strip(), "error": result.stderr.strip()}
    except subprocess.CalledProcessError as e:
        logging.error(f"Command '{command}' failed with exit code {e.returncode}. Error: {e.stderr.strip()}")
        return {"output": "", "error": e.stderr.strip()}
    except Exception as e:
        logging.error(f"Failed to run command '{command}': {e}")
        return {"output": "", "error": str(e)}

def save_output(domain, command_name, output):
    """Save the command output to a JSON file under the appropriate domain."""
    domain_dir = os.path.join(output_dir, domain)
    os.makedirs(domain_dir, exist_ok=True)
   
    # Add timestamp to filename for better traceability
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(domain_dir, f"{command_name}_{timestamp}.json")
    with open(output_file, "w") as f:
        json.dump(output, f, indent=4)
   
    logging.info(f"Output of '{command_name}' saved to {output_file}")

def display_output(command_name, output):
    """Display the command output to the console in a clean format."""
    print(f"\n[{command_name}]")
    if output['error']:
        print("Error:")
        print(output['error'])
    if output['output']:
        print("Output:")
        print(output['output'])
    print("-" * 40)

def generate_report(commands, selected_domains):
    """Generate a basic Markdown report summarizing the forensic data collected."""
    report_file = os.path.join(output_dir, "forensic_report.md")
    
    with open(report_file, "w") as f:
        f.write("# Forensic Report\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Selected Domains:** {', '.join(selected_domains)}\n\n")
        
        for domain, cmds in commands.items():
            if domain not in selected_domains:
                continue
            
            f.write(f"## {domain}\n")
            for name in cmds.keys():
                f.write(f"### {name}\n")
                output_file = os.path.join(output_dir, domain, f"{name}_*.json")
                f.write(f"Output stored in: `{output_file}`\n\n")
                # Optionally, include a snippet of the output
                f.write("```\n")
                with open(output_file) as output_f:
                    output_data = json.load(output_f)
                    f.write(output_data.get("output", "No output"))
                f.write("\n```\n\n")
    
    logging.info(f"Report generated at {report_file}")
    print(f"[INFO] Report generated: {report_file}")
