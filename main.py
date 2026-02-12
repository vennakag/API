import requests

# Ask user for a country name
country = input("Enter a country name: ")

# API endpoint
url = f"https://restcountries.com/v3.1/name/{country}"

# Send GET request
response = requests.get(url)

# Convert response to JSON
data = response.json()

# The API returns a list, so take the first result
country_data = data[0]

# Extract information
name = country_data["name"]["common"]
capital = country_data["capital"][0]
population = country_data["population"]
region = country_data["region"]

# Print results
print("\nCountry Information:")
print("Name:", name)
print("Capital:", capital)
print("Population:", population)
print("Region:", region)
