def do_stuff(s: str) -> str:
    part1 = s[4:6] 
    part2 = s[-9:]
    return part1 + " " + part2


if __name__ == '__main__':
    str_arg = 'The AI journey is the perfect opportunity to expand one`s horizons.'
    result = do_stuff(str_arg)
    print(result)
