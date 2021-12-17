import sys
import time
import threading

# Utilities
import Utilities.FileUtil as fileUtil
import Utilities.PlotUtil as plotUtil
import Utilities.SortingUtil as sortingUtil

# Components
import Components.Loader as loader

def main(argv):

    # Define CSV file.
    stock_tickers_file = 'Resources/stock_tickers.csv'

    time.sleep(0.5)
    print("\n ### Starting the Program ###\n")
    time.sleep(0.5)
    time.sleep(0.5)
    print("\n ** Checking System Configs **\n")
    time.sleep(0.5)

    # Show Recursion Limit
    print("\nSystem Recursion Limit:", sys.getrecursionlimit())

    # Initialize dataframe
    marketCapDataFrame = fileUtil.appendFile(stock_tickers_file, ["Market Cap"])[:2000]
    
    # Log info
    print("\n Based on the Recursion Limit, only retreived 2000 lines from the CSV file")

    # Fill all 'nan' values with 0
    marketCapDataFrame["Market Cap"] = marketCapDataFrame["Market Cap"].fillna(0)
    marketCapDataFrame["Market Cap"] = marketCapDataFrame["Market Cap"].astype(float).astype(int)

    print("\u0332".join("\n\nCSV File Provided:\n\n"), " " + stock_tickers_file, "\n")

    # Define Lists
    marketCapList_forHeapSort = marketCapDataFrame["Market Cap"].values.tolist()
    marketCapList_forQuickSort = marketCapDataFrame["Market Cap"].values.tolist()
    marketCapList_forShellSort = marketCapDataFrame["Market Cap"].values.tolist()

    time.sleep(0.5)
    print("\n ** Preparing to HeapSort the Market Cap into Ascending Order **\n")
    time.sleep(0.5)

    # Load the sort animation
    threading.Thread(target=loader.loadingAnimation("Sorting")).start()
    
    # Count time for the heapsort algorithm
    heapSort_start = time.time()
    heapSortResponse = sortingUtil.sortMarketCapAscending_UsingHeapSort(marketCapList_forHeapSort)
    heapSort_end = time.time()

    time.sleep(0.5)
    print("\n ** Preparing to QuickSort the Market Cap into Ascending Order **\n")
    time.sleep(0.5)

    # Load the sort animation
    threading.Thread(target=loader.loadingAnimation("Sorting")).start()

    # Count time for the quicksort algorithm
    quickSort_start = time.time()
    quicketSortResponse = sortingUtil.sortMarketCapAscending_UsingQuickSort(marketCapList_forQuickSort)
    quickSort_end = time.time()

    time.sleep(0.5)
    print("\n ** Preparing to ShellSort the Market Cap into Ascending Order **\n")
    time.sleep(0.5)

    # Load the sort animation
    threading.Thread(target=loader.loadingAnimation("Sorting")).start()

    # Count time for the shellsort algorithm
    shellSort_start = time.time()
    shellSortResponse = sortingUtil.sortMarketCapAscending_UsingShellSort(marketCapList_forShellSort)
    shellSort_end = time.time()

    # Total Time Taken
    heapSortTotal = heapSort_end - heapSort_start
    quickSortTotal = quickSort_end - quickSort_start
    shellSortTotal = shellSort_end - shellSort_start

    # Defined Values for the plot
    plotValues = []
    plotValues.append(heapSortTotal)
    plotValues.append(quickSortTotal)
    plotValues.append(shellSortTotal)

    # Save the results to CSV files
    fileUtil.saveFile(quicketSortResponse, "quickSortAscending.csv")
    fileUtil.saveFile(heapSortResponse, "heapSortAscending.csv")
    fileUtil.saveFile(shellSortResponse, "shellSortAscending.csv")

    print("\n Time Taken by QuickSort (seconds): ", quickSortTotal)
    print(" Time Taken by HeapSort  (seconds): ", heapSortTotal)
    print(" Time Taken by ShellSort (seconds): ", shellSortTotal, "\n")

    time.sleep(0.5)
    print("\n ** Prepare Generate Bar Chart from Processed Data **\n")
    time.sleep(0.5)

    # Load the chart animation
    threading.Thread(target=loader.loadingAnimation("Charting")).start()

    # Generate the chart
    plotUtil.generatePlotPng_FromSortingAlgorithmData(["HeapSort", "QuickSort", "ShellSort"], plotValues)

    time.sleep(0.5)
    print("\n ### Closing the Program ###\n")
    time.sleep(0.5)
   
if __name__ == '__main__':

    # Running the project here.
    main(sys.argv)