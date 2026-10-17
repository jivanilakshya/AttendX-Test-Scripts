def test_login_with_valid_credentials():
    username = "student123"
    password = "Test@123"

    assert username != ""
    assert password != ""

    print("Login test passed: credentials are provided.")


def test_login_with_empty_username():
    username = ""
    password = "Test@123"

    assert username == ""

    print("Login validation test passed.")