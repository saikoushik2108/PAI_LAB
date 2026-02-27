
import matplotlib.pyplot as plt
import networkx as nx

class ProctorCSP:
    def __init__(self, exams, proctors, exam_time, exam_skill, proctor_skills):
        self.exams = exams
        self.proctors = proctors
        self.exam_time = exam_time
        self.exam_skill = exam_skill
        self.proctor_skills = proctor_skills

    def is_valid(self, exam, proctor, assignment):
        # Proctor must have the required skill
        if self.exam_skill[exam] not in self.proctor_skills[proctor]:
            return False

        for assigned_exam in assignment:
            if assignment[assigned_exam] == proctor:
                if self.exam_time[assigned_exam] == self.exam_time[exam]:
                    return False
        return True

    def solve(self, assignment={}):
        if len(assignment) == len(self.exams):
            return assignment

        for exam in self.exams:
            if exam not in assignment:
                break

        for proctor in self.proctors:
            if self.is_valid(exam, proctor, assignment):
                assignment[exam] = proctor
                result = self.solve(assignment)
                if result:
                    return result
                del assignment[exam]

        return None

exams = ['Exam1', 'Exam2', 'Exam3']
proctors = ['P1', 'P2', 'P3']

exam_time = {
    'Exam1': '10AM',
    'Exam2': '10AM',
    'Exam3': '2PM'
}

exam_skill = {
    'Exam1': 'Math',
    'Exam2': 'Science',
    'Exam3': 'Math'
}

proctor_skills = {
    'P1': ['Math'],
    'P2': ['Science'],
    'P3': ['Math', 'Social']
}

csp = ProctorCSP(exams, proctors, exam_time, exam_skill, proctor_skills)
solution = csp.solve()
print("Assignment:", solution)

G = nx.Graph()

for exam, proctor in solution.items():
    G.add_edge(exam, proctor)

node_colors = []
for node in G.nodes():
    if node in exams:
        node_colors.append('lightblue')
    else:
        node_colors.append('lightgreen')

pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color=node_colors,
        node_size=2000, font_size=12, font_weight='bold')
plt.title("Exam-Proctor Assignment Graph")
plt.show()