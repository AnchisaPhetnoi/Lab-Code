class TaskMasterProgram:
    def __init__(self, task_name, student_name, due_date):
        self.task_name = task_name
        self.student_name = student_name
        self.due_date = due_date
        self.responsible_person = None

    def assign_responsible_person(self, person_name):
        self.responsible_person = person_name

    def display_task_info(self):
        print(f"Task: {self.task_name}")
        print(f"Student: {self.student_name}")
        print(f"Due Date: {self.due_date}")
        if self.responsible_person:
            print(f"Responsible Person: {self.responsible_person}")
        print("\n")


# ตัวอย่างการใช้งาน
task1 = TaskMasterProgram("Complete Assignment", "John Doe", "2024-01-31")
task1.assign_responsible_person("TaskMaster123")

task2 = TaskMasterProgram("Project Presentation", "Jane Doe", "2024-02-15")
task2.assign_responsible_person("TaskMaster456")

# แสดงข้อมูลงาน
task1.display_task_info()
task2.display_task_info()
