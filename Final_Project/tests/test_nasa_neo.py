import pytest
from final.nasa_neo import fetch_neo_data

@pytest.fixture
def mock_neo_response():
    return {
        "near_earth_objects": {
            "2024-01-01": [
                {
                    "id": "1",
                    "name": "Mock NEO",
                    "is_potentially_hazardous_asteroid": True,
                    "close_approach_data": [
                        {
                            "close_approach_date": "2024-01-01",
                            "relative_velocity": {"kilometers_per_second": "25.0"},
                            "miss_distance": {"kilometers": "400000"},
                            "orbiting_body": "Earth",
                        }
                    ],
                    "estimated_diameter": {
                        "kilometers": {
                            "estimated_diameter_min": 0.2,
                            "estimated_diameter_max": 0.4,
                        }
                    },
                }
            ]
        }
    }

def test_fetch_neo_data(monkeypatch, mock_neo_response):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data):
                self.json_data = json_data
            
            def json(self):
                return self.json_data
            
            def raise_for_status(self):
                pass  # Simulate a successful request

        return MockResponse(mock_neo_response)

    monkeypatch.setattr("requests.get", mock_get)

    df = fetch_neo_data("2024-01-01", "2024-01-02", "DEMO_KEY")
    assert len(df) == 1
    assert df.iloc[0]["name"] == "Mock NEO"

