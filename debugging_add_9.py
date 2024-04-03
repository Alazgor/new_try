# Function to determine if we sleep in
def sleep_in(weekday, vacation):
    return not weekday or vacation

result = sleep_in(False, False)
print(result)