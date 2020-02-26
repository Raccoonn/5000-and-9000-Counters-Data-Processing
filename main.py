from Parser_BeverageCounts import Parse_BeverageCounts
from Plot_BeverageCounts import Plot_BeverageCounts
from Volume_BeverageCounts import Machine_WaterVolumes

if __name__ == '__main__':
    '''
    Command line interface to produce clean counter logs and plot if desired.

    Tips: - Make sure your input/output filenames include '5000S+' or '9000F'
            The Parser will filter out certain lines based on which machine the 
            log file is from.
    '''

    print('\n\n5000/9000 Beverage count parser.\n')
    Input_5000 = input('\nInput 5000S+ raw data filename:  ')
    Output_5000 = input('\nInput 5000S+ output filename:  ')

    Input_9000 = input('\n\nInput 9000F raw data filename:  ')
    Output_9000 = input('\nInput 9000F output filename:  ')

    input('\n\nPress Enter to process 5000S+ data.\n\n')

    Parse_BeverageCounts(Input_5000, Output_5000)

    plot_data = input('Would you like to plot the data? (Y/N): ')
    if plot_data in ['Y', 'y', 'Yes', 'yes']:
        Plot_BeverageCounts(Output_5000)


    input('\n\nPress Enter to process 9000F data.\n\n')

    Parse_BeverageCounts(Input_9000, Output_9000)

    plot_data = input('Would you like to plot the data? (Y/N): ')
    if plot_data in ['Y', 'y', 'Yes', 'yes']:
        Plot_BeverageCounts(Output_9000)   


    calc_volumes = input('\n\nWould you like to estimate water usage? (Y/N): ')
    if calc_volumes in ['Y', 'y', 'Yes', 'yes']:
        DaysOfOperation = input('\nInput number of days in operation: ')
        Machine_WaterVolumes(Output_5000, Output_9000, DaysOfOperation)