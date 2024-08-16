# linux-digital-forensics-tool

## Overview

The **Linux Digital Forensics Tool** is a Python-based utility designed to automate the collection of forensic data on a Linux system. The tool helps forensic experts gather and analyze system, network, user, process, and log information. It provides structured output in JSON format, generates a detailed forensic report in Markdown, and offers basic data visualization.

## Features

- **Domain-Specific Command Grouping**: Collect data across multiple domains such as System Information, Network Information, User Information, Process Information, and Logs.
- **Interactive User Interface**: Allows users to select specific domains for investigation.
- **Formatted Output**: Outputs are saved in a structured format (JSON) with time-stamped filenames for traceability.
- **Markdown Report Generation**: Automatically generates a summary report of the forensic investigation.
- **Data Visualization**: Provides basic visualizations for key data points (e.g., active network connections).
- **Modular Design**: Easy to extend and customize with additional commands or functionality.

## Requirements

- Python 3.x
- Required Python packages:
  - `PyYAML`
  - `matplotlib`

You can install the necessary packages using pip:

```bash
pip install pyyaml matplotlib

Installation
Clone the Repository:bash git clone https://github.com/your-username/linux-digital-forensics-tool.git
cd linux-digital-forensics-tool


Install Dependencies: pip install -r requirements.txt


Set Up Configuration:

The commands to be executed are defined in the commands.yaml file. You can customize this file to include additional commands or modify existing ones.

Usage
Run the forensic_tool.py script: python forensic_tool.py



Follow the on-screen prompts to select the domains you wish to investigate.

Example

Select the domains you want to investigate:
1. System Information
2. Network Information
3. User Information
4. Process Information
5. Logs
Enter the numbers separated by commas (e.g., 1,3,5) or 'all' to run all: 1,2
Output
Forensic Outputs: The collected data will be stored in the forensic_outputs directory, organized by domain and time-stamped for traceability.
Markdown Report: A summary report will be generated as forensic_report.md in the same directory.
Visualization: Basic data visualization will be displayed during the process.



File Structure
linux-digital-forensics-tool/
│
├── forensic_tool.py           # Main script to run the tool
├── config.py                  # Configuration loader for commands
├── forensic_utils.py          # Utility functions for running commands and handling output
├── visualization.py           # Visualization functions for forensic data
├── commands.yaml              # YAML configuration file defining the commands to execute
└── README.md                  # Project documentation
