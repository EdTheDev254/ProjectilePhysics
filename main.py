import math
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, initial_speed, launch_angle, initial_height):
        self.initial_speed = initial_speed
        self.launch_angle = math.radians(launch_angle)
        self.initial_height = initial_height
        self.gravity = 9.8
        self.calculate_initial_components()

    def calculate_initial_components(self):
        self.initial_horizontal_velocity = self.initial_speed * math.cos(self.launch_angle)
        self.initial_vertical_velocity = self.initial_speed * math.sin(self.launch_angle)

    def calculate_position(self, time):
        x = self.initial_horizontal_velocity * time
        y = self.initial_height + (self.initial_vertical_velocity * time) - (0.5 * self.gravity * time**2)
        return x, y

def plot_trajectory_realtime(projectile, max_height_threshold, max_range_threshold):
    plt.style.use('dark_background')  # Set background to black

    plt.ion()

    fig, ax = plt.subplots()
    ax.set_title('Projectile Trajectory Simulation')
    ax.set_xlabel('Horizontal Distance (m)')
    ax.set_ylabel('Vertical Distance (m)')

    ax.set_xlim(0, max_range_threshold)  # Initial x-axis limit
    ax.set_ylim(0, max_height_threshold)  # Initial y-axis limit

    line, = ax.plot([], [], label=f"Speed: {projectile.initial_speed} m/s\nAngle: {math.degrees(projectile.launch_angle)}°\nHeight: {projectile.initial_height} m", color='orange')  # Bright color

    # First legend (details) is fixed at the upper right
    first_legend = ax.legend(loc='upper right', facecolor='black', edgecolor='white', fontsize='small', labelcolor='white')
    ax.add_artist(first_legend)

    time = 0
    max_height = 0
    max_range = 0
    try:
        while True:
            x, y = projectile.calculate_position(time)

            # Break the loop if the projectile hits the ground
            if y < 0:
                break

            line.set_xdata(list(line.get_xdata()) + [x])
            line.set_ydata(list(line.get_ydata()) + [y])

            # Update max_height and max_range
            if y > max_height:
                max_height = y
            if x > max_range:
                max_range = x

            plt.draw()
            plt.pause(0.01)

            time += 0.05

    except KeyboardInterrupt:
        pass  # Catch KeyboardInterrupt when the user closes the plot window

    # ... (previous code)

    range_value = x
    # Second legend (max height and range) is placed below the first one at the top right
    second_legend = ax.legend([f"Max Height: {max_height:.2f} m\nRange: {range_value:.2f} m"], loc='upper right', bbox_to_anchor=(1.0, 0.8), facecolor='black', edgecolor='white', fontsize='small', labelcolor='white')
    ax.add_artist(second_legend)

    plt.ioff()
    plt.show()

def main():
    initial_speed = float(input("Enter initial speed (m/s): "))
    launch_angle = float(input("Enter launch angle (degrees): "))
    initial_height = float(input("Enter initial height (m): "))
    
    # Set the threshold values for max height and max range
    max_height_threshold = float(input("Enter the maximum height threshold (m): "))
    max_range_threshold = float(input("Enter the maximum range threshold (m): "))

    projectile = Projectile(initial_speed, launch_angle, initial_height)

    plot_trajectory_realtime(projectile, max_height_threshold, max_range_threshold)

if __name__ == "__main__":
    main()
