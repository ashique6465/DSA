def minimum_cost_to_move(N, A, B):
    MOD = 10**9 + 7
    
    # Initialize dp array
    dp = [0] * (N + 1)
    dp[N] = A[N]
    
    # Calculate minCostFrom[i] which represents min(dp[j] + B[j]) for j > i
    minCostFrom = [0] * (N + 1)
    minCostFrom[N] = dp[N]
    
    for i in range(N - 1, 0, -1):
        dp[i] = A[i]
        if i < N:
            dp[i] += minCostFrom[i + 1]
        dp[i] %= MOD
        
        minCostFrom[i] = dp[i]
        if i < N:
            minCostFrom[i] = min(minCostFrom[i], minCostFrom[i + 1])
    
    return dp[1]

# Example usage with input
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = [0] * (N + 1)
    B = [0] * (N + 1)
    
    for i in range(1, N + 1):
        A[i] = int(data[i])
    
    for i in range(1, N + 1):
        B[i] = int(data[N + i])
    
    result = minimum_cost_to_move(N, A, B)
    print(result)
