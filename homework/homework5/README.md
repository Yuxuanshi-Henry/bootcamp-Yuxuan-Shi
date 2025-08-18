# Folder Structure
-data
--raw
--processed
-notebooks
--data
---raw
---processed
-src
README.md

# Format use

This project uses **CSV** and **Parquet** formats:

- **CSV**: Simple, readable, and widely supported.
- **Parquet**: Efficient columnar storage, supports compression, and is suitable for large-scale data processing.

# How Using Environment Variables 

Data paths are set using environment variables:

- `DATA_DIR_RAW` for raw data (default: `data/raw`)
- `DATA_DIR_PROCESSED` for processed data (default: `data/processed`)

The code reads these variables to determine where to save and load data