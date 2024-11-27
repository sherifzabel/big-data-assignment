#!/bin/bash

# Step 1: Run load.py
python3 load.py /home/doc-bd-a1/tit_dataset.csv

# Step 2: Run dpre.py
python3 dpre.py

# Step 3: Run eda.py
python3 eda.py

# Step 4: Run vis.py
python3 vis.py

# Step 5: Run model.py
python3 model.py
