# -Local-Time-Based-Wallpaper-Changer-python
This script automatically selects and changes your desktop wallpaper based on the current time of day in your local timezone. It detects your location, calculates sunrise and sunset times, and switches between wallpapers like morning, noon, evening, or night. It creates a personalized and dynamic desktop experience based on time and location.




### Overview:

This script automatically selects an appropriate wallpaper image based on the current time of day at your location (like morning, noon, evening, or night). It does this by:

1. Detecting your **geographical location** and **timezone** using your IP address.
2. Fetching the **sunrise and sunset times** for your location using a free API.
3. Comparing the **current local time** with the sunrise/sunset times.
4. Choosing a wallpaper image name accordingly (e.g., `"morning.png"`, `"night.png"`).

---

### Step-by-Step Explanation:

#### 1. **Getting Your Location**

The script uses an online service that can detect your public IP address and return geographic details about it. This includes:

* The city and country you're in.
* Your **latitude** and **longitude**, which are geographical coordinates.
* Your **timezone**, which is essential to convert times from UTC to your local time.

This information helps the program know **where you are in the world**, and what time zone you're in.

---

#### 2. **Getting Sunrise and Sunset Times**

Once your coordinates are known, the script uses another online service (sunrise-sunset.org) that provides **accurate sunrise and sunset times** for any location.

* These times are returned in **UTC** (Coordinated Universal Time), not local time.
* The script converts these UTC times to your **local time**, using your timezone information from the earlier step.

---

#### 3. **Checking the Current Local Time**

The script then checks what time it is **right now** in your local timezone. This is compared with:

* The local **sunrise time**
* A fixed **noon time** (12:00 PM)
* A fixed **evening start time** (5:00 PM)
* The local **sunset time**

---

#### 4. **Choosing the Right Wallpaper**

Based on the comparison, the script chooses a wallpaper that matches the time of day. Here's how:

* If it’s **before sunrise** → `"night.png"` is selected.
* If it’s **after sunrise but before noon** → `"morning.png"` is selected.
* If it’s **after noon but before 5 PM** → `"noon.png"` is selected.
* If it’s **after 5 PM but before sunset** → `"evening.png"` is selected.
* If it’s **after sunset** → `"night.png"` is selected again.

---

#### 5. **Displaying the Result**

At the end, the script prints:

* Your location (city and country).
* Your timezone.
* The current local time, sunrise time, and sunset time.
* And finally, the name of the selected wallpaper image.

---

### Purpose of the Script:

This kind of script is useful for **automatically updating a background image or theme** on your device to reflect the current time of day, giving a more dynamic and personalized visual experience.

