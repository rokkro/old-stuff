#A file to stuff most of the strings in w/out cluttering up the main file
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
# http://stackoverflow.com/a/17303428 for pretty font coloring

searchTerm = color.BOLD + "Provide a search term or press Enter: " + color.END
searchPrint = [color.RED + color.BOLD, color.END + "\t", color.CYAN + " {", "}" + color.END]
searchTip = color.CYAN + "Press enter if not searching ppa's." + color.END

noCommand = color.RED + "Command failed. Are you sure you are running an Ubuntu based distribution?" + color.END
noConnect = color.RED + color.UNDERLINE + "Error: page failed to load - check your internet connection to "
noPackage = "Make sure you have 'lxml' and 'bs4' installed to search online.\nInstall them with 'sudo pip3 install package-name.'"
noResults = "No results found."
noRootA = "Error: must run as root"
noRootB = color.RED + color.UNDERLINE + "You do not have root privileges to remove ppa's.\n" + color.END
noRootC = color.RED + color.UNDERLINE + "You must run this as root to add or remove ppa's and packages." + color.END
noPPA = color.RED + "You don't seem to have any ppa's installed..." + color.END
noFolder = color.RED + "Your system does not have the expected path to /etc/apt/sources.list.d/" + color.END

versionChk = "If these packages are already installed, you may want to verify that you are running this under Python 3.5.\n" \
             "Start this script with: python3 /path/to/script.py"
processFail = "Command failed to execute."
weirdPPA = " - probably not a ppa, do not remove unless you know what it is. Located in /etc/apt/sources.list.d/"
howToFind = color.BLUE + "Run 'apt-cache search <search-term>' to search the main repos." + color.END

outOfRange = "Input out of range. You may want to load more results if available or start a new search."
invalidInput = "Invalid input."
removed = color.RED + "removed "
cancelled = "Operation cancelled."

optionsA = color.CYAN + "Enter a ppa number or option character below. Adding/removing ppa's and packages can be dangerous." + color.END + "\n[" + color.RED + "s" + color.END + "] - search online ppa's | [" + color.RED + "m" + color.END +\
                "] - load more search results | [" + color.RED + "p" + color.END + "] - reprint search results\n"+ "[" + color.RED + "u" + color.END + "] - update package lists | [" + color.RED + "x" + color.END + "] - view/remove installed ppa's | " + "[" + color.RED + "dup" + color.END + "] - dist-upgrade | [" + \
           color.RED + "q" + color.END + "] - quit.\n>>>\t"
optionsB = "[" + color.RED + "a" + color.END + "] - add this ppa |" \
                                               " [" + color.RED + "s" + color.END + "] - start a new search | [" + color.RED + "u" + color.END + \
           "] - update package lists | [" + color.RED + "t" + color.END + "] - return | [" + color.RED + "q" + color.END + "] - quit.\n>>>\t"
optionsC = "Enter a number to indicate the ppa to view or remove. [" + color.RED + "t" + color.END + "] - return.\n>>>\t"
optionsD = "[" + color.RED + "z" + color.END + "] - remove ppa | [" + color.RED + "m" + color.END + "] - view packages | [" + color.RED + "t" + color.END + "] - return.\n>>>\t"
optionsE = color.CYAN + "Choose which type of packages you would like to view.\nIt's recommended you choose whatever fits your machine's architecture (amd64/i386), or 'all_Packages' if available." + color.END + \
           "\nIf you don't see any options, try updating your package lists (apt-get update). | [" + color.RED + "t" + color.END + "] - return. \n>>>\t"
optionsF = "[" + color.RED + "m" + color.END + "] - load more results | [" + color.RED + "t" + color.END + "] - return.\n>>>\t"
optionsG = "[" + color.RED + "o" + color.END + "] - package details | [" + color.RED + "i" + color.END + "] - install | [" + color.RED + "t" + color.END + "] - return.\n>>>\t"
optionsReturn = "Press " + color.END + "[" + color.RED + "t" + color.END + "]" + " to return.\n>>>\t" + color.END
optionsRemove = color.CYAN + "Enter the number of the ppa you want to remove, or press " + color.END + "[" + color.RED + "t" + color.END + "]" + color.CYAN + " to return.\n" + color.END + ">>>\t"
optionsRemoveConfirmA = [color.RED + "Are you sure you want to remove ","? Removing ppa's can prevent you from getting important package updates." + color.END +
                         "\n[" + color.RED + "y" + color.END + "]es or [" + color.RED + "n" + color.END + "]o\n>>>\t"]
optionsRemoveConfirmB = [" also found. Remove it too? [" + color.RED + "y" + color.END + "]es or [" + color.RED + "n" + color.END + "]o\n>>>\t"]
