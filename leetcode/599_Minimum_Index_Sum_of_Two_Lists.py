from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # reduce space complexity
        if len(list1) > len(list2):
            return self.findRestaurant(list2, list1)

        d1 = dict([(v, i) for i, v in enumerate(list1)])

        result = []
        least_index = len(list1) + len(list2)
        for i, v in enumerate(list2):
            if v not in d1:
                continue

            index = i + d1[v]
            if index == least_index:
                result.append(v)
            elif index < least_index:
                least_index = index
                result = [v]

        return result


def check_cases(s: Solution):
    assert (
        sorted(
            s.findRestaurant(
                ["Shogun", "Tapioca Express", "Burger King", "KFC"],
                [
                    "Piatti",
                    "The Grill at Torrey Pines",
                    "Hungry Hunter Steakhouse",
                    "Shogun",
                ],
            )
        )
        == sorted(["Shogun"])
    )

    assert (
        sorted(
            s.findRestaurant(
                ["Shogun", "Tapioca Express", "Burger King", "KFC"],
                ["KFC", "Shogun", "Burger King"],
            )
        )
        == sorted(["Shogun"])
    )

    assert (
        sorted(
            s.findRestaurant(
                ["Shogun", "Tapioca Express", "Burger King", "KFC"],
                ["KFC", "Burger King", "Tapioca Express", "Shogun"],
            )
        )
        == sorted(["KFC", "Burger King", "Tapioca Express", "Shogun"])
    )

    assert (
        sorted(
            s.findRestaurant(
                ["Shogun", "Tapioca Express", "Burger King", "KFC"],
                ["KNN", "KFC", "Burger King", "Tapioca Express", "Shogun"],
            )
        )
        == sorted(["KFC", "Burger King", "Tapioca Express", "Shogun"])
    )

    assert sorted(s.findRestaurant(["KFC"], ["KFC"])) == sorted(["KFC"])


def test_solution():
    check_cases(Solution())
