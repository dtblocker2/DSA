class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Pair numbers with their original indices
        indexed = [(num, i) for i, num in enumerate(nums)]

        # Step 2: Sort by value descending, take top k elements
        top_k = sorted(indexed, key=lambda x: x[0], reverse=True)[:k]

        # Step 3: Sort those top k elements by their original index
        top_k.sort(key=lambda x: x[1])

        # Step 4: Extract the values
        return [num for num, _ in top_k]
