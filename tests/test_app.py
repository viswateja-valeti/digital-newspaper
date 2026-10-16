
import unittest
from app import app

class NewspaperTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_subscription(self):
        response = self.client.post(
            "/subscribe",
            json={"name": "Ravi", "plan": "Monthly"}
        )
        self.assertEqual(response.status_code, 200)

    def test_missing_details(self):
        response = self.client.post(
            "/subscribe", json={}
        )
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
