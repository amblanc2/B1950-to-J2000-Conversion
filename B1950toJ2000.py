import math
import numpy as np

#This script is based on the work done by Keith Burnett on http://www.stargazing.net/kepler/b1950.html, it is a simple recreation of the QBASIC script, albeit a little more janky
print('Coordinate form for input is HHMMM(n/s)DDMM, for example Orion's Nebula coordinates from Burham's would be 05329s0525, corresponding to 5hrs 32.9min/5deg 25min South')
Coord=input("Enter coordinate in 'Burnham' format: ")

#Convert to decimal degrees
RA=Coord[0:5]
Dec=Coord[6:]
#Convert RA to deg
RA_hr=RA[0:2]
RA_min=RA[2:]
RA_min=RA_min[:2] + '.' + RA_min[2:]
RA_min=float(RA_min)
RA_hr=float(RA_hr)
RA=(RA_hr+RA_min/60)*15
#Convert Dec to deg
Dec=float(Dec[0:2])+float(Dec[2:])/60
if 's' in Coord:
  Dec=Dec*-1
RA_rad=math.radians(RA)
Dec_rad=math.radians(Dec)

#Convert to recntangular coordinates
x=math.cos(RA_rad)*math.cos(Dec_rad)
y=math.sin(RA_rad)*math.cos(Dec_rad)
z=math.sin(Dec_rad)
coord_mat=np.array([[x],[y],[z]])
prec_mat=np.array([[0.999926,-0.011179,-0.004859],
                   [0.011179,0.999938,-0.000027],
                   [0.004859,0.000027,0.999988]])
J2000_comp=np.matmul(prec_mat,coord_mat)
X,Y,Z=J2000_comp[0],J2000_comp[1],J2000_comp[2]
X,Y,Z=X[0],Y[0],Z[0]
X,Y,Z=float(X),float(Y),float(Z)

#Convert back to RA and Dec
print(X,Y,Z)
r=math.degrees(math.atan(Y/X))
if X<0:
  ra2000= r+180
elif Y<0 and X>0:
  ra2000 = r+360
else:
  ra2000=r+180
dec2000=math.degrees(math.asin(Z))

#Concert RA and DEC to HHMMSS
ra2000=ra2000/15
ra2000=math.modf(ra2000)
ra_hr=ra2000[1]
ra_min=ra2000[0]*60
ra_min=math.modf(ra_min)
ra_sec=round(ra_min[0]*60,1)
ra_min=ra_min[1]

dec2000=dec2000
dec2000=math.modf(dec2000)
dec_hr=dec2000[1]
dec_min=dec2000[0]*60
dec_min=math.modf(dec_min)
dec_sec=round(dec_min[0]*60,0)
dec_min=dec_min[1]

print('RA is '+str(int(ra_hr))+';'+str(int(ra_min))+';'+str(ra_sec))
print('Dec is '+str(int(dec_hr))+';'+str(int(dec_min))+';'+str(dec_sec))
