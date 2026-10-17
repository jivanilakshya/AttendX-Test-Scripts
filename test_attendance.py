def test_mark_attendance():
    student_id = "STU101"
    attendance_status = "Present"

    assert student_id != ""
    assert attendance_status in ["Present", "Absent"]

    print("Attendance marking test passed.")


def test_invalid_attendance_status():
    attendance_status = "Unknown"

    assert attendance_status not in ["Present", "Absent"]

    print("Invalid attendance status test passed.")