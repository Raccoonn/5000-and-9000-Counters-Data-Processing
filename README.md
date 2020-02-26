# 5000-and-9000-Counters-Data-Processing
Scripts for cleaning up raw counter data from each machine, as well as plotting the data if desired.


The raw log file for 5000S+ contains a few tes recipes and other weird recipes that I dont know what they are, (Ex.: Milk Foam, Caffe Latte, Latte Macchiato, etc.).  The "Primary Recipes.txt" file is used to filter out these other recipes. 


Usage: Simply run main.py and follow command line prompts.
  - Input raw log filename
  - Input desired output filename
  - Script will write Output files to current directory (Can be used for Volume_BeverageCounts.py - See Below)
  - Plot data if desired

For calculating water usage of machine run Volume_BeverageCounts.py and follow command line prompts.
  - Input output filenames for 5000S+ and 9000F (These are created by using main.py)
  - Output is a formatted print statement showing Total, Weekly, Daily water usage for each machine.


# 2-20-2020:
Added Volume_BeverageCounts.py.  This contains a function that uses a cleaned output file, (post parsing), and calculates the total/weekly/daily volume of water used for each machine.

Removed re.search() from Parser_BeverageCounts.py as it was not compatible with other sites log files.  Instead the raw counters are split at each semicolon using .split(';') then recipe, counts are defined by indexing, line[2], line[3].


# 2-22-2020:
I noticed that there are two lines for "Decaf L" in the 5000S+ counters.  Changed store in parser to better handle multiple recipes.


# 2-26-2020:
Modified Plot_BeverageCounts.py to use a log scale.  My intention is to account for the larger Iced Coffee beverage counts on the 5000S+ skewing the perspective of the plot.
