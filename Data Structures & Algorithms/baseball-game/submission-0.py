class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        record = []
        for x in operations:
            if x == "D":
                num = record[-1] * 2
                record.append(num)
            elif x == "C":
                record.pop()
            elif x == "+":
                record.append(record[-1] + record[-2])
            else:
                record.append(int(x))
        
        answer = 0
        for y in record:
            answer += y
        return answer