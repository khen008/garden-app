# Function to generate gardening advice based on season and plant type
def get_gardening_advice(season, plant_type):

    # Variable to hold gardening advice
    advice = ""

    # Determine advice based on the season
    if season == "summer":
        advice += "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        advice += "Protect your plants from frost with covers.\n"
    else:
        advice += "No advice for this season.\n"

    # Determine advice based on the plant type
    if plant_type == "flower":
        advice += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        advice += "Keep an eye out for pests!"
    else:
        advice += "No advice for this type of plant."

    return advice


# Hardcoded values for now (can be replaced with input later)
season = "summer"
plant_type = "flower"

# Call the function
advice = get_gardening_advice(season, plant_type)

# Print the generated advice
print(advice)