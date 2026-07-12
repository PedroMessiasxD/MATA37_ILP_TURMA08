def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def organizingContainers(container):
    n = len(container)
    
    
    container_capacities = [0] * n
    
    ball_type_totals = [0] * n
    
    
    for i in range(n):
        for j in range(n):
            container_capacities[i] += container[i][j]
            ball_type_totals[j] += container[i][j]
            
    
    
    
    bubble_sort(container_capacities)
    bubble_sort(ball_type_totals)
    
    
    possible = True
    for i in range(n):
        if container_capacities[i] != ball_type_totals[i]:
            possible = False
            break
            
    if possible:
        return "Possible"
    else:
        return "Impossible"

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    q = int(input_data[ptr])
    ptr += 1
    
    results = []
    for _ in range(q):
        n = int(input_data[ptr])
        ptr += 1
        
        container = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(int(input_data[ptr]))
                ptr += 1
            container.append(row)
            
        results.append(organizingContainers(container))
        
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
