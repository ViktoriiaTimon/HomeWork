#

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

def test_team_lead():
    team_lead_check = TeamLead(
    name = "Tom",
    salary = 23000,
    department = "new department",
    programming_language="python",
    team_size= 5
        )
    assert team_lead_check.name == "Tom"
    assert team_lead_check.salary == 23000
    assert team_lead_check.department == "new department"
    assert team_lead_check.programming_language == "python"
    assert team_lead_check.team_size == 5
test_team_lead()
