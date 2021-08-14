class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        maxx = 0
        maxx_counter = 0
        for i in tasks:
            freq[ord(i) - ord("A")] += 1
            if maxx == freq[ord(i) - ord("A")]:
                maxx_counter += 1
            elif maxx < freq[ord(i) - ord("A")]:
                maxx = freq[ord(i) - ord("A")]
                maxx_counter = 1
        part_counter = maxx - 1
        part_len = n - (maxx_counter - 1)
        empty_slot = part_len * part_counter
        available_tasks = len(tasks) - maxx * maxx_counter
        idle_tasks = max(0, empty_slot - available_tasks)
        return len(tasks) + idle_tasks
