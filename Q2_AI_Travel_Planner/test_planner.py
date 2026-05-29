import unittest
from src.planner import TravelPlanner

class TestTravelPlanner(unittest.TestCase):
    def setUp(self):
        self.planner = TravelPlanner()

    def test_bordeaux_wine_trip(self):
        # A user going to Bordeaux who loves wine with a decent budget
        plan = self.planner.generate_itinerary("Bordeaux", max_budget=100, prefers_wine=True)
        
        self.assertEqual(plan["destination"], "Bordeaux")
        self.assertIn("ChateauTour", [a["name"] for a in plan["activities"]])
        self.assertTrue(any("CabernetSauvenon" in item for item in plan["dining_recommendations"]))
        self.assertLessEqual(plan["total_cost"], 100)

    def test_budget_cutoff(self):
        # Budget too low for the Eiffel Tower (costs 25)
        plan = self.planner.generate_itinerary("Paris", max_budget=10, prefers_wine=False)
        self.assertEqual(len(plan["activities"]), 0)
        self.assertEqual(plan["total_cost"], 0)

if __name__ == '__main__':
    unittest.main()
