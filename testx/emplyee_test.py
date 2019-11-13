from attribute_test import Employee


def test_empusername():
    emp = Employee()
    emp.username = "Nilesh"
    emp.password = "Nilesh"
    assert emp.username is  None
    assert emp.password is not None


