FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

RUN mkdir /home/doc-bd-a1/

COPY tit_dataset.csv /home/doc-bd-a1/
COPY load.py dpre.py eda.py model.py vis.py /home/doc-bd-a1/

CMD ["/bin/bash"]


# FROM ubuntu:22.04

# # Install Python3 and required packages
# RUN apt-get update && apt-get install -y python3 python3-pip
# RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# # Create the working directory
# RUN mkdir -p /home/doc-bd-a1/

# # Copy dataset and scripts
# COPY tit_dataset.csv /home/doc-bd-a1/tit_dataset.csv
# COPY *.py /home/doc-bd-a1/
# COPY run_pipeline.sh /home/doc-bd-a1/run_pipeline.sh

# # Grant execute permission to the script
# RUN chmod +x /home/doc-bd-a1/run_pipeline.sh

# # Set the working directory
# WORKDIR /home/doc-bd-a1/

# # Set the script as the entrypoint
# CMD ["./run_pipeline.sh"]

