class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        number_of_students = len(students)

        foodmap = Counter(students)

        for s in sandwiches:
            if foodmap[s] > 0:
                foodmap[s] -= 1
                number_of_students -= 1
            else:
                return number_of_students
        return number_of_students