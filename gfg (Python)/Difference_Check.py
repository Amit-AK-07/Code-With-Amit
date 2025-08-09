class Solution:
    def minDifference(self, arr):
        # code here
        def time_to_seconds(time_str):
            h, m, s = map(int, time_str.split(':'))
            return h * 3600 + m * 60 + s

        seconds_list = [time_to_seconds(time) for time in arr]
        seconds_list.sort()

        min_diff = 24 * 3600  # maximum seconds in a day

        for i in range(1, len(seconds_list)):
            diff = seconds_list[i] - seconds_list[i - 1]
            min_diff = min(min_diff, diff)

        wrap_diff = (24 * 3600 - seconds_list[-1]) + seconds_list[0]
        min_diff = min(min_diff, wrap_diff)

        return min_diff

        
