# Advanced Artificial Rain (Cloud Seeding) Simulation

def artificial_rain():
    print("======================================")
    print(" Advanced Artificial Rain Simulator")
    print("======================================")

    humidity = float(input("Enter Humidity (%): "))
    cloud = float(input("Enter Cloud Coverage (%): "))
    temperature = float(input("Enter Temperature (°C): "))
    wind = float(input("Enter Wind Speed (km/h): "))

    score = 0

    if humidity >= 70:
        score += 30
    elif humidity >= 50:
        score += 15

    if cloud >= 60:
        score += 30
    elif cloud >= 40:
        score += 15

    if 15 <= temperature <= 30:
        score += 20
    else:
        score += 10

    if wind <= 20:
        score += 20
    elif wind <= 40:
        score += 10

    print("\n----- Analysis Report -----")
    print(f"Success Score: {score}/100")

    if score >= 80:
        print("Cloud seeding is highly recommended.")
        print("Expected Rainfall: Heavy Rain")
    elif score >= 60:
        print("Cloud seeding may be successful.")
        print("Expected Rainfall: Moderate Rain")
    elif score >= 40:
        print("Low probability of artificial rain.")
        print("Expected Rainfall: Light Rain")
    else:
        print("Conditions are not suitable for cloud seeding.")
        print("Expected Rainfall: No Rain")

    print("----------------------------")
    print("Simulation Completed.")

# Run the program
artificial_rain()
