import requests
from datetime import datetime
import pytz

#Function to get location and timezone based on IP
def get_location():
    ip_api_url = "http://ip-api.com/json"
    response = requests.get(ip_api_url)
    data = response.json()

    latitude = data['lat']
    longitude = data['lon']
    timezone_str = data['timezone']  

    print(f"Location: {data['city']}, {data['country']} (Lat: {latitude}, Lon: {longitude})")
    print(f"Timezone: {timezone_str}")

    return latitude, longitude, timezone_str

def get_sun_times(latitude, longitude):
    today = datetime.utcnow().date()
    formatted_date = today.strftime('%Y-%m-%d')

    url = f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&date={formatted_date}&formatted=0"
    response = requests.get(url)
    data = response.json()

    sunrise = datetime.fromisoformat(data['results']['sunrise'])
    sunset = datetime.fromisoformat(data['results']['sunset'])

    return sunrise, sunset

def get_wallpaper(sunrise, sunset, timezone_str):
    local_timezone = pytz.timezone(timezone_str)

    current_utc_time = datetime.utcnow().replace(tzinfo=pytz.utc)
    current_local_time = current_utc_time.astimezone(local_timezone)

    sunrise_local = sunrise.astimezone(local_timezone)
    sunset_local = sunset.astimezone(local_timezone)

    print(f"\nCurrent Local Time: {current_local_time.strftime('%H:%M:%S')}")
    print(f"Sunrise Local Time: {sunrise_local.strftime('%H:%M:%S')}")
    print(f"Sunset Local Time: {sunset_local.strftime('%H:%M:%S')}\n")

    noon = sunrise_local.replace(hour=12, minute=0, second=0, microsecond=0)
    evening_start = sunset_local.replace(hour=17, minute=0, second=0, microsecond=0)

    if current_local_time < sunrise_local:
        return "night.png"
    elif sunrise_local <= current_local_time < noon:
        return "morning.png"
    elif noon <= current_local_time < evening_start:
        return "noon.png"
    elif evening_start <= current_local_time < sunset_local:
        return "evening.png"
    else:
        return "night.png"

def main():
    latitude, longitude, timezone_str = get_location()

    sunrise, sunset = get_sun_times(latitude, longitude)

    wallpaper = get_wallpaper(sunrise, sunset, timezone_str)

    print(f"Selected Wallpaper: {wallpaper}")

if __name__ == "__main__":
    main()

