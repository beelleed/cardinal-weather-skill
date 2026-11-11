# Cardinal Weather

A standalone Hermes weather skill using live Open-Meteo forecasts. No API keys or third-party Python packages required.

## Install and use

Register the public tap: `hermes skills tap add beelleed/cardinal-weather-skill`

Search with `hermes skills search cardinal-weather`, inspect the result and install it using the Hermes skill hub.

Ask Hermes: Use cardinal-weather to show the Los Angeles forecast and cite the sources.

You can also run `python skills/cardinal-weather/scripts/weather.py --city "Los Angeles"` directly.

Output includes three forecast dates, daily high/low Celsius temperatures, maximum rain probability, units, source URLs, and a UTC retrieval timestamp. City lookup uses the first geocoding result; confirm the returned city/country for ambiguous names. Errors are reported instead of invented forecasts.

## Privacy and attribution

Use public city names, never private addresses. City searches and forecast coordinates are sent to Open-Meteo.

This AI-assisted course project adapts the author's own Assignment 2 Open-Meteo integration. This repository contains only the standalone weather skill.

Weather documentation: https://open-meteo.com/en/docs

Geocoding documentation: https://open-meteo.com/en/docs/geocoding-api
