# Python
for x in array:
	if x < pivot:
		less.append(x)
	else:
		greater.append(x)




def append_element(some_list,element):
	some_list.append(element)


def isiterable(obj):
	try:
		iter(obj)
		return True
	except TypeError: #不可迭代
	    return False

x = 5
if ont isiterable(x,list) and isiterable(x):
	x = list(x)


def add_and_maybe_multiply(a,b,c=None):
	result = a + b
        if c is not None:
		    result = result*c
     return result


sequence = [1,2,None,4,None,5]
total = 0
for value in sequence:
	if value is None:
		continue
	total += value


sequence = [1,2,0,4,6,5,2,1]
total_until_5 = 0
for value in sequence:
	if value == 5:
		break
	total_until_5 += value


x = 256
tatal = 0
while x > 500:
	break
total += x

