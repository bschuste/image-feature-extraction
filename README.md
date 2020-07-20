# image-feature-extraction
**Display Sample Image and Extract its Features**

## Objective
Extract image features from a sample file.

## Computation Steps
1. Read the ppm sample file
2. Display the file content
3. Compute the image histogram
4. Compute several features like luminance average, median, min and max values 
5. Compute the chrominance saturation and hue
6. Miscellaneous

## First Creation
python3 -m venv env
. ./env/bin/activate
pip install --upgrade pip
# Alternatively upgrade pip this way on OSX if SSL certificate error
curl https://bootstrap.pypa.io/get-pip.py | python3
pip install numpy
pip install matplotlib
pip install Pillow
# Create requirement file
pip freeze > requirements.txt
deactivate

## Running pylint
pylint *.py

## Build and run
pip install -r requirements.txt
python features.py