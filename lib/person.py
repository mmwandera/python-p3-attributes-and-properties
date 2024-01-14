#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name='J. Doe', job='Sales'):
        self.name = name
        self.job = job

    # Define a name property for your Person class. The name must be of type str and under 25 characters. The name should be converted to title caseLinks to an external site. before it is saved.
    # If the name is invalid, the setter method should print() "Name must be string under 25 characters."
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if type(name) == str and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # Define a job property for your Person class.
    # If the job is invalid, the setter method should print() "Job must be in list of approved jobs." The job must be in the following list of jobs:
    def get_job(self):
        return self._job
    
    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)
