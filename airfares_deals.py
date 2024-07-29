def find_second_lowest_airfares(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # Parse the data and store it in a list of tuples
        flights = []
        for line in lines:
            datetime, origin, destination, airfare = line.strip().split(',')
            airfare = float(airfare)  # Convert airfare to float
            flights.append((datetime, origin, destination, airfare))
        
        # Sort the flights based on the airfare
        flights.sort(key=lambda x: x[3])
        
        # Find the second lowest airfare
        if len(flights) < 2:
            print("Not enough data to determine the second lowest airfare.")
            return
        
        lowest_airfare = flights[0][3]
        second_lowest_airfare = None
        
        for flight in flights:
            if flight[3] > lowest_airfare:
                second_lowest_airfare = flight[3]
                break
        
        if second_lowest_airfare is None:
            print("No second lowest airfare found.")
            return
        
        # Display the flights with the second lowest airfare
        print("Flights with the second lowest airfare:")
        for flight in flights:
            if flight[3] == second_lowest_airfare:
                print(f"Date/Time: {flight[0]}, Origin: {flight[1]}, Destination: {flight[2]}, Airfare: {flight[3]}")
    
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    filename = "airfares.txt"
    find_second_lowest_airfares(filename)
