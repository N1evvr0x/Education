class Solution:
    def isPalindrome(self, x: int) -> bool:
        answer = []
        result = []
        if x < 0:
            return False
        for i in str(x):
            answer.append(i)
        for i in answer:
            result.append(i)
        result.reverse()
        for i in range(len(answer)):
            if answer[i] != result[i]:
                return False
        return True
Solution = Solution()
print(Solution.isPalindrome(121))
