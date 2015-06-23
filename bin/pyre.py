import sys
#import create

print ("Number of arguments: " + str(len(sys.argv)) + " arguments")
print ("List of arguments: " + str(sys.argv) + "")
for a in range(0, len(sys.argv)):
    print ("Argument " + str(a) + ": " + str(sys.argv[a]) + "")
initial_statement = sys.argv[1]
if initial_statement == "create":
    print ("Create")
    # Comment
