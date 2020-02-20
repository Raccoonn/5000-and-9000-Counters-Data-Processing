

def Machine_WaterVolumes(filename_5000, filename_9000, DaysOfOperation):
    '''
    Function to calculate water volumes used by each machine.
    
    Input File: - These files should be the resulting files after parsing the raw
                  5000/9000 counts.csv files.

    For 5000S+: - All drinks are calculated except Iced Coffee and Hot chocolate
                - Americanos have their own volume designation
                - All other espresso drinks are calculated by volume of espresso shot
                  for the corresponding drink size.
                - Volume of hot water estimated to 300 mL, have to confirm this

    For 9000F:  - Only calculates total 2 liter brewings and Hot Tea volumes


    *** NOTICE: - These values of water volume through each machine only include drinks,
                  it does NOT include the amount of water used in cleaning.

                - Therefore it can be said that these values are an underestimate.

                - I will stress that we have NO confidence interval yet, these values are
                  a very rough under-estimate of total water usage currently.
    '''

    # All volumes are in milliliters
    # Water volume for 5000S+ beverages: [S, M, L]
    V_Espresso = [40, 46, 50]
    V_Decaf = [300, 400, 500]
    V_Americano = [300, 400, 500]
    V_HotWater = 400

    # Water volume for 9000F, just include 2 liter brewing
    V_Coffee = 2000
    V_HotTea = [300, 400, 500]


    # Read in beverage data for each machine
    f_5000 = open(filename_5000)
    data_5000 = [[i for i in line.split(', ')] for line in f_5000.read().splitlines()]
    f_5000.close()

    f_9000 = open(filename_9000)
    data_9000 = [[i for i in line.split(', ')] for line in f_9000.read().splitlines()]
    f_9000.close()

    # Espresso recipes for easier sorting of beverages with espresso shots
    f_Espresso = open('Espresso Recipes.txt')
    Espresso_Recipes = [i for i in f_Espresso.read().splitlines()]
    f_Espresso.close()


    # calculate all drinks for 5000S+ except Iced Coffee and Hot Chocolate
    # Initialize volume counter for 5000S+
    V_5000 = 0
    for recipe, count in data_5000:
        size = recipe[-1]   # Pull size from end of recipe string
        count = int(count)  # Convert count from str to int

        # Decaf Coffee
        if 'Decaf' in recipe:
            if size == 'L':
                V_5000 += V_Decaf[2]*count
            elif size == 'M':
                V_5000 += V_Decaf[1]*count
            else:
                V_5000 += V_Decaf[0]*count

        # Americanos
        elif 'Americano' in recipe:
            if size == 'L':
                V_5000 += V_Americano[2]*count
            elif size == 'M':
                V_5000 += V_Americano[1]*count
            else:
                V_5000 += V_Americano[0]*count

        # All Espresso drinks referenced in 'Espresso Recipes.txt'
        elif recipe in Espresso_Recipes:
            if size == 'L':
                V_5000 += V_Espresso[2]*count
            elif size == 'M':
                V_5000 += V_Espresso[1]*count
            else:
                V_5000 += V_Espresso[0]*count

        # Hot Water poured from 5000S+
        elif recipe == 'Hot Water':
            V_5000 += V_HotWater*count




    # Calculate 2 liter brewing and Hot Teas from 9000F
    # Initialie volume counter for 9000F
    V_9000 = 0

    for recipe, count in data_9000:
        size = recipe[-1]   # Pull size from end of recipe string
        count = int(count)  # Convert count from str to int

        # Total volume of 2 liter brewing cycles
        if recipe == '2 liter brewing':
            V_9000 += V_Coffee*count

        # Hot Tea from 9000F
        elif 'Hot Tea' in recipe:
            if size == 'L':
                V_9000 += V_HotTea[2]*count
            elif size == 'M':
                V_9000 += V_HotTea[1]*count
            else:
                V_9000 += V_HotTea[0]*count



    # Operational Time Period
    WeeksOfOperaton = DaysOfOperation/7

    # Print Volumes: Total, Weekly, Daily
    # Divided by 1000 to convert to Liters
    print('\nWater Usage for 5000S+:\n'
        ' Total: ', round(V_5000/1000, 2), '\n',
        'Daily: ', round(V_5000/1000/DaysOfOperation, 2), '\n'
        ' Weekly: ', round(V_5000/1000/WeeksOfOperaton, 2), '\n')

    print('Water Usage for 9000F:\n'
        ' Total: ', round(V_9000/1000, 2), '\n',
        'Daily: ', round(V_9000/1000/DaysOfOperation, 2), '\n'
        ' Weekly: ', round(V_9000/1000/WeeksOfOperaton, 2), '\n')
   

