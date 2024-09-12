# Dont' change this file


def test_extract_data():
    result = extract_data()
    assert result == [
        ["lionel messi", 97],
        ["jisung park", 99],
        ["heungmin son", 102],
    ]


if __name__ == "__main__":
    try:
        from run import extract_data

        test_extract_data()
        print("TEST SUCCESS")
    except Exception as e:
        print(e)
        print("TEST FAILED")
