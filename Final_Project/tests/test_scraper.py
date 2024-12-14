import pytest
from final.scraper import scrape_launch_sites

def test_scrape_launch_sites(monkeypatch):
    mock_html = """
    <table class="wikitable">
        <tr>
            <th>Country</th><th>Location</th><th>Coordinates</th>
            <th>Operational date</th><th>Number of rocket launches</th>
            <th>Heaviest rocket launched</th><th>Highest achieved altitude</th><th>Notes</th>
        </tr>
        <tr>
            <td>Mock Country</td><td>Mock Location</td><td>0.0N, 0.0E</td>
            <td>2020-2024</td><td>10</td><td>1000 kg</td><td>LEO</td><td>Mock Notes</td>
        </tr>
    </table>
    """

    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, text):
                self.text = text
            
            def raise_for_status(self):
                pass  # Simulate a successful request

        return MockResponse(mock_html)

    monkeypatch.setattr("requests.get", mock_get)

    df = scrape_launch_sites("https://mock-wikipedia.com")
    assert len(df) == 1
    assert df.iloc[0]["Location"] == "Mock Location"
    assert df.iloc[0]["Country"] == "Mock Country"
