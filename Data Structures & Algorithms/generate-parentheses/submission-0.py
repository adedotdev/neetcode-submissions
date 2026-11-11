class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        '''
        backtracking
        1. only add an opening parenthesis if opened < n
        2. only add a closing parenthesis if closed < opened
        3. append to the result list every valid combination of parenthese
            - a combination is valid if and only if (IIF) opened == closed == n 
            - OR len(combination) == 2 * n (hint: length of combination should always be a single open-close pair (2) times n pairs) 
        '''

        res = []

        def backtrack(curr, opened, closed):
            if opened == closed == n:
                res.append(curr)
                return

            if opened < n:
                backtrack(curr + "(", opened + 1, closed)
            if closed < opened:
                backtrack(curr + ")", opened, closed + 1)

        backtrack("", 0, 0)
        return res