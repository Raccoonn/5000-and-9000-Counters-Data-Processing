from Parser_BeverageCounts import Parse_BeverageCounts
from Plot_BeverageCounts import Plot_BeverageCounts

if __name__ == '__main__':
    '''
    Command line interface to produce clean counter logs and plot if desired.
    '''

    print('\n\n5000/9000 Beverage count parser.\n')
    filename_rawInput = input('\nInput raw data filename:  ')
    filename_cleanOutput = input('\nDefine output filename:  ')

    Parse_BeverageCounts(filename_rawInput, filename_cleanOutput)

    plot_data = input('\nWould you like to plot the data? (Y/N): ')

    if plot_data not in ['N', 'n', 'No', 'no']:
        Plot_BeverageCounts(filename_cleanOutput)
