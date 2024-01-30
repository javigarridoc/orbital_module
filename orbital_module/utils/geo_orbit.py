from astropy import units as u

from poliastro.bodies import Earth
from poliastro.twobody import Orbit
from poliastro.twobody.sampling import EpochsArray
from poliastro.util import time_range
from poliastro.earth import EarthSatellite
from poliastro.earth.plotting import GroundtrackPlotter

import plotly.graph_objects as go


from poliastro.czml.extract_czml import CZMLExtractor

import pandas as pd

from tabulate import tabulate

import webbrowser


class GeoOrbit:
    """Define orbit, get a 3D Orbit view with Cesium, get groundtrack and get ephems"""
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
        
    def get_ephem(self, start_date, end_date):
        self.ephem = self.orb.to_ephem(strategy=EpochsArray(epochs=time_range(start=start_date, end=end_date)))
        self.ephem_epochs = self.ephem.epochs # All epochs of the time range
        self.ephem_coord = self.ephem.sample(self.ephem.epochs)
        
        coord_x = self.ephem_coord.x.value
        coord_y = self.ephem_coord.y.value
        coord_z = self.ephem_coord.z.value
        coord_xyz = self.ephem_coord.xyz.value
        
        # Write the ephem to an excel file
        data_frame = pd.DataFrame(coord_xyz)
        data_frame_transpose = data_frame.transpose()
        file_path = "files/ephem/Ephem_{}.xlsx".format(self.name)
        data_frame_transpose.to_excel(file_path, index=False, header=["X","Y","Z"])
        print(f"Ephemerides written to {file_path}")