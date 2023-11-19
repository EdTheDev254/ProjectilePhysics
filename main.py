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

    def calculate_velocity(self, time):
        vx = self.initial_horizontal_velocity
        vy = self.initial_vertical_velocity - self.gravity * time
        return vx, vy

    def calculate_drag_force(self, velocity):
        drag_force = 0.5 * velocity**2
        return drag_force

    def calculate_acceleration_due_to_drag(self, velocity):
        acceleration_due_to_drag = self.calculate_drag_force(velocity)
        return acceleration_due_to_drag

def plot_trajectory_realtime(projectile, max_time):
    plt.style.use('dark_background')  # Set background to black

    plt.ion()

    fig, ax = plt.subplots()
    ax.set_title('Projectile Trajectory Simulation')
    ax.set_xlabel('Horizontal Distance (m)')
    ax.set_ylabel('Vertical Distance (m)')

    #ax.set_xlim(0, 2000)
    ax.set_xlim(0, max_time * projectile.initial_horizontal_velocity)
    ax.set_ylim(0, projectile.initial_height + 1000)

    line, = ax.plot([], [], label=f"Speed: {projectile.initial_speed} m/s\nAngle: {math.degrees(projectile.launch_angle)}°\nHeight: {projectile.initial_height} m", color='orange')  # Bright color

    # First legend (details) is fixed at the upper right
    first_legend = ax.legend(loc='upper right', facecolor='black', edgecolor='white', fontsize='small', labelcolor='white')
    ax.add_artist(first_legend)

    time = 0
    max_height = 0
    try:
        while time <= max_time:
            x, y = projectile.calculate_position(time)
            if y < 0:
                break

            line.set_xdata(list(line.get_xdata()) + [x])
            line.set_ydata(list(line.get_ydata()) + [y])

            plt.draw()
            plt.pause(0.01)

            vx, vy = projectile.calculate_velocity(time)
            velocity = math.sqrt(vx**2 + vy**2)
            acceleration_due_to_drag = projectile.calculate_acceleration_due_to_drag(velocity)
            time += 0.05

            if y > max_height:
                max_height = y

    except KeyboardInterrupt:
        pass  # Catch KeyboardInterrupt when the user closes the plot window

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

    projectile = Projectile(initial_speed, launch_angle, initial_height)

    max_simulation_time = 30
    plot_trajectory_realtime(projectile, max_simulation_time)

if __name__ == "__main__":
    main()
