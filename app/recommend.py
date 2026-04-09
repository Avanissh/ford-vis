import json


# Load structured vehicle data
def load_vehicles():
    with open("data/vehicles.json") as f:
        return json.load(f)


vehicles = load_vehicles()


def recommend_vehicle(query):
    query = query.lower()

    results = []

    for v in vehicles:
        score = 0
        reasons = []

        # 🔹 Family logic
        if "family" in query:
            if v["seats"] >= 5:
                score += 1
                reasons.append("suitable seating capacity")

        # 🔹 SUV preference
        if "suv" in query:
            if v["type"] == "SUV":
                score += 1
                reasons.append("SUV type preferred")

        # 🔹 Pickup / towing
        if "towing" in query or "pickup" in query:
            if v["type"] == "Pickup":
                score += 1
                reasons.append("good for towing")

        # 🔹 Sport
        if "sport" in query or "performance" in query:
            if v["type"] == "Coupe":
                score += 1
                reasons.append("performance oriented")

        if score > 0:
            results.append({
                "model": v["model"],
                "score": score,
                "reason": ", ".join(reasons)
            })

    # sort by score
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    # return top 2
    return results[:2]