def pick_peaks(arr):
    pos = []
    peaks = []
    plateau_start = -1  # Tracks the start of a plateau
    
    if len(arr) < 3:
        return {'pos': [], 'peaks': []}
    
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] >= arr[i + 1]:
            # Check for plateau
            if arr[i] == arr[i + 1]:
                plateau_start = i
            else:
                if plateau_start != -1:
                    pos.append(plateau_start)
                    peaks.append(arr[plateau_start])
                    plateau_start = -1
                else:
                    pos.append(i)
                    peaks.append(arr[i])
        elif arr[i] > arr[i - 1] and arr[i] == arr[i + 1]:
            plateau_start = i
    
    return {'pos': pos, 'peaks': peaks}

# x = [1,2,3,6,4,1,2,3,2,1]

x = [18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18, -4, 19, 4, 18, 10, -4, 8, 13, 9, 16, 18, 6, 7]

# ([18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18, -4, 19, 4, 18, 10, -4, 8, 13, 9, 16, 18, 6, 7]),{'pos': [5, 9, 12, 14, 16, 20, 23], 'peaks': [15, 17, 18, 19, 18, 13, 18]})

print(pick_peaks(x))

