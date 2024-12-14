import pytest
from final.launches import fetch_all_launches, parse_launch_data

@pytest.fixture
def mock_launch_response():
    return {
        "results": [
            {
                "id": "123",
                "name": "Mock Launch",
                "status": {"name": "Success"},
                "window_start": "2024-01-01T00:00:00Z",
                "window_end": "2024-01-01T01:00:00Z",
                "launch_service_provider": {"name": "Mock Provider"},
                "pad": {"name": "Mock Pad", "location": {"name": "Mock Location"}},
                "mission": {"orbit": "LEO"},
            }
        ],
        "next": None,
    }

def test_fetch_all_launches(monkeypatch, mock_launch_response):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data):
                self.json_data = json_data
            
            def json(self):
                return self.json_data
            
            def raise_for_status(self):
                pass  # Simulate a successful request

        return MockResponse(mock_launch_response)

    monkeypatch.setattr("requests.get", mock_get)

    launches = fetch_all_launches("https://mock-api.com", {"limit": 1})
    assert len(launches) == 1
    assert launches[0]["id"] == "123"

def test_parse_launch_data():
    launches = [
        {
            "id": "123",
            "name": "Mock Launch",
            "status": {"name": "Success"},
            "window_start": "2024-01-01T00:00:00Z",
            "window_end": "2024-01-01T01:00:00Z",
            "launch_service_provider": {"name": "Mock Provider"},
            "pad": {"name": "Mock Pad", "location": {"name": "Mock Location"}},
            "mission": {"orbit": "LEO"},
        }
    ]
    df = parse_launch_data(launches)
    assert len(df) == 1
    assert "launch_id" in df.columns

