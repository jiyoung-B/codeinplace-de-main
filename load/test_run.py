# Dont' change this file


def test_load_data():
    result = load_data()
    print(f"테스트 결과 : {result}")

    assert result == [
        ["heungmin", "son", 102],
        ["jisung", "park", 99],
        ["lionel", "messi", 97]
    ]

if __name__ == "__main__":
    try:
        from run import load_data
#        import run
        test_load_data()
        print("TEST SUCCESS")
    except Exception as e:
        print(e)
        print("TEST FAILED")
