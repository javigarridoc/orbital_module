import numpy as np
from astropy import units as u

# class SatelliteOrientation:
#     '''Define the satellite orientation'''  
    
#     def __init__(self, name):
#         self.name = name

def satellite_orientation(orbit,orientation,face_oriented):
    if orientation=='Nadir':
        print('The satellite orientation is:', orientation)
        ang_1 = np.radians(orbit.raan.value)
        ang_2 = np.radians(orbit.inc.value)
        
        R_1 = np.array([[np.cos(ang_1), -np.sin(ang_1), 0], [np.sin(ang_1), np.cos(ang_1), 0], [0, 0, 1]])
        R_2 = np.array([[1, 0, 0],  [0, np.cos(ang_2), -np.sin(ang_2)], [0, np.sin(ang_2), np.cos(ang_2)]])
        
        coords = orbit.ephem_coord
        rr, vv = orbit.ephem.rv()
        nu = rv_to_nu(orbit)
        
        #print('coords = ', rr)
        print('nu = ',np.degrees(nu))
        
        if face_oriented=='+X':
            for i in range(len(nu)):
                ang_3 = np.radians(orbit.argp.value+orbit.nu.value) + nu[i]
                #print('ang_3 = ', np.degrees(ang_3))
                R_3 = np.array([[np.cos(ang_3), -np.sin(ang_3), 0], [np.sin(ang_3), np.cos(ang_3), 0], [0, 0, 1]])
                
                
                
    elif orientation=='Sun':
        print('The satellite orientation is:', orientation)
        
        
        
        
def rv_to_nu(orbit):
    mu = 3.986e5 # km^3/s^2
    rr, vv = orbit.ephem.rv()
    rr = (rr << u.km).value
    vv = (vv << u.km / u.s).value
    nu = []
    
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
            #print('r_vec', r_vec)
            #print('dot = ',np.dot(r_vec / r, e_vec / e))
            #print('e_vec = ', e_vec)
            #print('e_vec2 = ', e_vec2)
            nu_value = np.arccos(np.dot(r_vec / r, n_vec / n))
            
            # MAL REVISAR IF
            if i==0:
                nu.append(nu_value)
            else:
                if (nu[i-1]<=np.pi) and (nu[i-1]>=0):
                    nu.append(nu_value)
                elif (nu[i-1]>np.pi) and (nu[i-1]<=2*np.pi):
                    nu_value2 = 2*np.pi - nu_value
                    nu.append(nu_value2)
                else:
                    print('Error')
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
            #print('r_vec', r_vec)
            #print('dot = ',np.dot(r_vec / r, e_vec / e))
            #print('e_vec = ', e_vec)
            #print('e_vec2 = ', e_vec2)
            
            if v_r>=0:
                nu_value = np.arccos(np.dot(r_vec / r, e_vec / e))
                nu.append(nu_value)
            elif v_r<0:
                nu_value = 2*np.pi - np.arccos(np.dot(r_vec / r, e_vec / e))
                nu.append(nu_value)
            #print('nu_value', nu_value)
    return nu

        
# coords = np.array([[100,0,0],[]])
# satellite_orientation(orientation='Nadir', face_oriented='+X',raan=0,inc=30,argp=0,nu=90)
