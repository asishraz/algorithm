'''

define l = 0 , r = n- 1
while (l <r )
    if arr[l] + arr[r] > k
        r --
    if arr[l] + arr[r] < k
        l ++
    else:
        return true
    
return False














'''