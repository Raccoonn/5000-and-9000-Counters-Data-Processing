from Parser_BeverageCounts import Parse_BeverageCounts
from Plot_BeverageCounts import Plot_BeverageCounts

if __name__ == '__main__':
    '''
    Command line interface to produce clean counter logs and plot if desired.

    Tips: - Make sure your input/output filenames include '5000S+' or '9000F'
            The Parser will filter out certain lines based on which machine the 
            log file is from.
    '''

    print('\n\n5000/9000 Beverage count parser.\n')
    filename_rawInput = input('\nInput raw data filename:  ')
    filename_cleanOutput = input('\nInput output filename:  ')

    Parse_BeverageCounts(filename_rawInput, filename_cleanOutput)

    plot_data = input('\nWould you like to plot the data? (Y/N): ')

    if plot_data not in ['N', 'n', 'No', 'no']:
        Plot_BeverageCounts(filename_cleanOutput)