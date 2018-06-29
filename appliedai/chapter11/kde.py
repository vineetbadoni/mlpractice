# Import the libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Read in data and examine first 10 rows

flights = pd.read_csv('data/formatted_flights.csv')
flights.head(10)


def plotHistForDifferentBins():
    # Show 4 different binwidths
    for i, binwidth in enumerate([1, 5, 10, 15]):
        # Set up the plot
        ax = plt.subplot(2, 2, i + 1)

        # Draw the plotx`
        ax.hist(flights['arr_delay'], bins=int(180 / binwidth),
                color='blue', edgecolor='black')

        # Title and labels
        ax.set_title('Histogram with Binwidth = %d' % binwidth, size=30)
        ax.set_xlabel('Delay (min)', size=22)
        ax.set_ylabel('Flights', size=22)

    plt.tight_layout()
    plt.show()

plotHistForDifferentBins();