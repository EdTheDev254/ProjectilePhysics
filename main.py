import math
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, initial_speed, launch_angle, initial_height, time_step):
        # Projectile parameters
        self.initial_speed = initial_speed
        self.launch_angle = math.radians(launch_angle)
        self.initial_height = initial_height
        self.gravity = 9.8
        self.time_step = time_step
        self.calculate_initial_components()

    def calculate_initial_components(self):
        # Calculate initial horizontal and vertical components of velocity
        self.initial_horizontal_velocity = self.initial_speed * math.cos(self.launch_angle)
        self.initial_vertical_velocity = self.initial_speed * math.sin(self.launch_angle)

    def calculate_position(self, time):
        # Calculate projectile position at a given time
        x = self.initial_horizontal_velocity * time
        y = self.initial_height + (self.initial_vertical_velocity * time) - (0.5 * self.gravity * time**2)
        return x, y

    def calculate_max_height(self):
        # Calculate the maximum height of the projectile
        return (self.initial_vertical_velocity**2) / (2 * self.gravity)

    def calculate_max_range(self):
        # Calculate the maximum horizontal range of the projectile
        return (self.initial_speed**2) * math.sin(2 * self.launch_angle) / self.gravity

    def calculate_time_of_flight(self):
        # Calculate the total time of flight for the projectile
        return (2 * self.initial_vertical_velocity) / self.gravity

    def timeStep(self):
        # Get the time step for the simulation
        return self.time_step

def plot_trajectory_realtime(projectile, ax):
    # Set up plot aesthetics
    ax.set_facecolor('black')
    ax.set_title('Projectile Trajectory Simulation', color='white')
    ax.set_xlabel('Horizontal Distance (m)', color='white')
    ax.set_ylabel('Vertical Distance (m)', color='white')

    # Set axis color
    for spine in ax.spines.values():
        spine.set_color('white')

    # Set tick color
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Calculate max range and max height for setting plot limits
    max_range = projectile.calculate_max_range()
    max_height = projectile.calculate_max_height()
    ax.set_xlim(0, max_range * 2)
    ax.set_ylim(0, max_height * 2)

    # Plot trajectory with initial information
    line, = ax.plot([], [], label=f"Speed: {projectile.initial_speed} m/s\nAngle: {math.degrees(projectile.launch_angle)}°\nHeight: {projectile.initial_height} m", color='orange')

    # Add legends
    first_legend = ax.legend(loc='upper right', fontsize='small', facecolor='black', edgecolor='white', labelcolor='white')
    ax.add_artist(first_legend)

    time = 0
    max_height_reached = 0
    max_range_reached = 0

    # Use a larger time step for faster simulation
    dt = projectile.timeStep()

    # Use the 'close_event' flag to check if the plot window is closed
    close_event = False
    
    def on_close(event):
        nonlocal close_event
        close_event = True

    fig = plt.gcf()
    fig.canvas.mpl_connect('close_event', on_close)

    while not close_event:
        x, y = projectile.calculate_position(time)

        line.set_xdata(list(line.get_xdata()) + [x])
        line.set_ydata(list(line.get_ydata()) + [y])

        # Update max_height_reached and max_range_reached
        if y > max_height_reached:
            max_height_reached = y
        if x > max_range_reached:
            max_range_reached = x

        plt.draw()
        plt.pause(0.01)

        time += dt

        # Break the loop if the projectile hits the ground
        if y < 0:
            break

    range_value = x
    # Add second legend for max height and range
    second_legend = ax.legend([f"Max Height: {max_height_reached:.2f} m\nRange: {range_value:.2f} m"], loc='upper right', bbox_to_anchor=(1.0, 0.8), fontsize='small', facecolor='black', edgecolor='white', labelcolor='white')
    ax.add_artist(second_legend)

    plt.ioff()
    plt.show()  # Display the final plot

def main():
    while True:
        # Get user input for projectile parameters
        initial_speed = float(input("Enter initial speed (m/s): "))
        launch_angle = float(input("Enter launch angle (degrees): "))
        initial_height = float(input("Enter initial height (m): "))
        time_step = float(input("Enter time step (lower values use lower time steps):"))

        # Create Projectile instance
        projectile = Projectile(initial_speed, launch_angle, initial_height, time_step)

        # Set the axes limits before starting the simulation
        max_range = projectile.calculate_max_range()
        max_height = projectile.calculate_max_height()

        # Create plot
        fig, ax = plt.subplots(facecolor='black')
        ax.set_xlim(0, max_range + 500)
        ax.set_ylim(0, max_height + 200)

        # Perform real-time trajectory simulation
        plot_trajectory_realtime(projectile, ax)

        # Ask the user if they want to calculate for another projectile
        user_input = input("Do you want to calculate for another projectile? (yes/no): ").lower()
        if user_input != 'yes':
            break

if __name__ == "__main__":
    main()
