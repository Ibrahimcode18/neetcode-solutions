class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        while True:
            if len(students) == 0:
                return len(students)
            elif not sandwiches[0] in students:
                return len(students)
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                next_student = students[0]
                students.pop(0)
                students.append(next_student)
        