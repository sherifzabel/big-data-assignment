#!/bin/bash

# Copy the result files from the container
docker cp bd-a1-container:/home/doc-bd-a1/res_dpre.csv ./service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-1.txt ./service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-2.txt ./service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-3.txt ./service-result/
docker cp bd-a1-container:/home/doc-bd-a1/vis.png ./service-result/
docker cp bd-a1-container:/home/doc-bd-a1/k.txt ./service-result/

# Stop the container
docker stop bd-a1-container
