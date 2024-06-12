
class Drone:
    def __init__(self, id, location):
        self.id = id
        self.location = location

    def update_location(self, new_location):
        self.location = new_location

class Migrant:
    def __init__(self, id, location):
        self.id = id
        self.location = location

def track_migrants(drones, migrants):
    for drone in drones:
        for migrant in migrants:
            if is_nearby(drone.location, migrant.location):
                print(f"Drone {drone.id} has detected migrant {migrant.id} at location {migrant.location}")

def is_nearby(location1, location2, threshold=1.0):
    return abs(location1 - location2) <= threshold

def main():
    # Example setup
    drones = [Drone(id=1, location=0.0), Drone(id=2, location=5.0)]
    migrants = [Migrant(id=1, location=0.5), Migrant(id=2, location=6.0)]

    print("Tracking Migrants using Drones")
    track_migrants(drones, migrants)

if __name__ == "__main__":
    main()
