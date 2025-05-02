import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from datetime import datetime

# Create figure for plotting
fig, ax = plt.subplots()
times = []
humidities = []

# This function is called periodically from FuncAnimation
def update(frame):
    current_time = datetime.now().strftime('%H:%M:%S')
    humidity = random.uniform(30, 80)

    times.append(current_time)
    humidities.append(humidity)

    # Limit x and y lists to 20 items
    times_trimmed = times[-20:]
    humidities_trimmed = humidities[-20:]

    ax.clear()
    ax.plot(times_trimmed, humidities_trimmed, marker='o', color='blue')
    ax.set_ylim(25, 85)
    ax.set_xlabel("Time")
    ax.set_ylabel("Humidity (%)")
    ax.set_title("Real-Time Humidity Readings")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

# Set up animation
ani = animation.FuncAnimation(fig, update, interval=1000)

plt.show()