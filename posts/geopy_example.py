from geopy.distance import geodesic

# Define coordinates (latitude, longitude)
beach = (-1.980424, -80.747772)
hometown = (-2.21452000, -80.95151000)

# Calculate the distance
distance = geodesic(beach, hometown).km

print(f"Distance from beach to hometown: {distance:.2f} km")