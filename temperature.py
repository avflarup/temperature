import requests
import numpy as np
import matplotlib.pyplot as plt

URL = "https://opendataapi.dmi.dk/v2/metObs/collections/observation/items"
params = {
    "parameterId": "temp_mean_past1h",
    "stationId": "06070", # Århus Lufthavn
    #"limit": 1000 # Uncomment to fetch more or fewer data points. 1000 is the default limit.
    }

def fetch_temperature_data(URL, params):
    r = requests.get(URL, params=params)
    return r.json() 

def plot_temperature_data(data):
    times = [item['properties']['observed'] for item in data['features']][::-1]  # Reverse to get chronological order
    temperatures = [item['properties']['value'] for item in data['features']][::-1]  # Reverse to match times
    
    plt.plot(times, temperatures, color='r')
    plt.title('Temperature Over Time at Århus Lufthavn')
    plt.xlabel('Date')
    plt.ylabel('Temperature [°C]')
    spaced_dates = [times[i] for i in np.linspace(0, len(times)-1, 10, dtype=int)] # Show 10 evenly spaced dates
    only_dates = [date.split('T')[0] for date in spaced_dates] # Extract just the date part
    plt.xticks(spaced_dates, only_dates, rotation=45) 
    plt.grid()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    data = fetch_temperature_data(URL, params)
    plot_temperature_data(data)