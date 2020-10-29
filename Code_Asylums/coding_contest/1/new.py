def interweavingStrings(one, two, three):
    	return helper(0, 0, one, two, three, len(one), len(two))

def helper(i1, i2, one, two, three, l1, l2):
	if i1==l1:
		return two[i2:]==three[i2+i1:]
	elif i2==l2:
		return one[i1:]==three[i1+i2:]
	
	if one[i1]!=three[i1+i2] and two[i2]!=three[i1+i2]:
		return False
	
	return helper(i1+1, i2, one, two, three, l1, l2) or helper(i1, i2+1, one, two, three, l1, l2)

print(interweavingStrings("aabcc", "dbbca", "aadbbbaccc"))
