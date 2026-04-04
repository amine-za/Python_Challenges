def find_fewest_coins(coins, target):
    memo = {}

    if target < 0:
        raise ValueError("target can't be negative")
        

    def helper(target):
        if target == 0:
            return []

        if target in memo:
            return memo[target]

        best = None

        for coin in list(reversed(coins)):
            if coin <= target:
                try:
                    result = helper(target - coin)
                    candidate = result + [coin]

                    if best is None or len(candidate) < len(best):
                        best = candidate
                except ValueError:
                    continue

        if best is None:
            raise ValueError("can't make target with given coins")

        memo[target] = best
        return best

    return helper(target)