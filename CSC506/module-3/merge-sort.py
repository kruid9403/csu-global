list = [6,20,8,19,56,23,87,41,49,53]

def merge_sort(list):
    if len(list) > 1:
        #split the list
        mid=len(list) // 2
        left_arr = list[:mid]
        right_arr = list[mid:]
        
        #index for lists
        l=0
        r=0
        m=0
        print(left_arr)
        print(right_arr)
        #break down arrays
        merge_sort(left_arr)
        merge_sort(right_arr)

        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] < right_arr[r]:
                list[m] = left_arr[l]
                l+=1
            else:
                list[m] = right_arr[r]
                r+=1
            m+=1

        while l < len(left_arr):
            list[m] = left_arr[l]
            l+=1
            m+=1

        while r < len(right_arr):
            list[m] = right_arr[r]
            r+=1
            m+=1

# print(list)
merge_sort(list)
# print(list)