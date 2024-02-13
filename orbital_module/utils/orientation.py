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
        
        R_1 = R_z(ang_1) 
        R_2 = R_x(ang_2) 
        
        nu = rv_to_nu(orbit)
        print(np.degrees(nu))
        
        xyz_list = [] 
        R_tot_list = []
        
        for i in range(len(nu)):
            ang_3 = np.radians(orbit.argp.value+orbit.nu.value) + nu[i]
            R_3 = R_z(ang_3) 
            R_tot = np.dot(np.dot(R_1, R_2), R_3)
            R_tot_list.append(R_tot)
            xyz_0 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
            xyz_new = np.dot(R_tot, xyz_0)
            xyz_list.append(xyz_new)
        
        if face_oriented=='+X':
            ang_4 = np.radians(180)
            R_4 = R_z(ang_4)
            R_tot_final = [R_4 @ R_i for R_i in R_tot_list]
            
        elif face_oriented=='-X':
            ang_4 = np.radians(0)
            R_4 = R_z(ang_4)
            R_tot_final = [R_4 @ R_i for R_i in R_tot_list]

        
        elif face_oriented=='+Y':
            ang_4 = np.radians(90)
            R_4 = R_z(ang_4)
            R_tot_final = [R_4 @ R_i for R_i in R_tot_list]
            
        elif face_oriented=='-Y':
            ang_4 = np.radians(270)
            R_4 = R_z(ang_4)
            R_tot_final = [R_4 @ R_i for R_i in R_tot_list]
        
        elif face_oriented=='+Z':
            ang_4 = np.radians(270)
            R_4 = R_y(ang_4)
            R_tot_final = [R_4 @ R_i for R_i in R_tot_list]
        
        elif face_oriented=='-Z':
            ang_4 = np.radians(90)
            R_4 = R_y(ang_4)
            R_tot_final = [R_4 @ R_i for R_i in R_tot_list]
        else:
            exit('Error')
        
        
    elif orientation=='Sun':
        print('The satellite orientation is:', orientation)
        
    #print(xyz_list)
        
        
        
        
def rv_to_nu(orbit):
    mu = 3.986e5 # km^3/s^2
    rr, vv = orbit.ephem.rv()
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

# coords = np.array([[100,0,0],[]])
# satellite_orientation(orientation='Nadir', face_oriented='+X',raan=0,inc=30,argp=0,nu=90)
