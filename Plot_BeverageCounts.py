import matplotlib.pyplot as plt
import numpy as np


def Plot_BeverageCounts(filename_BeverageCounts):
    '''
    Given a processed log file for 5000S+ or 9000F this will plot all the beverages
    and their associated dispensed counts as a labeled bar graph.
    '''

    # Read in Beverage Data
    f = open(filename_BeverageCounts)
    data = [[i for i in line.split(',')] for line in f.read().splitlines()]

    # Split up drink names and dispensed counts
    labels, counts = [], []
    for line in data:
        labels.append(line[0])
        counts.append(int(line[1]))


    x = np.arange(len(labels))  # the label locations
    width = .35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, counts, width)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_title('Counts of Dispensed Drinks')
    ax.set_xticks(x)
    ax.set_yticklabels([])
    ax.set_xticklabels(labels, rotation=90, size='xx-small')


    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom',
                        size='x-small')


    autolabel(rects1)
    fig.tight_layout()
    plt.show()

