import math
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, initial_speed, launch_angle, initial_height, time_step):
        self.initial_speed = initial_speed
        self.launch_angle = math.radians(launch_angle)
        self.initial_height = initial_height
        self.gravity = 9.8
        self.time_step = time_step
        self.calculate_initial_components()

    def calculate_initial_components(self):
        self.initial_horizontal_velocity = self.initial_speed * math.cos(self.launch_angle)
        self.initial_vertical_velocity = self.initial_speed * math.sin(self.launch_angle)

    def calculate_position(self, time):
        x = self.initial_horizontal_velocity * time
        y = self.initial_height + (self.initial_vertical_velocity * time) - (0.5 * self.gravity * time**2)
        return x, y

    def calculate_max_height(self):
        return (self.initial_vertical_velocity**2) / (2 * self.gravity)

    def calculate_max_range(self):
        return (self.initial_speed**2) * math.sin(2 * self.launch_angle) / self.gravity

    def calculate_time_of_flight(self):
        return (2 * self.initial_vertical_velocity) / self.gravity

    def timeStep(self):
        return self.time_step

def plot_trajectory_realtime(projectile, ax):
    ax.set_facecolor('black')  # Set axes background color to black
    ax.set_title('Projectile Trajectory Simulation', color='white')  # Set title color to white
    ax.set_xlabel('Horizontal Distance (m)', color='white')  # Set label color to white
    ax.set_ylabel('Vertical Distance (m)', color='white')  # Set label color to white

    # Set the color of the axes to a bright color
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')

    ax.tick_params(axis='x', colors='white')  # Set tick color to white
    ax.tick_params(axis='y', colors='white')  # Set tick color to white

    # Automatically set the initial x-axis and y-axis limits based on calculated max range and max height
    max_range = projectile.calculate_max_range()
    max_height = projectile.calculate_max_height()
    ax.set_xlim(0, max_range * 2)  # Adjusted for better visualization
    ax.set_ylim(0, max_height * 2)  # Adjusted for better visualization

    line, = ax.plot([], [], label=f"Speed: {projectile.initial_speed} m/s\nAngle: {math.degrees(projectile.launch_angle)}°\nHeight: {projectile.initial_height} m", color='orange')  # Bright color

    # First legend (details) is fixed at the upper right
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
    # Second legend (max height and range) is placed below the first one at the top right
    second_legend = ax.legend([f"Max Height: {max_height_reached:.2f} m\nRange: {range_value:.2f} m"], loc='upper right', bbox_to_anchor=(1.0, 0.8), fontsize='small', facecolor='black', edgecolor='white', labelcolor='white')
    ax.add_artist(second_legend)

    plt.ioff()
    plt.show()  # Display the final plot

def main():
    while True:
        initial_speed = float(input("Enter initial speed (m/s): "))
        launch_angle = float(input("Enter launch angle (degrees): "))
        initial_height = float(input("Enter initial height (m): "))
        time_step = float(input("Enter time step (lower values use lower time steps):"))

        # Projectile Instance
        projectile = Projectile(initial_speed, launch_angle, initial_height, time_step)

        # Set the axes limits before starting the simulation
        max_range = projectile.calculate_max_range()
        max_height = projectile.calculate_max_height()

        fig, ax = plt.subplots(facecolor='black')  # Set window background color to black
        ax.set_xlim(0, max_range + 500)  # Adjusted for better visualization
        ax.set_ylim(0, max_height + 200)  # Adjusted for better visualization

        plot_trajectory_realtime(projectile, ax)

        plt.show()  # Display the final plot

        # Ask the user if they want to calculate for another projectile
        user_input = input("Do you want to calculate for another projectile? (yes/no): ").lower()
        if user_input != 'yes':
            break

if __name__ == "__main__":
    main()
