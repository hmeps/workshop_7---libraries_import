import sys
print("Total Arguements:", len(sys.argv))
print("Script name:", sys.argv[0])
# sys.argv[0] will always print the name of the file in the terminal
if len(sys.argv) > 1:
    print("Additional Arguements:")
    for arg in sys.argv[1:]:
        print(arg)
    """
        The colon inside the square brackets makes it go through all further arguements
        without it, only arg1 is printed as it is the first member of the list aka [1]
    """