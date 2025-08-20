# Credit Risk Classification

## Stage 01: Problem Framing & Scoping

### Problem Statement
Predict whether a loan applicant has good credit or not. This helps banks reduce financial risk while still approving as many reliable customers as possible.

### Stakeholder & User
* Stakeholder: Bank Risk Management Team
* User: Credit Analysts
* Decision Window: Loan approval decision at applying time

### Useful Answer & Decision
* Type: Classification
* Artifact: Predicted label (default or non-default) for each applicant
* Decision Trigger: If predicted as `default` --> flag applicant as high risk

### Assumptions & Constraints
* Data available: Historical loan applications with repayment outcomes (e.g., German Credit dataset)
* Only structured tabular features used (demographics, income, loan details, etc.)
* Model maybe simple

## Stage 02: Tooling Setup

### Verified Interpreter
Python version: 3.10.18 (main, Jun  5 2025, 08:37:47) [Clang 14.0.6 ]\
Interpreter path: /opt/anaconda3/envs/bootcamp_env/bin/python

### Import Check
Checked import works wells
### load .env
### print data_dir

## Stage 03: Python Fundamentals

### Define functions
calc_mean_std: calculate the mean and standard deviation of a list of numbers

log_call: decorator to log function calls with timestamp

calc_mean_std_logged: calculate the mean and standard deviation of a list of numbers with logging



### Save functions to src/utils.py

## Stage 04: Data Acquisition and Ingestion

Downloaded data from https://archive.ics.uci.edu/static/public/144/data.csv\
Saved to files: metadata.json features.csv targets.csv original.csv variable_info.txt variables.csv\
Checked data validation -> No na found 

## Stage 05: Data Storage

Stored in metadata.json features.csv targets.csv original.csv

## Stage 06: Data Processing
Modified targets' definition from `good -> 1; bad -> 2` to `good -> 1; bad -> 0`\
Filled na with median for all numerical data\
Normalized (0-1) all numerical features\
Saved files to dir: data/processed


---
## **Lifecycle Mapping**
(Update here with future steps)

**Goal --> Stage --> Deliverable**
---
* Define loan default prediction scope -> Stage 01 -> This scoping doc
* Setting up tools -> Stage 02 -> .env & config.py
* Python fundamental functions -> Stage 03 -> utils.py
* Data acquisition -> Stage 04 -> metadata.json features.csv targets.csv original.csv
* Data storage -> Stage 05 -> features.csv targets.csv
* Data processing -> Stage 06 -> features_simple_processed.csv targets_simple_processed.csv