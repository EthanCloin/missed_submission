def solve(number: int) -> bool:
    # need to check each product of every permutation of child numbers
    # could filter out those like "81 * 72" and "72 * 81"

    from itertools import permutations


    perms = permutations(str(number))

    # key = left num, val = list of right nums
    attempted_combos = {}

    for perm in perms:
        for div_idx in range(1, len(perm)):
            left_digits = perm[:div_idx]
            right_digits = perm[div_idx:]

            left_num = ""
            for l in left_digits:
                left_num += l

            right_num = ""
            for r in right_digits:
                right_num += r

            if left_num in attempted_combos.keys():
                if right_num not in attempted_combos.values():
                    attempted_combos[left_num].append(right_num)
            elif right_num in attempted_combos.keys():
                pass

            print("l: " + str(left_num))
            print("r: " + str(right_num))





    return False


if __name__ == '__main__':
    solution = solve(2187)
    print(solution)
