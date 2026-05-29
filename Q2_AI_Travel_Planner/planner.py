from .knowledge_base import KnowledgeBaseManager

class TravelPlanner:
    def __init__(self):
        self.kb = KnowledgeBaseManager()

    def generate_itinerary(self, destination, max_budget, prefers_wine=False):
        """
        AI Decision Logic: Filters and curates an itinerary using crossed-domain data
        against user constraints.
        """
        raw_options = self.kb.query_activities_and_pairings(destination)
        
        itinerary = {
            "destination": destination,
            "activities": [],
            "dining_recommendations": [],
            "total_cost": 0
        }
        
        current_budget = max_budget

        for row in raw_options:
            activity = row.activity.split("#")[-1]
            cost = int(row.cost)
            
            # Check constraints (Cost assessment)
            if cost <= current_budget:
                itinerary["activities"].append({"name": activity, "cost": cost})
                itinerary["total_cost"] += cost
                current_budget -= cost
                
            # Cross-domain knowledge Reuse (Food & Wine pairing validation)
            if row.food and row.wine:
                food_item = row.food.split("#")[-1]
                wine_pair = row.wine.split("#")[-1]
                
                dining_rec = f"Try {food_item}"
                if prefers_wine:
                    dining_rec += f" paired perfectly with a glass of {wine_pair}"
                    
                if dining_rec not in itinerary["dining_recommendations"]:
                    itinerary["dining_recommendations"].append(dining_rec)
                    
        return itinerary
