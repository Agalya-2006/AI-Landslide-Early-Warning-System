def predict_risk(soil_moisture, rainfall):
    if soil_moisture > 70 and rainfall > 80:
        return "High Risk"
    elif soil_moisture > 50:
        return "Medium Risk"
    else:
        return "Low Risk"

soil = 75
rain = 90

print("Predicted Risk Level:", predict_risk(soil, rain))
