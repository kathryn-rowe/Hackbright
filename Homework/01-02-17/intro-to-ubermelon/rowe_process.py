#Opens the Um-server-01 text file and assigns it to the variable log_file
log_file = open("um-server-01.txt")

#Defines/create a function called sales_reports
def sales_reports(log_file):
    #This function reads each line in the log_file aka um-server-01 text file
    for line in log_file:
        #and then strips the string of white space
        line = line.rstrip()
        #assigns the day variable to contain the first through the fourth item
        day = line[0:3]
        #If the characters created in the day variable are the same as Mon, then it prints the line
        if day == "Mon":
            print line


sales_reports(log_file)
