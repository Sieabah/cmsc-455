"""
Christopher S. Sidell
CMSC 455 - HW1 - Tyler Simon

This HW simulates a toy rocket flying into the air.
"""

class Rocket:

    # Planetary information
    atmospheric_conditions = {
        "gravity": 9.80665,#m/s^2
        "rho": 1.293 #kg/m^2
    }

    def __init__(self):
        """
        Rocket description
        :return:
        """
        self.length = 0.311 #m
        self.diameter = 0.0241 #m
        self.bodyarea = 0.000506 #m^2
        self.bodydrag = 0.45
        self.finarea = 0.00496 #m^2
        self.findrag = 0.01
        self.mass = 0.0340 #kg
        self.iengine = 0.0242 #kg
        self.fengine = 0.0094 #kg

        self.height = 0 #m
        self.velocity = 0 #m/s
        self.acceleration = 0 #m/s^2
        self.mass = self.mass + self.iengine #kg

        self.bMoved = False

        self.__time = 0
        self.__dt = 0


    def thrust(self, time):
        """
        Ft =
        :param time:
        :return:
        """
        if time < 0:
            return 0

        if time <= 0.19:
            return (74.15789473684211 * time)
        elif time <= 0.4:
            return (pow(time-0.4,2)*210 + 4.74)
        elif time <= 1.8:
            return 4.74
        elif time <= 1.85:
            return (-94.8*(time-1.85))
        else:
            return 0

    def simulate(self, time):
        """
        Simulate the rocket at time
        :param time: new time to simulate at
        :return:
        """

        # Calculate time
        self.__dt = time - self.__time
        self.__time = time

        # Get thrust
        thrust = self.thrust(time)

        # Rocket Physics
        self.acceleration = self.accel()
        self.velocity = self.v()
        self.height = self.s()

        #Burn fuel
        self.mass -= 0.0001644*thrust

        # Return rocket state
        return {
            'time': self.__time,
            'height': self.height,
            'velocity': self.velocity,
            'acceleration': self.acceleration,
            'force': self.force(),
            'mass': self.mass
        }

    def accel(self):
        """
        Get acceleration
        a = F/m
        :return:
        """
        return self.force()/self.mass

    def dv(self):
        """
        Get delta velocity
        dv = a*dt dv
        :return:
        """
        return self.accel()*self.__dt

    def v(self):
        """
        Get new velocity
        v = v+dv
        :return:
        """
        return self.velocity + self.dv()

    def ds(self):
        """
        Get delta position
        ds = v*dt
        :return:
        """
        return self.v()*self.__dt

    def s(self):
        """
        Get position
        s = s+ds
        :return:
        """
        new_height = self.height + self.ds()
        if new_height < 0:
            self.velocity = 0
            self.acceleration = 0
            return 0

        return new_height

    def force(self):
        """
        Get force at time with drag and gravity forces applied
        F = Ft - (Fd body + Fd fins + Fg)
        :return:
        """
        drag = self.force_of_drag()
        return self.thrust(self.__time) - (drag['body'] + drag['fins'] + self.force_of_gravity())

    def force_of_gravity(self):
        """
        Get force of gravity on rocket
        Fg = m*g
        :return:
        """
        return self.mass * self.atmospheric_conditions['gravity']


    def force_of_drag(self):
        """
        Get the force of drag, body & fins
        Fd = Cd*Rho*A*v^2 /2
        :return:
        """
        # Get variables
        cdbody = self.bodydrag
        areabody = self.bodyarea

        cdfins = self.findrag
        areafins = self.finarea

        # Calcualte once variables
        rho = self.atmospheric_conditions['rho'] #kg/m^3
        velocity = pow(self.velocity,2)*0.5
        rho_velocity = rho*velocity

        # Get drag forces
        body = cdbody*areabody*rho_velocity
        fins = cdfins*areafins*rho_velocity

        # Return dictionary of drag forces
        return {'body': body, 'fins': fins}

def main():
    # Setup simulation
    time_interval = 0.1
    time = 0
    rocket = Rocket()

    # Variable to save state
    endstate = None

    # simulate
    while(time_interval):

        # Simulate the rocket at time
        state = rocket.simulate(time)

        # If we're falling, quit
        if state['velocity'] < 0:
            break

        # Save new state
        endstate = state

        # Print state to console
        print state['time'], state['height'], state['velocity'], state['acceleration'], state['force'], state['mass']

        # Increment time
        time += time_interval

    print "Max height ~"+str(endstate['height'])

# Run program, catch Overflow exceptions
try:
    main()
except OverflowError, e:
    print "ERR: Numbers got too big to calculate",e
