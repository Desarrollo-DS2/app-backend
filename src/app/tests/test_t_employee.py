from .tests_in_common import *

def test_employee_role(test_employee):
    assert test_employee.get_role() == 'Gerente'