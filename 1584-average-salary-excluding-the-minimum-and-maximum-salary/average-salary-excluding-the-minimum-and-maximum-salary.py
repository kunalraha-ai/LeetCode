class Solution:
    def average(self, salary: List[int]) -> float:
        average_salary = sum(salary) - min(salary) - max(salary)
        return average_salary / (len(salary) - 2)