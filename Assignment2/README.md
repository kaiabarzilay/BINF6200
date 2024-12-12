Kaia Barzilay

October 12th, 2024

# BINF6200 Assignment 2

This program takes two commands in the command line, the text file and column number, and returns Descriptive Statistics of the data in that column within the file.

#### In order to run this program a text file with columns of data is required.

## Description:

This code, stats_in_python.py, takes two command line arguments: sys.argv[1], which is the text file name for a file containing columns of data and sys.argv[2], which is the column number. This program loops over the file and for each line appends the value at that column into a list if it is numeric. If this is not possible due to the column being out of range or the value not being numeric, this program returns an error message. Once all the values in the indicated column have been appended to the list the values are used to calculate and print Descriptive Statistics for the column's values. These statistics include number of values in the column (count), the number of valid numbers in the column (numeric), average, maximum, minimum, variance, standard deviation and median.

## Executing Programs in command line:
```
$ python3 stats_in_python.py sys.argv[1] sys.argv[2]
```
### Example commands
```
$ python3 stats_in_python.py data_file2.txt 4
```
```
$ python3 stats_in_python.py data_file3.txt 3
```
