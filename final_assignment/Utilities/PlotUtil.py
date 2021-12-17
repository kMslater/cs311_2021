import matplotlib.pyplot as plot

# Method generates a plots based on the values that are inputted.
def generatePlotPng_FromSortingAlgorithmData(headers, values):
    
    # Define X Variables
    xPositions = [index for index, _ in enumerate(headers)]

    # Plot all bars
    plot.bar(xPositions, values, color='blue')

    # Define y-values
    plot.ylabel('Time Taken (Seconds)')
    plot.title('Sorting Algorithm Runtimes (Big-O Analysis)')

    # Define x-values
    plot.xticks(xPositions, headers)

    # Save PNG and show the plot/chart/graph
    plot.gcf().savefig('Outputs/sorting_big_o_bar_chart.png')
    plot.show()