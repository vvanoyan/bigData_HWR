import sys
for line sys.stdin:

    data = line.strip().split("\t")
    if (len(data)!=6):
        raise NameError('Row has not 6 elements')
    # store the 6 elements of the tuple in seperate variables
    date, time, item, category, sales, payment = data
    # Write the key-value combination to standard output (stdout)
    # Key is the payment, value is the sales     
    # With a tab (\t) between key and value
    # New line \n means new record
    mylist=['Computers','Cameras','Video Games']
    if(category in mylist):
         sys.stdout.write("{0}\t{1}\n".format(category, sales))
