<h3>Chinese Writing App</h3>

Chinese handwriting detection app with interactive drawing interface for digits from 1 to 10, created for 2019 Year 4 Computer Elective Programme (CEP) Final Project. 

- Self-collected dataset of 322 data points of each of the 10 digits (for 3220 handwriting samples in total)
- 97.5% accuracy on 80 unseen datapoint validation set
  - Keras sequential model
- Interactive Signature Pad app supported with flask backend

Usage

- Virtual environment
  - Run ``` pip3 install virtualenv``` to install python virtual environemnt package 
  - Inside the main folder, run ```virtualenv [env_name]``` to create the virtual environment
  - To activate the virtual environment, run ```source [env_name]/bin/activate```
  - To deactivate the virtual environment, run ```deactivate```
- Instal the following packages
  - ```flask``` and ```flask-cors``` to run flask server
  - ```keras``` and ```tensorflow```
  - ``` Pillow``` Pillow imagine processing library
- Running
  - Run ```python3 __init__.py``` to run flask server
  - Open the HTML file ```index.html```

