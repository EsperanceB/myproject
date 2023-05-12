# Task on beginner programming with functions
print("Estimate your holiday expenses, easily and quickly!")
print("""Here is an application to help you avoid surprise on the cost of your holidays.
      \nOur holiday destinations are Paris, Dubai, London, Cape Town and New York.
       \nMake your choice and we do the reste about the estimation for the cost of your holiday!\n """)



# Function to calculate the total cost of hotel here I took arbitrary 120 as the cost of one night. 
# The number of nights will be given by the user 

def hotel_cost(num_nights):
    total_cost_hotel = num_nights*120
    return total_cost_hotel

# Function that return the plane cost which depends on the city the user will enter

def plane_cost(city_flight):
    cost = city_flight_cost[city_flight]
       
    return cost

# Function that return the total cost of car rent, arbitrary I used 50 as the car rent cost per day

def car_rental(rental_days):
    daily_rent = 50
    total_cost_for_rent = daily_rent*rental_days
    return total_cost_for_rent

# Function that return the total cost of the holiday
# Here you have the other functions name as arguments but remembering the scope, we could have used different names and get the same result

def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_cost_holiday = hotel_cost + plane_cost + car_rental
    return total_cost_holiday

# Defining the inputs outsides of functions to make it possible to be used globally
# Just to ensure the user has a chance to re-enter the input I've used what I've learnt in defensive programming
city_flight_cost = {"Paris":300, "Dubai":400, "London":350, "Cape Town":380,"New York": 420}  # I defined a dictionary that is not exaustive just as an exemple
while True:
    try:
        city_flight = (input("Please enter the city :")).capitalize()  # The capitalize function to make sure the user input correspond to the keys in the dictionary 
        num_nights = int(input("Number of nights: "))
        rental_days = int(input("Rental days: "))

        # Finally print out the total cost to the user

        #if city_flight in city_flight_cost:
        print(f"The total cost of your holiday is {holiday_cost(hotel_cost(num_nights), plane_cost(city_flight), car_rental(rental_days))} £")
        break

    except KeyError:
        print("Enter a valide city please! ")
    except ValueError:
        print("Oops enter the correct value please! ")
    except Exception:
        print("Something went wrong, please try again! ")
    # This is not an exaustive application more choice can be provided, like hotels with their range of pricing,car model to rent and its price, curency etc