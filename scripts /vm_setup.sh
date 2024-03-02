#!/bin/bash

# Run using the below command
# bash vm_setup.sh

echo "Downloading anaconda..."
wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh

echo "Running anaconda script..."
bash Anaconda3-2023.09-0-Linux-x86_64.sh -b -p ~/anaconda

echo "Removing anaconda script..."
rm Anaconda3-2023.09-0-Linux-x86_64.sh

#activate conda
eval "$($HOME/anaconda/bin/conda shell.bash hook)"

echo "Running conda init..."
conda init
# Using -y flag to auto-approve
echo "Running conda update..."
conda update -y conda

echo "Installed conda version..."
conda --version
