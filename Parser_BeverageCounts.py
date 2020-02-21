
def Parse_BeverageCounts(filename_rawInput, filename_cleanOutput):
    '''
    Given a beverage count log file from the 5000S+ or the 9000F this script will
    parse the raw log and write a file of sorted recipes and the number dispensed.
    '''

    # .split(';') input data to use indexing for recipe, count.  This works better
    # than the regex for variable inputs.  Belleview has 5 counts where as Davis has
    # 4 in each line.  This change broke the regex as it was.
    f_input = open(filename_rawInput)
    data = [line.split(';') for line in f_input.read().splitlines()]
    f_input.close()

    # Delete first line which is just a legend, copied here for reference.
    # Recipe number;S(1)-M(0)-L(2);Beverage;Counter 1;Counter 2;Counter 3;Counter 4
    del data[0]


    # Primary Recipes.txt helps to filter out test recipes and others that I don't
    # know what they are, (Ex.: Caffe Latte, Latte Macchiato, Milk Foam, etc.).
    f_recipes = open('Primary Recipes.txt')
    Primary_Recipes = [i for i in f_recipes.read().splitlines()]
    f_recipes.close()


    # For the 9000F log Coffee S/M/L are written as 'small', 'medium', 'large'
    # This loop will change them to Coffee 'size' for clarity
    # Also removes a space in Decaf M, for some reason there is an extra space
    store = {}
    for line in data:
        recipe, count = line[2], line[3]
        if recipe == 'Decaf  M': recipe = 'Decaf M'
        elif recipe == 'large': recipe = 'Coffee L'
        elif recipe == 'medium': recipe = 'Coffee M'
        elif recipe == 'small': recipe = 'Coffee S'
        
        # If recipe not in "Primary Recipes.txt" it is disregarded
        if recipe in Primary_Recipes:
            store[recipe] = count
            

    # Sorting keys to make final output look nicer
    sort_keys = sorted(store)

    # Write keys in sorted order with dispense count
    f_output = open(filename_cleanOutput, 'w')
    for key in sort_keys:
        f_output.write(key + ', ' + store[key] + '\n')
    f_output.close()
