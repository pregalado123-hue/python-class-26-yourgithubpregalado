# Starting file for LAB 7
# CS 31-Lab
# Date: November 15, 2026
# Excercises 7-1 and 7-2 

import csv 

def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used

def read_trips():
    trips = []
    try:
        with open("trips.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                trips.append([float(row[0]), float(row[1]), float(row[2])])
    except FileNotFoundError:
        print("No previous trip data found.")
    return trips
def write_trips(trips):
    with open("trips.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(trips)
def list_trips(trips):
    print("Distance\tGallons\tMPG")
    for trip in trips:
        print(f"{trip[0]}\t{trip[1]}\t{trip[2]}")

def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    # Get the saved trips 
    trips = read_trips()
    list_trips(trips)
    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()
        # Add the trip to the list
        trip = [miles_driven, gallons_used, mpg]
        trips.append(trip)
        write_trips(trips)
        list_trips(trips)
        
        more = input("More entries? (y or n): ")
    print("Bye!")

if __name__ == "__main__":
    main()
