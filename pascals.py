def pascals(numRows):
        i = 0
        j = 0
        sol = [[1]]
        old = [1]
        cur = [1]
        while i < numRows -1:
            while j < len(old)- 1:
                cur.append(old[j]+old[j+1])
                j += 1
            cur.append(1)
            j = 0
            sol.append(cur)
            old = cur
            cur = [1]
            i += 1
        return sol
