from .tests_in_common import *


def test_student_number_of_tickets(test_student):
    assert test_student.get_number_of_tickets() == 5
