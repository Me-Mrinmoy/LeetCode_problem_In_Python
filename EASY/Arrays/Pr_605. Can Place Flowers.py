def canPlaceFlowers(flowerbed, n):
    count = 0
    length = len(flowerbed)

    for i in range(length):
        if flowerbed[i] == 0:
            # Check if previous and next are empty or boundaries
            empty_prev = (i == 0) or (flowerbed[i - 1] == 0)
            empty_next = (i == length - 1) or (flowerbed[i + 1] == 0)
            
            if empty_prev and empty_next:
                flowerbed[i] = 1  # Plant flower
                count += 1
                if count >= n:
                    return True
    return count >= n
