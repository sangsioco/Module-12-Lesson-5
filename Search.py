def binary_search(video_titles, target):
    low = 0
    high = len(video_titles) - 1
    
    while low <= high:
        mid = (low + high) 
        guess = video_titles[mid]
        
        if guess == target:
            return mid
        if guess < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1
