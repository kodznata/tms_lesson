import pytest
from hw19_pytest.school_code import Students
from hw19_pytest.school_code import School


@pytest.fixture(scope="class")
def new_students():
    natasha = Students("Kodz", 3, [7, 6, 7, 7, 6])
    tanya = Students("Smith", 1, [10, 10, 10, 10, 9])
    nikita = Students("Ronaldo", 2, [6, 1, 7, 5, 9])
    school = School()
    school.add_student(natasha)
    school.add_student(tanya)
    school.add_student(nikita)
    return school


class TestsSchool:

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_show_student_with_marks_positive(self, new_students):
        assert new_students.show_student_with_marks(7, 6) == \
               "Student Kodz in the 3 group has only (7, 6) marks"

    @pytest.mark.xfail
    def test_show_student_with_marks_negative(self, new_students):
        assert new_students.show_student_with_marks(3, 4) == \
               "Student Kodz in the 3 group has only (3, 4) marks"

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_show_student_with_group_positive(self, new_students):
        assert new_students.show_student_with_group(2) == \
               "Student Ronaldo is in the group 2"

    @pytest.mark.xfail
    def test_show_student_with_group_negative(self, new_students):
        assert new_students.show_student_with_group(1) == \
               "Student Ronaldo is in the group 1"

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_show_student_with_automat_positive(self, new_students):
        assert new_students.show_student_with_automat(7) == \
               "Student Smith has automat"

    @pytest.mark.skip
    def test_show_student_with_automat_negative(self, new_students):
        assert new_students.show_student_with_automat(7) == \
               "Student Ronaldo has automat"
