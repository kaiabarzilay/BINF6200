"""This is a program that opens a text file with columns and
based on the column number provided by the command line,
prints out Descriptive Statistics for the column contents"""

import sys
import math

def main():
    """This is a function to calculate Descriptive Statistics for the column contents,
     or return an error message if that is not possible or
    if some lines in the file need to be skipped."""

    # Create empty lists to store column data
    numbers = []
    original_column_data = []

    # Raise error message if command line is missing arguments
    try:
        # In the command line the second command is the text file name,
        # and the third is the column number.
        data_file_name = sys.argv[1]
        column_to_parse = int(sys.argv[2])

    except IndexError:
        print("Error: Please enter a valid text file name/column number")
        sys.exit()

    # Open text file as indicated by the command line
    with open (data_file_name,"r",encoding='utf-8') as infile:
        # Initialize line count
        count = 0

        for line in infile:
            # Iterate over every line in the text file and remove data at indicated column
            # Append data in the column to list

            try:
                count = count+1
                original_column_data.append((line.split())[column_to_parse])

            # If this doesn't work, indicate that there is no data at the column and line indicated.
            # Exit the program
            except IndexError:
                print('\n'+'Exiting:','There is no valid' +'', "'list index'",'' + 'in column'+'',
                      sys.argv[2],'',
                  'in line'+'',count,''+'in file: '+sys.argv[1]+'\n')
                sys.exit()

        # For each data point in the list try to turn it into a float.
        # Append float numbers to numbers list
        for i,float_number in enumerate(original_column_data):

            try:
                float_number = float(original_column_data[i])
                if math.isnan(float_number):
                    continue
                numbers.append(float_number)

            # If this doesn't work, indicate that the value could not be turned into a float
            except ValueError:
                print('Skipping line number'+' '+ str(i + 1)+
                     ": could not convert string to float : \'"+
                    original_column_data[i]+ "\'"+'\n')

        # If there are no valid numbers in the column print error message.
        if len(numbers) == 0:
            print('\n''Error: There were no valid number(s) in column'+'',
                  sys.argv[2],'' +'in file:'+'',sys.argv[1] +'\n')
            sys.exit()

        # The length of the data in the column
        column_count = len(original_column_data)
        # The length of the valid floats in the column
        number_count = len(numbers)

        # Calculate maximum and minimum of the data in the column
        column_maximum = max(numbers[:])
        column_minimum = min(numbers[:])

        # Calculate the column variance and standard deviation
        try:
            column_variance = sum((x - (math.fsum(numbers[:]))
                                   / (len(numbers))) ** 2 for x in numbers) / (number_count - 1)
            column_std_dev = math.sqrt(column_variance)
        # If there is only one data in the column print variance and standard deviation as 0
        except ZeroDivisionError:
            column_variance = 0
            column_std_dev = 0

        # Print statements for Descriptive Statistics
        print('\n'+'    Column:', sys.argv[2],'\n')
        print('        Count     =', f"{column_count:>10.3f}")
        print('        ValidNum  =', f"{number_count:>10.3f}")
        print('        Average   =', f"{(math.fsum(numbers[:]))/ (len(numbers)):>10.3f}")
        print('        Maximum   =', f"{column_maximum:>10.3f}")
        print('        Minimum   =', f"{column_minimum:>10.3f}")
        print('        Variance  =', f"{column_variance:>10.3f}")
        print('        Std Dev   =', f"{column_std_dev:>10.3f}")
        print('        Median    =', f"{(sorted(numbers))[int(number_count / 2)]:>10.3f}\n")

main()
