"""The python code helps to read the command line input for curl method."""
"""The import statement the import sys imports the library sys from the module along with the functions and methods of the library system"""
import sys

"""from the lib.helper module we are importing the built in function curl of lib-helper module in to source code"""
from lib.helper import curl

"""url is a variable assigned with none type value"""
URL = None

"""the variable ARG_CNT is assigned with len(sys.argv) -1 len() returns the length of given input."""
ARG_CNT = len(sys.argv) - 1

"""The below if statement checks the condition whether ARG_CNT not equal to 1 then it prints the function will download the content from url"""
if ARG_CNT != 1:
    print('Usage: curl [URL]...')

"""If the ARG CNT variable value is 1, the second argument on the console is placed in the url variable, and if http is not the first argument, http:// is appended to the second argument and stored in the url variable. The curl function is run and the value is printed.""" 
if ARG_CNT == 1:
    URL = sys.argv[1]
    if 'http' not in URL[:5]:
        URL = "http://"+URL

"""the print() function is used to print the output to the terminal.In the below print () function it first executes the curl() function which takes one argument is used to print the output of given function"""
print(curl(URL))
