# 5000-and-9000-Counters-Data-Processing
Scripts for cleaning up raw counter data from each machine, as well as plotting the data if desired.


The raw log file for 5000S+ contains a few tes recipes and other weird recipes that I dont know what they are, (Ex.: Milk Foam, Caffe Latte, Latte Macchiato, etc.).  The "Primary Recipes.txt" file is used to filter out these other recipes. 

Also included in this repository are example input files, output files, and plots that I have created for the Davis location.


Usage: Simply run main.py and follow command line prompts.
  - Input raw log filename
  - Input desired output filename
  - Plot data if desired




# 2-20-2020:
Added Volume_BeverageCounts.py.  This contains a function that uses a cleaned output file, (post parsing), and calculates the total/weekly/daily volume of water used for each machine.

Removed re.search() from Parser_BeverageCounts.py as it was not compatible with other sites log files.  Instead the raw counters are split at each semicolon using .split(';') then recipe, counts are defined by indexing, line[2], line[3].


# 2-22-2020:
I noticed that there are two lines for "Decaf L" in the 5000S+ counters.  The parser was incorrectly taking the lower of the two values and was leading to different results than other sites.  Now in parser the store dictionary stores an increasing integer rather than a string cause the value to be over written.
