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
        
        nu = rv_to_nu(orbit)
        print(np.degrees(nu))
        
        xyz_list = [] 
        R_list = []
        
        for i in range(len(nu)):
            ang_3 = np.radians(orbit.argp.value+orbit.nu.value) + nu[i]
            
            R = R_euler_zxz(ang_1,ang_2,ang_3)
            R_list.append(R)
            
            xyz_0 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
            xyz_new = np.dot(R, xyz_0)
            xyz_list.append(xyz_new)
        
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
            
        x_dir = [R_i @ np.array([1,0,0]) for R_i in R_tot_list] 
        y_dir = [R_i @ np.array([0,1,0]) for R_i in R_tot_list] 
        z_dir = [R_i @ np.array([0,0,1]) for R_i in R_tot_list] 
        
        print(x_dir)
        
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
