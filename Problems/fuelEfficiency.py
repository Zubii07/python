def calculate_efficiency(km, liters):
    return km / liters

km = float(input("Enter kilometers driven: "))
liters = float(input("Enter fuel used (liters): "))
efficiency = calculate_efficiency(km, liters)
print(f"Fuel efficiency: {efficiency:.2f} km/l")

trip_data = []

while True:
    km = float(input("Enter kilometers driven: "))
    liters = float(input("Enter fuel used (liters): "))
    efficiency = calculate_efficiency(km, liters)
    trip_data.append((km, liters, efficiency))
    
    cont = input("Add another trip? (y/n): ")
    if cont.lower() != 'y':
        break


efficiencies = [trip[2] for trip in trip_data]
average_efficiency = sum(efficiencies) / len(efficiencies)
best_trip = max(trip_data, key=lambda x: x[2])

print(f"\nAverage efficiency: {average_efficiency:.2f} km/l")
print(f"Best trip: {best_trip[0]} km with {best_trip[2]:.2f} km/l")
