## Final Project Proposal by Lan Wang

#### Name of Project

Near-Earth Objects and Global Space Launch Activities

#### Type of project:

API Client (A) 

#### Brief description of the purpose

This project focuses on integrating data about Near-Earth Objects (NEOs) from NASA’s API with global space launch event data from the Launch Library 2 API, enriched by external information on launch site locations and associated countries. The objective is to develop a Python package that enables users to:

1. Query and filter NASA’s NEO data (asteroids, comets) by date, size, and closest approach distance.

2. Retrieve and filter information on recent and upcoming rocket launches (e.g., SpaceX, Arianespace, Roscosmos) worldwide via the Launch Library 2 API. Users will be able to specify date ranges, launch providers, and orbit types.

3.Incorporate web-scraped data about launch sites (e.g., geographic coordinates, associated countries, and possibly administrative details) from a reliable public source (e.g., Wikipedia or a dedicated spaceports directory website).

4.Integrate these datasets to study and visualize the relationship between human space activity (frequency and nature of launches by country) and the observation or monitoring intensity of NEOs over time.

5.Perform analyses: for instance, see if there’s a correlation between the number of space launches from a region and the number or characteristics of NEOs observed or tracked during the same periods.

6.Produce summary statistics, run basic regression or correlation analysis, and present visualizations (time-series of NEO detections vs. launches, geographical distribution of launch sites, etc.).

7.Help people interest in asteroids and comets to learn recent activities

#### Links to data sources / API etc

NASA NEO (Near Earth Object) Web Service API:

Home Page: https://api.nasa.gov/ (The NEO Feed endpoint: https://api.nasa.gov/neo/rest/v1/)
Authenticaiton: This API require a key to access, but free for regist.
Provides JSON data about asteroids and comets that pass near Earth, including their size, speed, closest approach date/time, and orbiting body.

Launch Library 2 API:
Documentation: https://ll.thespacedevs.com/
Authenticaiton: This API doesn't require a key to access.
An API that provides detailed information on upcoming and historical rocket launches worldwide, including launch provider, rocket configuration, orbit type, location, and date/time.


Launch Site Data (Web Scraping):
Potential source: Wikipedia list of spaceports.
By scraping this, we can obtain a table mapping each launch site’s name to its ISO country code, region, latitude/longitude, and possibly its owner/operator.
This will allow us to link each launch (from Launch Library 2 API) to a specific country and region for aggregated analysis.


#### Outline of Technical Steps / Challenges

step1: API Client for NEO Data (NASA):

Implement functions to
Query NEO objects by a start and end date.(too many)
Filter results by asteroid size (diameter), speed, or minimum approach distance.
Convert the JSON responses into pandas DataFrames.

step2: API Client for Launch Library 2 Data:

Implement functions to
Retrieve past and upcoming launches by date range.
Filter by launch provider (e.g., NASA, SpaceX, Arianespace), mission type, or orbit type (LEO, GTO).
Handle pagination and convert JSON responses into DataFrames.

step3: Web Scraping Launch Site Information:

Use requests and BeautifulSoup to scrape a table of rocket launch sites.
Extract the launch site name, country, geographic coordinates, and possibly operational status.
Store this in a DataFrame and perform cleaning (strip whitespace, convert coordinates to numeric values).

Step4: Match together to merge
Match each launch from the Launch Library 2 API data to its corresponding launch site via name matching.
Using the matched site, add country and region information to the launch events.
Ensure country codes or names are standardized for consistent merges.
Aggregate NEO data over monthly or yearly periods, and do the same with launches per country to enable time-series or panel data analysis.

Step5: Analysis & Visualization:
Compute summary statistics:
NEO counts per month/year.
Number of launches per month/year per country/region
Time series/ regression model apply


#### Package Development & Documentation:
Organize the project into a Python package:
Modules for API queries (nasa_neo.py, launches.py)
Modules for web scraping (scraper.py) and data integration (integrator.py)
Analysis and visualization modules (analysis.py, visualization.py).

#### Are there any significant hurdles that you have doubts about? Would not solving them render the project incomplete?
It is difficult to matching launch sites from the API to scraped data, because Na value, miswriting or might be tricky if naming conventions differ. A fallback plan involves fuzzy matching or manually handling common discrepancies. And some launch events may not provide exact site details, requiring filtering or default values.
Also NEO data and launch data may have different time granularities or coverage periods. The analysis will focus on overlapping periods and highlight any data limitations. What's more, it is a great challenge to choose a long period.

