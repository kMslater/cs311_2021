import os
import csv
import time
import threading
import pandas as panda

# Components
import Components.Loader as loader

# Method reads the CSV path and returns the dataframe.
# Takes CSV path as an input and column header.
def appendFile(filePath, readColumnInput):

    return panda.read_csv(filePath, usecols=readColumnInput)

# Method saves a '.csv' file into a certain directory.
# Takes dataframe and filename as inputs.
def saveFile(dataFrame, fileName):

    print(" ** Preparing to Save the", fileName, "File **\n")
    time.sleep(1)

    # Load the saving animation.
    threading.Thread(target=loader.loadingAnimation("Saving")).start()
    workingDirectory = os.getcwd() + '/' + fileName
    
    with open("Outputs/" + fileName, 'w') as file:

        # CSV.writer method writes and saves a file
        csvWriter = csv.writer(file)
        csvWriter.writerow(dataFrame)

    # Display the save directory.
    time.sleep(1)
    print(" File '" + fileName + "' has been saved to:", workingDirectory, "\n")

    return dataFrame