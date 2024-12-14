# final
Detail thing please refer to README FINAL project.ipynb

This package provides an API client for retrieving and analyzing:
- NASA Near-Earth Objects (NEO) data
- Rocket launch data from Launch Library 2
- Launch site information from a public webpage (scraped data)


## Installation

```bash
$ pip install final
```

## Usage

from final.nasa_neo import fetch_neo_data

df = fetch_neo_data("2024-01-01", "2024-01-07", api_key="YOUR_API_KEY")
print(df.head())


from final.launches import fetch_all_launches, parse_launch_data

base_url = "https://ll.thespacedevs.com/2.2.0/launch/"
params = {"window_start__gte": "2024-01-01", "window_end__lte": "2024-01-31"}
launches = fetch_all_launches(base_url, params)
launch_df = parse_launch_data(launches)
print(launch_df.head())

from final.scraper import scrape_launch_sites

url = "https://en.wikipedia.org/wiki/List_of_rocket_launch_sites"
site_df = scrape_launch_sites(url)
print(site_df.head())




- TODO

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`final` was created by Lan Wang. It is licensed under the terms of the MIT license.

## Credits

`final` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

