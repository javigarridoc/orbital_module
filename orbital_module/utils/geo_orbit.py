from astropy import units as u
from astropy.time import Time

from poliastro.bodies import Earth, Sun
from poliastro.twobody import Orbit
from poliastro.twobody.sampling import EpochsArray
from poliastro.util import time_range
from poliastro.earth import EarthSatellite
from poliastro.earth.plotting import GroundtrackPlotter
from poliastro.czml.extract_czml import CZMLExtractor
from astropy.coordinates import (
    CartesianRepresentation,
    get_body_barycentric_posvel,
)
from poliastro.core.events import eclipse_function
from poliastro.twobody.events import (
    AltitudeCrossEvent,
    LatitudeCrossEvent,
    NodeCrossEvent,
    PenumbraEvent,
    UmbraEvent,
)

import plotly.graph_objects as go

import pyvista as pv
import numpy as np

import pandas as pd

from tabulate import tabulate

import webbrowser


class GeoOrbit:
    """Define orbit, get a 3D Orbit view, get groundtrack and get ephems"""
    global N
    N = 100 # Sample points
    
    def __init__(self, name):
        self.name = name
    
    def define_orbit(self, a, ecc, inc, raan, argp, nu, start_epoch, end_epoch, PrimaryBody=Earth): # Poner epoch final como opcional, si no se coge un solo periodo
        
        
        self.orb = Orbit.from_classical(PrimaryBody, a, ecc, inc, raan, argp, nu, start_epoch) # Define orbit with Poliastro
        
        self.body = PrimaryBody
        self.a = a
        self.ecc = ecc
        self.inc = inc
        self.raan = raan
        self.argp = argp
        self.nu = nu
        self.start_epoch = start_epoch
        self.end_epoch = end_epoch
        self.T = self.orb.period
        self.params = tabulate([["a = {}".format(a)],
                       ["ecc = {}".format(ecc)],
                       ["inc = {}".format(inc)],
                       ["RAAN = {}".format(raan)],
                       ["argp = {}".format(argp)],
                       ["nu = {}".format(nu)],
                       ["Start Epoch = {}".format(start_epoch)],
                       ["End Epoch = {}".format(end_epoch)],
                       ["T = {}".format(self.T)]],
                        headers=['{} Orbit Params:'.format(self.name)])
        
        self.ephem = self.orb.to_ephem(strategy=EpochsArray(epochs=time_range(start=start_epoch, periods=N, end=end_epoch)))
        self.ephem_epochs = self.ephem.epochs # All epochs of the time range
        self.ephem_coord = self.ephem.sample(self.ephem.epochs)
        
    def orbit_viewer(self, port=8080): # Create CZML file and print the orbit using CESIUM
        
        start_epoch = self.start_epoch
        end_epoch = self.end_epoch
        extractor = CZMLExtractor(start_epoch, end_epoch, N,scene3D=True)
        extractor.add_orbit(
            self.orb,
            id_name=self.name,
            path_width=2,
            #label_text=self.name,
            label_fill_color=[125, 80, 120, 255]
            )
        # Obtener el documento CZML
        czml_document = extractor.get_document()

        # Convert CZML to JSON format
        czml_json = czml_document.dumps()

        # Open file and write the CZML
        with open("files/czml/{}.czml".format(self.name), "w") as archivo:
            archivo.write(czml_json)
            archivo.close()
            
        html_text1 = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, maximum-scale=1, minimum-scale=1, user-scalable=no"
    />
    <meta name="description" content="CZML Polyline">
    <meta name="cesium-sandcastle-labels" content="CZML">
    <title>Cesium Demo</title>
    <script type="text/javascript" src="../Sandcastle-header.js"></script>
    <script src="../../../Build/CesiumUnminified/Cesium.js"></script>
    <script>window.CESIUM_BASE_URL = "../../../Build/CesiumUnminified/";</script>
  </head>
  <body
    class="sandcastle-loading"
    data-sandcastle-bucket="bucket-requirejs.html"
  >
<style>
      @import url(../templates/bucket.css);
    </style>
    <div id="cesiumContainer" class="fullSize"></div>
    <div id="loadingOverlay"><h1>Loading...</h1></div>
    <div id="toolbar"></div>

    <script id="cesium_sandcastle_script">
window.startup = async function (Cesium) {
    'use strict';
const czml = '''

        html_text2 = '''\n
const viewer = new Cesium.Viewer("cesiumContainer");
const dataSourcePromise = Cesium.CzmlDataSource.load(czml);
viewer.dataSources.add(dataSourcePromise);
viewer.zoomTo(dataSourcePromise);
    Sandcastle.finishedLoading();
};
if (typeof Cesium !== 'undefined') {
    window.startupCalled = true;
    window.startup(Cesium).catch((error) => {
      "use strict";
      console.error(error);
    });
}
</script>
</body>
</html>'''

        html_code = html_text1 + czml_json + html_text2
            
        # Open file and write the html
        with open("Cesium-1.111/Apps/Sandcastle/gallery/Orbit_viewer_{}.html".format(self.name), "w") as html_file:
            html_file.write(html_code)
            html_file.close()
            
        # Automatically open the default web browser with the HTML page.
        webbrowser.open(f"http://localhost:{port}/Cesium-1.111/Apps/Sandcastle/gallery/Orbit_viewer_{self.name}.html")
            
    def get_groundtrack(self, View, EarthStation=None):
        # Define earth satellite
        spacecraft = EarthSatellite(self.orb,None)
        start_date = self.start_epoch
        end_date = self.end_epoch
        t_span = time_range(start=start_date, periods=N, end=end_date)
        
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
        
        
    def orbit_3D(self, Num, size):
        
        self.ephemT = self.orb.to_ephem(strategy=EpochsArray(epochs=time_range(start=self.start_epoch, periods=Num, end=self.start_epoch+self.T)))
        self.ephemT_coord = self.ephemT.sample(self.ephemT.epochs)
        x_orbit = self.ephemT_coord.x.value
        y_orbit = self.ephemT_coord.y.value
        z_orbit = self.ephemT_coord.z.value

        # Create satellite and Earth
        sc = pv.Cube(center=(0.0, 0.0, 0.0), x_length=size, y_length=size, z_length=size)
        earth = pv.examples.planets.load_earth(radius=6378.1)
        earth_texture = pv.examples.load_globe_texture()

        # Create Plotter
        plotter = pv.Plotter(window_size=[1000,1000])

        # Add satellite to Plotter
        for i in range(Num):
            sc_translate = sc.translate((x_orbit[i], y_orbit[i], z_orbit[i]))
            plotter.add_mesh(sc_translate, color='r')

        # Add Earth to plotter
        plotter.add_mesh(earth, texture=earth_texture, smooth_shading=True)

        # Define camera position
        plotter.camera_position = "iso"

        # Show Plotter
        plotter.show()

    def Eclipse(self):
        attractor = Earth
        k = Earth.k.to_value(u.km**3 / u.s**2)
        R_sec = Sun.R.to_value(u.km)
        R_pri = Earth.R.to_value(u.km)
        # Position vector of Sun wrt Solar System Barycenter
        r_sec_ssb = get_body_barycentric_posvel("Sun", self.ephem_epochs)[0]
        r_pri_ssb = get_body_barycentric_posvel("Earth", self.ephem_epochs)[0]