from astroquery.jplhorizons import Horizons
from astropy.time import Time
import numpy as np



def astro(da,mth,yr):
    st = Time(str(yr)+'-'+str(mth)+'-'+str(da)).jd

    plp = []
    plv = []
    for i, nasaid in enumerate(['sun',
                                199, 299, 399, 499, 599, 699, 799, 899,
                                999, '2003 EL61', 'makemake', 'sedna', '2003 UB313',
                                'ceres','pallas', 433, 'vesta', 'apophis', 'toutatis', 'itokawa', 'gaspra', 243, 'DES=2000007', 'hygiea',
                                90000030, 'hale-bopp']):
        obj = Horizons(id=nasaid, location="@sun", epochs=st).vectors()
        plp.append([np.double(obj[xi]) for xi in ['x', 'y', 'z']])
        plv.append([np.double(obj[vxi]) for vxi in ['vx', 'vy', 'vz']])

        n,m = np.shape(plp)
        pos = np.ones((n, 3))
        vel = np.ones((n, 3))
        for i in range(n):
            for j in range(m):
                pos[i,j] = plp[i][j]
                vel[i,j] = plv[i][j]

    return pos, vel


pos, vel = astro(20,7,2000)
