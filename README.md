# Math Bites
![Check Style](https://github.com/hbyr99/math_bites/actions/workflows/style.yaml/badge.svg)
![Unit Test](https://github.com/hbyr99/math_bites/actions/workflows/unittest.yaml/badge.svg)

A command line interface program to find new and intersting facts about the numbers all around us.

## Installation
The following dependencies are required to run the program:
* python3
* plotly
* requests
* sqlalchemy
* pandas

Run the following to install all dependencies:
```
sudo pip3 install --upgrade plotly requests sqlalchemy pandas
```

To install the program:
```
git clone https://github.com/hbyr99/math_bites/
```

## Usage
### Finding new facts
1. Select the first option from the prompt
2. Select the type of information to look for 
3. Enter the numbers into the prompt:
  * Restrict input to numerical data
  * Dates past the normal calendar are formatted into normal input

### Show facts fetched
1. Select the second option from the prompt
2. Choose the data to show

### Show analytical data
1. Select the third option from the prompt
2. Choose the data to show
3. Check the folder for the .html file containing the scatter graph

### Delete history
1. Select the fourth option from the prompt
    * This is a non-reversable action!

## License
<a href="license.txt"><img src="https://img.shields.io/badge/License-GNU%20GPLv3-blue"/></a>
