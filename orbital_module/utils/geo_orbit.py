from astropy import units as u
from astropy.time import Time
from astropy.coordinates import get_body_barycentric, solar_system_ephemeris

from poliastro.bodies import Earth, Sun
from poliastro.twobody import Orbit
from poliastro.twobody.sampling import EpochsArray
from poliastro.twobody.propagation import CowellPropagator
from poliastro.util import time_range
from poliastro.earth import EarthSatellite
from poliastro.earth.plotting import GroundtrackPlotter
from astropy.coordinates import get_body_barycentric_posvel
from poliastro.ephem import Ephem


from poliastro.core.events import eclipse_function
from poliastro.twobody.events import UmbraEvent

import plotly.graph_objects as go

import matplotlib.pyplot as plt

import pyvista as pv
from matplotlib.colors import ListedColormap
import numpy as np

import pandas as pd

from tabulate import tabulate

import webbrowser

from .utils import rv_to_nu, R_x, R_y, R_z, R_euler_zxz


class GeoOrbit:
    """Define geo-orbit, get a 3D Orbit view, get groundtrack, get ephems and get umbra positions.
    
    Attributes:
        name (str): Orbit tag
        a (Quantity): Semi-major axis
        ecc (Quantity): Eccentricity
        inc (Quantity): Inclination
        raan (Quantity): Longitude of the ascending node
        argp (Quantity): Argument of periapsis
        nu (Quantity): True Anomaly
        start_epoch (time): Start epoch of the orbit 
        end_epoch (time): End epoch of the orbit propagator
        body (Body): Main attractor
        T (Quantity): Orbit Period
        N (int): Sample points
        ephem (): Ephemerides of the orbit during the propagated epoch
        ephem_coord (): Ephemerides Coordinates
        ephem_epochs (Time): Ephemerides epochs
    """
    
    global method#,N
    #N = 500 # Sample points
    method = CowellPropagator() # Propagator method
    
    def __init__(self, name: str):
        """
        Initialize the GeoOrbit class with a name.

        Args:
            name (str): Name of the orbit.
        """
        
        self.name = name
    
    def define_orbit(self, a, ecc, inc, raan, argp, nu, start_epoch, end_epoch, orbit_epoch, PrimaryBody=Earth): # Poner epoch final como opcional, si no se coge un solo periodo
        """
        Define the geo-orbit by keplerian parameters.

        Args:
            a (Quantity): Semi-major axis.
            ecc (Quantity): Eccentricity.
            inc (Quantity): Inclination.
            raan (Quantity): Longitude of the ascending node.
            argp (Quantity): Argument of periapsis.
            nu (Quantity): True anomaly.
            start_epoch (Time): Start epoch of the orbit.
            end_epoch (Time): End epoch of the orbit.
            body (Body, optional): Main attractor. Defaults to Earth.
        """
        
        self.orb = Orbit.from_classical(PrimaryBody, a, ecc, inc, raan, argp, nu, start_epoch) # Define orbit with Poliastro
        
        self.body = PrimaryBody
        self.a = a
        self.ecc = ecc
        self.inc = inc
        self.raan = raan
        self.argp = argp
        self.nu = nu
        self.T = self.orb.period
        self.start_epoch = start_epoch
        if orbit_epoch=='Final Epoch':
            self.end_epoch = end_epoch
            t = (end_epoch-start_epoch)
            self.N = round(t.sec/self.T.value * 50)
        elif orbit_epoch=='Period':
            self.end_epoch = start_epoch+self.orb.period
            self.N = 100
        
        self.params = tabulate([["a = {}".format(self.a)],
                       ["ecc = {}".format(self.ecc)],
                       ["inc = {}".format(self.inc)],
                       ["RAAN = {}".format(self.raan)],
                       ["argp = {}".format(self.argp)],
                       ["nu = {}".format(self.nu)],
                       ["Start Epoch = {}".format(self.start_epoch)],
                       ["End Epoch = {}".format(self.end_epoch)],
                       ["T = {}".format(self.T)]],
                        headers=['"{}" Orbit Params:'.format(self.name)])
        
        self.ephem = self.orb.to_ephem(strategy=EpochsArray(epochs=time_range(start=self.start_epoch, periods=self.N, end=self.end_epoch), method=method))
        self.ephem_epochs = self.ephem.epochs # All epochs of the time range
        self.ephem_coord = self.ephem.sample(self.ephem.epochs)
        #print('N = ',self.N)
        
    def get_groundtrack(self, View, EarthStation=None):
        """
        Generate the groundtrack of the orbit.
        
        Args:
            View (str): Type of view of the groundtrack desired.
            
        Returns:
            groundtrack: A Plotly figure with the groundtrack.
        """
        
        # Define earth satellite
        spacecraft = EarthSatellite(self.orb,None)
        start_date = self.start_epoch
        end_date = self.end_epoch
        t_span = time_range(start=start_date, periods=self.N, end=end_date)
        
        # Generate an instance of the plotter, add title and show latlon grid
        gp = GroundtrackPlotter()
        gp.update_layout(title="{} satellite groundtrack".format(self.name))

        # Plot previously defined EarthSatellite object
        gp.plot(
            spacecraft,
            t_span,
            label="SC",
            color="red",
            marker={
                "size": 10,
                "symbol": "hourglass",
                "line": {"width": 1, "color": "black"},
            },
        )
        if View == "3D":
            # Switch to three dimensional representation
            gp.update_geos(projection_type="orthographic")
        elif View == "2D":
            # Switch to three dimensional representation
            gp.update_geos(projection_type="equirectangular")
        else:
            print('Error: define type of view')
        
        if EarthStation:
            # Position in [LAT LON]
            STATION = EarthStation.coord * u.deg

            # Let us add a new trace in original figure
            gp.add_trace(
                go.Scattergeo(
                    lat=STATION[0],
                    lon=STATION[-1],
                    name="{}".format(EarthStation.name),
                    marker={"color": "blue"},
                )
            )
        
        gp.update_geos(showcountries=True)
        gp.fig.show()
        
    def get_ephem(self):
        """
        Get the ephemerides of the orbit.

        Returns:
            ephem: Ephemerides of the orbit during the propagated epoch into a .csv file.
        """
        
        coord_x = self.ephem_coord.x.value
        coord_y = self.ephem_coord.y.value
        coord_z = self.ephem_coord.z.value
        coord_xyz = self.ephem_coord.xyz.value
        times = Time(self.ephem_epochs, format='jd')
        
        # Write the ephem to a csv file
        df = pd.DataFrame({'Time (J2000)': times,
                            'Coord_X (km)': coord_x,
                            'Coord_Y (km)': coord_y,
                            'Coord_Z (km)': coord_z})
        file_path = "files/ephem/Ephem_{}.csv".format(self.name)
        df.to_csv(file_path, index=False)
        print(f"Ephemerides written to {file_path}")
        
        
    def orbit_3D(self, Num, size, orientation, face_oriented):
        
        """
        Generate a 3D view of the orbit.

        Args:
            Num (int): Number of sample points.
            size (float): Size of the satellite.
            orientation (str): Orientation type of the satellite ('Nadir' or 'Sun').
            face_oriented (str): Face of the satellite oriented ('+X', '-X', '+Y', '-Y', '+Z', '-Z').
            
            
        Returns:
            orbit_3D: A PyVista figure with the 3D orbit representation.
        """
        
        
        self.ephemT = self.orb.to_ephem(strategy=EpochsArray(epochs=time_range(start=self.start_epoch, periods=Num, end=self.start_epoch+self.T), method=method))
        self.ephemT_coord = self.ephemT.sample(self.ephemT.epochs)
        x_orbit = self.ephemT_coord.x.value
        y_orbit = self.ephemT_coord.y.value
        z_orbit = self.ephemT_coord.z.value
        rr, vv = self.ephemT.rv()
        nu = rv_to_nu(self.orb,rr,vv)
                
        # Create satellite and Earth
        earth = pv.examples.planets.load_earth(radius=6378.1)
        earth_texture = pv.examples.load_globe_texture()
        
        # Create Plotter
        plotter = pv.Plotter()
        
        # Colormap
        colors = np.zeros(6)
        yellow = np.array([255 / 256, 247 / 256, 0 / 256, 1.0])
        red = np.array([1.0, 0.0, 0.0, 1.0])
        mapping = np.linspace(0, 1, 256)
        newcolors = np.empty((256, 4))
        newcolors[mapping < 1] = red
        newcolors[mapping >= 1] = yellow
        my_colormap = ListedColormap(newcolors)

        # Add satellite to Plotter
        for i in range(Num):
            position = (x_orbit[i], y_orbit[i], z_orbit[i])
            sc = pv.Cube(center=(0.0, 0.0, 0.0), x_length=size, y_length=size, z_length=size)
            
            # Rotation Z: RAAN
            sc_1 = sc.rotate_z(angle=self.raan.value)
            x_vec1 = np.dot(R_z(np.radians(self.raan.value)), np.array([1,0,0]) )
            y_vec1 = np.dot(R_z(np.radians(self.raan.value)), np.array([0,1,0]) )
            z_vec1 = np.dot(R_z(np.radians(self.raan.value)), np.array([0,0,1]) )
            
            
            # Rotation X: Inc
            sc_2 = sc_1.rotate_vector(x_vec1, angle=self.inc.value) 
            x_vec2 = np.dot(np.dot(R_z(np.radians(self.raan.value)), R_x(np.radians(self.inc.value))), np.array([1,0,0]))
            y_vec2 = np.dot(np.dot(R_z(np.radians(self.raan.value)), R_x(np.radians(self.inc.value))), np.array([0,1,0]))
            z_vec2 = np.dot(np.dot(R_z(np.radians(self.raan.value)), R_x(np.radians(self.inc.value))), np.array([0,0,1]))
            
            
            # Rotation Z: nu + argp
            ang_3 = (self.argp.value+np.degrees(nu[i])) 
            sc_3 = sc_2.rotate_vector(z_vec2, angle=ang_3) 
            x_vec3 = np.dot(np.dot(np.dot(R_z(np.radians(self.raan.value)), R_x(np.radians(self.inc.value))), R_z(np.radians(ang_3))), np.array([1,0,0]))
            y_vec3 = np.dot(np.dot(np.dot(R_z(np.radians(self.raan.value)), R_x(np.radians(self.inc.value))), R_z(np.radians(ang_3))), np.array([0,1,0]))
            z_vec3 = np.dot(np.dot(np.dot(R_z(np.radians(self.raan.value)), R_x(np.radians(self.inc.value))), R_z(np.radians(ang_3))), np.array([0,0,1]))
            
                
            # Rotation: Oriented face
            if orientation=='Nadir':
                if face_oriented=='+X':
                    sc_4 = sc_3.rotate_vector(z_vec3, angle=180)
                    colors[1]=1
                elif face_oriented=='-X':
                    sc_4 = sc_3.rotate_vector(z_vec3, angle=0)
                    colors[0]=1
                elif face_oriented=='+Y':
                    sc_4 = sc_3.rotate_vector(z_vec3, angle=90)
                    colors[3]=1
                elif face_oriented=='-Y':
                    sc_4 = sc_3.rotate_vector(z_vec3, angle=270)
                    colors[2]=1
                elif face_oriented=='+Z':
                    sc_4 = sc_3.rotate_vector(y_vec3, angle=270)
                    colors[5]=1
                elif face_oriented=='-Z':
                    sc_4 = sc_3.rotate_vector(y_vec3, angle=90)
                    colors[4]=1
                else:
                    exit('Error')
                
                sc_trans = sc_4.translate(position)
                sc_trans["Color"] = colors
                plotter.add_mesh(sc_trans, line_width=3,scalars="Color", cmap=my_colormap, show_edges=True,show_scalar_bar=False)
            
            elif orientation=='Sun':
                # if face_oriented=='+X':
                #     sc_4 = sc_3.rotate_vector(z_vec3, angle=180)
                #     colors[1]=1
                # elif face_oriented=='-X':
                #     sc_4 = sc_3.rotate_vector(z_vec3, angle=0)
                #     colors[0]=1
                # elif face_oriented=='+Y':
                #     sc_4 = sc_3.rotate_vector(z_vec3, angle=90)
                #     colors[3]=1
                # elif face_oriented=='-Y':
                #     sc_4 = sc_3.rotate_vector(z_vec3, angle=270)
                #     colors[2]=1
                # elif face_oriented=='+Z':
                #     sc_4 = sc_3.rotate_vector(y_vec3, angle=270)
                #     colors[5]=1
                # elif face_oriented=='-Z':
                #     sc_4 = sc_3.rotate_vector(y_vec3, angle=90)
                #     colors[4]=1
                # else:
                #     exit('Error')
                
                sc_trans = sc.translate(position)
                #sc_trans["Color"] = colors
                plotter.add_mesh(sc_trans, line_width=3,color='yellow',show_edges=True,show_scalar_bar=False)
                
                

        # Add Earth to plotter
        plotter.add_mesh(earth, texture=earth_texture, smooth_shading=True)

        # Define stars background
        image_path = pv.examples.planets.download_stars_sky_background(load=False)
        plotter.add_background_image(image_path)
        
        # Define camera position
        plotter.camera_position = "iso"
        plotter.set_focus((0,0,0))

        # Add axes
        plotter.add_axes(line_width=3,color='white')
        plotter.add_arrows(np.array([0,0,0]), np.array([1,0,0]), mag=15000,color='red')
        plotter.add_arrows(np.array([0,0,0]), np.array([0,1,0]), mag=15000,color='green')
        plotter.add_arrows(np.array([0,0,0]), np.array([0,0,1]), mag=15000,color='blue')
        #plotter.add_camera_orientation_widget()
        
        # Show Plotter
        plotter.show()

    def umbra(self):
        """
        Get the positions of the satellite in umbra.
        

        Returns:
            ephem_umbra: Ephemerides of the satellite in umbra.
        """
        
        # Primary Body == Earth
        # Secondary Body == Sun
        
        k = Earth.k.to_value(u.km**3 / u.s**2)
        R_sun = Sun.R.to_value(u.km)
        R_earth = Earth.R.to_value(u.km)
        
        # Position and velocity vector of satellite
        rr, vv = self.ephem.rv()
        rr = (rr << u.km).value
        vv = (vv << u.km / u.s).value
        
        # Position vector of Sun wrt Solar System Barycenter
        r_sun = get_body_barycentric_posvel("Sun", self.start_epoch)[0] # Secondary body
        r_earth = get_body_barycentric_posvel("Earth", self.start_epoch)[0] # Primary body
        
        r_sec = ((r_sun - r_earth).xyz << u.km).value # Position vector of the secondary body with respect to the primary body
        
        # print('rr vv =', np.hstack((rr[1], vv[1])))
        # print('r_sec =', r_sec)
        eclipses = []
        umbra = []  # List to store values of eclipse_function.
        umbra_points = [] # List to store values of points in umbra
        for i in range(len(rr)):
            r = rr[i]
            v = vv[i]
            eclipse = eclipse_function(k, np.hstack((r, v)), r_sec, R_sun, R_earth)
            eclipses.append(eclipse)
            alpha = np.degrees( np.arccos(np.dot(r_sec, r)/(np.linalg.norm(r_sec) * np.linalg.norm(r))) ) # Angle between r_sun and r_sat [0,180]
            if ((eclipse>=0) and (alpha>=90)):
                umbra.append(eclipse)
                umbra_points.append(i)
                
        self.ephem_umbra_coord = [rr[j] for j in umbra_points]
        self.ephem_umbra_epochs = [self.ephem_epochs[j] for j in umbra_points]
        
        coord_x = [arr[0] for arr in self.ephem_umbra_coord]
        coord_y = [arr[1] for arr in self.ephem_umbra_coord]
        coord_z = [arr[2] for arr in self.ephem_umbra_coord]
        
        #print(self.ephem_umbra_epochs)
        times = [t.jd for t in self.ephem_umbra_epochs]
        
        
        # Write the ephem to a csv file
        df = pd.DataFrame({'Time (J2000)': times,
                            'Coord_X (km)': coord_x,
                            'Coord_Y (km)': coord_y,
                            'Coord_Z (km)': coord_z})
        file_path = "files/umbra/Umbra_{}.csv".format(self.name)
        df.to_csv(file_path, index=False)
        print(f"Umbra ephemerides written to {file_path}")
        
        plot_umbra_function = False
        if plot_umbra_function == True:
            plt.xlabel("Point")
            plt.ylabel("Umbra function")
            #plt.title("Umbra function")
            plt.plot(eclipses)
            plt.axhline(y=0, color='r', linestyle='--', label='y = 0')
            plt.grid(True)
            plt.show()
        
        
        
        
        
    def plot_umbra(self, size=1000):
        """
        Generate a 3D view of the orbit for the points in umbra.

        Args:
            size (float, optional): Size of the satellite.
            
            
        Returns:
            orbit_3D_umbra: A PyVista figure with the 3D representation for the points in umbra.
        """
        
        # Primary Body == Earth
        # Secondary Body == Sun
        
        # Position vector of Sun wrt Solar System Barycenter
        r_sun = get_body_barycentric_posvel("Sun", self.start_epoch)[0] # Secondary body
        r_earth = get_body_barycentric_posvel("Earth", self.start_epoch)[0] # Primary body
        r_sec = ((r_sun - r_earth).xyz << u.km).value # Position vector of the secondary body with respect to the primary body

        x_orbit = [array[0] for array in self.ephem_umbra_coord]
        y_orbit = [array[1] for array in self.ephem_umbra_coord]
        z_orbit = [array[2] for array in self.ephem_umbra_coord]
        # print('x', x_orbit)

        # Create satellite, Earth and Sun
        sc = pv.Cube(center=(0.0, 0.0, 0.0), x_length=size, y_length=size, z_length=size)
        earth = pv.examples.planets.load_earth(radius=6378.1)
        earth_texture = pv.examples.load_globe_texture()
        sun = pv.examples.planets.load_sun(radius=696340)
        sun_texture = pv.examples.planets.download_sun_surface(texture=True)
        sun_translate = sun.translate((r_sec[0], r_sec[1], r_sec[2]))
        sun_direction = pv.Line((0, 0, 0), (r_sec[0]/1000, r_sec[1]/1000, r_sec[2]/1000))
        sun_tube = pv.Tube((0, 0, 0), (r_sec[0]/1000, r_sec[1]/1000, r_sec[2]/1000), radius=6378.1, n_sides=30)
        
        # Create Plotter
        plotter = pv.Plotter(window_size=[1500,1500])

        # Add satellite to Plotter
        for i in range(len(x_orbit)):
            sc_translate = sc.translate((x_orbit[i], y_orbit[i], z_orbit[i]))
            plotter.add_mesh(sc_translate, color='g')

        # Add Earth and Sun to plotter
        plotter.add_mesh(earth, texture=earth_texture, smooth_shading=True)
        #plotter.add_mesh(sun_translate, texture=sun_texture, smooth_shading=True)
        plotter.add_mesh(sun_direction, line_width=3, color='yellow', label='Sun direction')
        plotter.add_mesh(sun_tube, color='yellow')

        # Define stars background
        image_path = pv.examples.planets.download_stars_sky_background(load=False)
        plotter.add_background_image(image_path)
        
        # Define camera position
        plotter.camera_position = "iso"
        plotter.set_focus((0,0,0))

        # Add axes
        plotter.add_axes(line_width=3,color='white')
        plotter.add_arrows(np.array([0,0,0]), np.array([1,0,0]), mag=15000,color='red')
        plotter.add_arrows(np.array([0,0,0]), np.array([0,1,0]), mag=15000,color='green')
        plotter.add_arrows(np.array([0,0,0]), np.array([0,0,1]), mag=15000,color='blue')
        
        # Add legend
        plotter.add_legend(bcolor=None,size=(0.1, 0.1),face=None)
        
        # Show Plotter
        plotter.show()
