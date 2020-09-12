for i in range(1,101):
    if i%7==0 :
        continue
    if i>10:
    	if str(i)[0]=='7' or str(i)[1]=='7':
    	    continue
    print(i)
