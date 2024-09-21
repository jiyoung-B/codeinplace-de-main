# Dont' change this file


def test_load_data():
    result = load_data()
    print(f"테스트 결과 : {result}")

    assert result == [
        ("heungmin", "son", 102),
        ("jisung", "park", 99),
        ("lionel", "messi", 97)
    ]
    '''
    # '()'로 반환해서 test 실패. '[]'로 반환하도록 변환해서 확인하려면 튜플을 리스트로 변환
    # 튜플을 리스트로 변환
    transformed_result = [list(row) for row in result]
    # 기대하는 값 (리스트 형식으로)
    expected_result = [
        ["heungmin", "son", 102],
        ["jisung", "park", 99],
        ["lionel", "messi", 97]
    ]
    assert transformed_result == expected_result, f"Expected {expected_result}, but got {transformed_result}"
    '''

if __name__ == "__main__":
    try:
        from run import load_data
#        import run
        test_load_data()
        print("TEST SUCCESS")
    except Exception as e:
        print(e)
        print("TEST FAILED")
