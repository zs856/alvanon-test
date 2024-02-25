# The number of goals achieved by two football teams in matches in a league is given in the
# form of two lists. For each match of team B, compute the total number of matches of team A
# where team A has scored less than or equal to the number of goals scored by team B in that
# match.
# Example:
# teamA = [1, 2, 3]
# teamB = [2, 4]
# Team A has played three matches and has scored teamA = [1, 2, 3] goals in each match
# respectively. Team B has played two matches and has scored teamB = [2, 4] goals in each
# match respectively. For 2 goals scored by team B in its first match, team A has 2 matches
# with scores 1 and 2. For 4 goals scored by team B in its second match, team A has 3
# matches with scores 1, 2 and 3. Hence, the answer is [2, 3].
import logging
from typing import List


class Solution:
    def has_non_integer_element(self, arr: List[int]) -> bool:
        for item in arr:
            if not isinstance(item, int):
                return True
        return False

    def find_matches(self, team_a: List[int], team_b: List[int]) -> List[int]:
        result = []
        if team_a is None or team_b is None:
            logging.error("All of the input should not be None")
            return result
        if self.has_non_integer_element(team_a) or self.has_non_integer_element(team_b):
            logging.error("non-integer element should not be contained in the input")
            return result

        for goals_b in team_b:
            count = sum(1 for goals_a in team_a if goals_a <= goals_b)
            result.append(count)
        return result


if __name__ == "__main__":
    s = Solution()
    team_a = [1, 2, 3, 4]
    team_b = [2, 4, 5]
    matches = s.find_matches(team_a, team_b)
    print(f"matches: {matches}")
