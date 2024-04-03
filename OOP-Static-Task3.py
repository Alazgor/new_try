class TimeUtils:
    @staticmethod
    def time_to_seconds(time_str):
        """
        Convert a time string in the format hh:mm:ss to total number of seconds.
        """
        # Split the time string into hours, minutes, and seconds
        hours, minutes, seconds = map(int, time_str.split(':'))

        # Calculate total seconds
        total_seconds = (hours * 3600) + (minutes * 60) + seconds

        return total_seconds


# Example usage:
time_str = "12:30:45"
total_seconds = TimeUtils.time_to_seconds(time_str)
print(f"The total number of seconds in {time_str} is {total_seconds} seconds.")
