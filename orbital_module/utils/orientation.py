import numpy as np
from astropy import units as u

from astropy.coordinates import get_body_barycentric, solar_system_ephemeris

from .utils import rv_to_nu, R_x, R_y, R_z, R_euler_zxz


def satellite_orientation(orbit,orientation,face_oriented):
    print('The satellite orientation is:', orientation)

    ang_1 = np.radians(orbit.raan.value)
    ang_2 = np.radians(orbit.inc.value)
    # Position and velocity vector of satellite
    rr, vv = orbit.ephem.rv()
    rr = (rr << u.km).value
    vv = (vv << u.km / u.s).value
    nu = rv_to_nu(orbit,rr,vv)
    #print(np.degrees(nu))
    
    R_list = [] # Rotation matrix for every sample point
        
    for i in range(len(nu)):
        ang_3 = np.radians(orbit.argp.value+orbit.nu.value) + nu[i]
        R = R_euler_zxz(ang_1,ang_2,ang_3)
        R_list.append(R)
            
            
    if orientation=='Nadir':
        
        
        
        if face_oriented=='+X':
            ang_4 = np.radians(180)
            R_4 = R_z(ang_4)
            R_tot_list = [R_4 @ R_i for R_i in R_list]
            
        elif face_oriented=='-X':
            ang_4 = np.radians(0)
            R_4 = R_z(ang_4)
            R_tot_list = [R_4 @ R_i for R_i in R_list]

        elif face_oriented=='+Y':
            ang_4 = np.radians(90)
            R_4 = R_z(ang_4)
            R_tot_list = [R_4 @ R_i for R_i in R_list]
            
        elif face_oriented=='-Y':
            ang_4 = np.radians(270)
            R_4 = R_z(ang_4)
            R_tot_list = [R_4 @ R_i for R_i in R_list]
        
        elif face_oriented=='+Z':
            ang_4 = np.radians(270)
            R_4 = R_y(ang_4)
            R_tot_list = [R_4 @ R_i for R_i in R_list]
        
        elif face_oriented=='-Z':
            ang_4 = np.radians(90)
            R_4 = R_y(ang_4)
            R_tot_list = [R_4 @ R_i for R_i in R_list]
        else:
            exit('Error')
            
        x_sat = [R_i @ np.array([1,0,0]) for R_i in R_tot_list] 
        y_sat = [R_i @ np.array([0,1,0]) for R_i in R_tot_list] 
        z_sat = [R_i @ np.array([0,0,1]) for R_i in R_tot_list] 
        
        
    elif orientation=='Sun':
        # Earth-centered cartesian coordinate system
        solar_system_ephemeris.set('jpl') # JPL ephemeris
        print(solar_system_ephemeris.bodies)
        x_sat = []
        y_sat = []
        z_sat = []
        vec_n = [R_i @ np.array([0,0,1]) for R_i in R_list] # Normal to orbit plane
        
        
        for i in range(len(nu)):
            r_sat_earth = rr[i] # Position vector of the Satellite with respect to Earth
            v_sat = vv[i]
            r_sun = get_body_barycentric(body='sun', time=orbit.ephem_epochs[i], ephemeris='jpl')
            r_earth = get_body_barycentric(body='earth', time=orbit.ephem_epochs[i], ephemeris='jpl')
            r_sun_earth = ((r_sun - r_earth).xyz << u.km).value # Position vector of the Sun with respect to Earth
            r_sun_sat = (r_sun_earth - r_sat_earth) # Position vector of the Sun with respect to Satellite
            r_normalized = r_sun_sat / np.linalg.norm(r_sun_sat)
            v_normalized = v_sat / np.linalg.norm(v_sat)
            
            
            if face_oriented=='+X':
                x_sat.append(r_normalized)
                z_sat.append(vec_n[i])
                y_sat.append(np.cross(z_sat[i], x_sat[i]))
                
            elif face_oriented=='-X':
                x_sat.append(-1*r_normalized)  
                z_sat.append(vec_n[i])      
                y_sat.append(np.cross(z_sat[i], x_sat[i]))

            elif face_oriented=='+Y':
                y_sat.append(r_normalized)
                z_sat.append(vec_n[i])
                x_sat.append(np.cross(y_sat[i], z_sat[i]))
                
            elif face_oriented=='-Y':
                y_sat.append(-1*r_normalized)
                z_sat.append(vec_n[i])
                x_sat.append(np.cross(y_sat[i], z_sat[i]))
                                
            elif face_oriented=='+Z': 
                y_sat.append(vec_n[i])
                z_sat.append(r_normalized)
                x_sat.append(np.cross(y_sat[i], z_sat[i]))
            
            elif face_oriented=='-Z':
                y_sat.append(vec_n[i])
                z_sat.append(-1*r_normalized)
                x_sat.append(np.cross(y_sat[i], z_sat[i]))
                
            else:
                exit('Error')        

    
    return x_sat, y_sat, z_sat   
        
        