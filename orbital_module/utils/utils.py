import numpy as np
from astropy import units as u

def rv_to_nu(orbit,rr,vv):
    """
    Get the true anomaly in the orbit from position and velocity vectors.

    Args:
        orbit (GeoOrbit): The orbit object containing satellite orbit parameters.
        rr (numpy.ndarray): Position vector array of the satellite.
        vv (numpy.ndarray): Velocity vector array of the satellite.

    Returns:
        nu (list): List of true anomaly values.
    """
    
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
    """
    Generate the rotation matrix around the X-axis.

    Args:
        ang (float): Angle in radians.

    Returns:
        R_x (numpy.ndarray): Rotation matrix.
    """
    R_x = np.array([[1, 0, 0],  [0, np.cos(ang), -np.sin(ang)], [0, np.sin(ang), np.cos(ang)]])  
    
    return R_x

def R_y(ang):
    """
    Generate the rotation matrix around the XY-axis.

    Args:
        ang (float): Angle in radians.

    Returns:
        R_y (numpy.ndarray): Rotation matrix.
    """    
    
    R_y = np.array([[np.cos(ang), 0, np.sin(ang)],  [0, 1, 0], [-np.sin(ang), 0, np.cos(ang)]])  
    
    return R_y

def R_z(ang):
    """
    Generate the rotation matrix around the Z-axis.

    Args:
        ang (float): Angle in radians.

    Returns:
        R_z (numpy.ndarray): Rotation matrix.
        
    """    
    R_z = np.array([[np.cos(ang), -np.sin(ang), 0], [np.sin(ang), np.cos(ang), 0], [0, 0, 1]])
    
    return R_z

def R_euler_zxz(ang_1,ang_2,ang_3):
    
    """
    Generate the Euler rotation matrix for Z1-X2-Z3 rotations.

    Args:
        ang_1 (float): First rotation angle around the Z-axis in radians.
        ang_2 (float): Second rotation angle around the X-axis in radians.
        ang_3 (float): Third rotation angle around the Z-axis in radians.

    Returns:
        R (numpy.ndarray): Euler rotation matrix.
    """
    
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
