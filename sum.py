class InvalidArgumentsCount(Exception):
    pass


class InvalidArguments(Exception):
    pass


def csum(*nums):
    if len(nums) < 2:
        raise InvalidArgumentsCount("INVALID_ARGUMENTS_COUNT")

    if any(not isinstance(i, (int, float)) for i in nums):
        raise InvalidArguments("INVALID_ARGUMENTS")

    return sum(nums)


def main():
    test_cases = [
        (1,),
        (1, "2"),
        (1, 2)
    ]

    for case in test_cases:
        try:
            print(csum(*case))
        except Exception as err:
            print(err)


if __name__ == "__main__":
    main()
