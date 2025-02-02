class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # TODO: probably better to rewrite because it is bandage fixing for pair case

        def dfs(employee: int) -> int:
            if visited[employee]:
                # Visiting, so cycle found
                if dp[employee] == -1:
                    dp[employee] = 0
                    return employee
                # Finished, no update needed
                else:
                    return -1

            visited[employee] = True
            cycle = dfs(favorite[employee])
            
            # cycle / pair formed
            if cycle == employee:
                dp[employee] = dp[favorite[employee]] + 1
                typeLst[employee] = -3 if dp[employee] == 2 else -2
                # pair formed
                if typeLst[employee] == -3:
                    # use arm length instead
                    dp[employee] = 0

                cycleUpdate(employee, favorite[employee], typeLst[employee])
                return -1
            
            # cyclic
            if typeLst[favorite[employee]] == -2:
                typeLst[employee] = -2
                dp[employee] = -2
                return -1
            # pair
            if typeLst[favorite[employee]] == -3:
                typeLst[employee] = favorite[employee]
                dp[employee] = 1
                dp[typeLst[employee]] = max(dp[typeLst[employee]], 1)
                return -1
            # unvisited (discovering an cycle)
            if typeLst[favorite[employee]] == -1:
                dp[employee] = dp[favorite[employee]] + 1
                return cycle
            # arm
            typeLst[employee] = typeLst[favorite[employee]]
            dp[employee] = dp[favorite[employee]] + 1
            dp[typeLst[employee]] = max(dp[typeLst[employee]], dp[employee])
            return -1


        def cycleUpdate(cycle: int, cur: int, ce: bool) -> None:
            if cur == cycle:
                return
            
            typeLst[cur] = ce
            dp[cur] = dp[cycle]
            cycleUpdate(cycle, favorite[cur], ce)
            return


        n = len(favorite)
        visited = [False] * n
        typeLst = [-1] * n # -1: unknown, -2: cyclic, -3: pair, 0 -> n-1: arm (pos of pair)
        dp = [-1] * n # unvisited: -1, cyclic: cycle length, pair: max arm length, arm: length of arm

        for i in range(n):
            dfs(i)
        
        cycle = pair = 0
        for i in range(n):
            # cyclic
            if typeLst[i] == -2:
                cycle = max(cycle, dp[i])
            # pair
            elif typeLst[i] == -3:
                pair += dp[i] + dp[favorite[i]] + 2
        
        return max(cycle, pair // 2)