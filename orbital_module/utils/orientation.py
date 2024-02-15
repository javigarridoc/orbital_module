import numpy as np
from astropy import units as u

from astropy.coordinates import get_body_barycentric, solar_system_ephemeris

# class SatelliteOrientation:
#     '''Define the satellite orientation'''  
    
#     def __init__(self, name):
#         self.name = name

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
        
        

def rv_to_nu(orbit,rr,vv):
    mu = 3.986e5 # km^3/s^2
    
    rr = (rr << u.km).value
    vv = (vv << u.km / u.s).value
    nu = []
    
    # If circular orbit
    if orbit.ecc == 0:
        for i in range(len(rr)):
            r_vec = rr[i]
            v_vec = vv[i]
            r = np.linalg.norm(r_vec)
            v = np.linalg.norm(v_vec)
            v_r = np.dot(r_vec / r, v_vec)
            v_p = np.sqrt(v ** 2 - v_r ** 2)


            h_vec = np.cross(r_vec, v_vec)
            h = np.linalg.norm(h_vec)
            n_vec = np.array([np.cos(np.radians(orbit.raan)), np.sin(np.radians(orbit.raan)), 0])
            n = np.linalg.norm(n_vec)
            
            if orbit.inc==0:                
                if v_vec[0]<=0:
                    nu_value = np.arccos(r_vec[0]/r)
                    nu.append(nu_value)
                elif v_vec[0]>0:
                    nu_value = 2*np.pi - np.arccos(r_vec[0]/r)
                    nu.append(nu_value)
            else:
                if r_vec[2]>=0:
                    nu_value = np.arccos(np.dot(r_vec / r, n_vec / n))
                    nu.append(nu_value)
                elif r_vec[2]<0:
                    nu_value = 2*np.pi - np.arccos(np.dot(r_vec / r, n_vec / n))
                    nu.append(nu_value)
                    
    # If elliptic orbit      
    else:
        for i in range(len(rr)):
            r_vec = rr[i]
            v_vec = vv[i]
            r = np.linalg.norm(r_vec)
            v = np.linalg.norm(v_vec)
            v_r = np.dot(r_vec / r, v_vec)
            v_p = np.sqrt(v ** 2 - v_r ** 2)


            h_vec = np.cross(r_vec, v_vec)
            h = np.linalg.norm(h_vec)
            e_vec = np.cross(v_vec, h_vec) / mu - r_vec / r
            e = np.linalg.norm(e_vec)
            
            if v_r>=0:
                nu_value = np.arccos(np.dot(r_vec / r, e_vec / e))
                nu.append(nu_value)
            elif v_r<0:
                nu_value = 2*np.pi - np.arccos(np.dot(r_vec / r, e_vec / e))
                nu.append(nu_value)
            
    return nu


def R_x(ang):
    '''Rotation Matrix around X-axis'''
    R_x = np.array([[1, 0, 0],  [0, np.cos(ang), -np.sin(ang)], [0, np.sin(ang), np.cos(ang)]])  
    
    return R_x

def R_y(ang):
    '''Rotation Matrix around Y-axis'''
    R_y = np.array([[np.cos(ang), 0, np.sin(ang)],  [0, 1, 0], [-np.sin(ang), 0, np.cos(ang)]])  
    
    return R_y

def R_z(ang):
    '''Rotation Matrix around Z-axis'''
    R_z = np.array([[np.cos(ang), -np.sin(ang), 0], [np.sin(ang), np.cos(ang), 0], [0, 0, 1]])
    
    return R_z

def R_euler_zxz(ang_1,ang_2,ang_3):
    '''Euler rotation matrix Z1-X2-Z3'''
    c1 = np.cos(ang_1)
    c2 = np.cos(ang_2)
    c3 = np.cos(ang_3)
    s1 = np.sin(ang_1)
    s2 = np.sin(ang_2)
    s3 = np.sin(ang_3)
    
    R = np.array([
    [c1*c3 - c2*s1*s3,  -c1*s3 - c2*c3*s1,  s1*s2],
    [c3*s1 + c1*c2*s3,  c1*c2*c3 - s1*s3,  -c1*s2],
    [s2*s3, c3*s2, c2] 
    ])
    
    return R

# coords = np.array([[100,0,0],[]])
# satellite_orientation(orientation='Nadir', face_oriented='+X',raan=0,inc=30,argp=0,nu=90)
