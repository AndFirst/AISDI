def merge_sort(list):
    if len(list) > 1:
        half = len(list)//2
        right = list[half:]
        left = list[:half]
        
        merge_sort(right)
        merge_sort(left)        
        
        r=l=k=0
        
        while r < len(right) and l < len(left):
            if right[r]<left[l]:
                list[k] = right[r]
                r+=1
            else:
                list[k] = left[l]
                l+=1
            k+=1
            
        while r < len(right):
            list[k] = right[r]
            r+=1
            k+=1
            
        while l < len(left):
            list[k] = left[l]
            l+=1
            k+=1
    
    return list
