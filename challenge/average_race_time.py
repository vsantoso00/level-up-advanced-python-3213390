# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    rhines_times = []  # Initialize an empty list to store
    races = get_data()
    def get_time(line): # creates a regex to find the time in the format mm:ss:M
        return re.findall(r'\d{2}:\S+', line)[0]  # Regex to match times in mm:ss:M format
    for line in races.splitlines(): # Split the data into lines and loop through each line
        
        if "Jennifer Rhines" in line: # Check if the line contains Jennifer Rhines' name
            rhines_times.append(get_time(line))  # If it does, extract the time using the get_time function and append it to the list
        else:
            pass  
    return rhines_times     # Return the list of times
    

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    
    total_ms = 0  # Initialize total seconds to 0
    
    for time in racetimes:  # Loop through each time in the list
        try:
            minutes, seconds, milli = re.split(r'[:.]',time)  # Split the time into minutes and seconds and milliseconds
            total_ms += ((int(minutes) * 60 + int(seconds))*1000 ) + int(milli) 
        
        except ValueError: 
            minutes, seconds = re.split(r'[:]',time)  # Split the time into minutes and seconds
            total_ms += (int(minutes) * 60 + int(seconds))*1000  
    
    
    avg_ms = total_ms // len(racetimes)
    avg_mins = avg_ms // 60000
    avg_secs = (avg_ms % 60000) // 1000
    avg_ms_digit = (avg_ms % 1000) // 100
    return f"{avg_mins:02}:{avg_secs:02}.{avg_ms_digit}" 
    
#print(get_rhines_times(get_data()))  # Test the function to see if it returns the correct times
#print(get_average())  # Test the function to see if it returns the correct average seconds
