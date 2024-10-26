from enum import IntEnum
import math

#Names of data values
class Values(IntEnum):
    SEMI_MAJOR_AXIS_INITIAL = 0
    ECCENTRICITY_INITIAL = 1
    INCLINATION_INITIAL = 2
    MEAN_LONGITUDE_INITIAL = 3
    PERIHELION_LONGITUDE_INITIAL = 4
    ASCENDING_NODE_LONGITUDE_INITIAL = 5
    SEMI_MAJOR_AXIS_PER_CENTURY = 6
    ECCENTRICITY_PER_CENTURY = 7
    INCLINATION_PER_CENTURY = 8
    MEAN_LONGITUDE_PER_CENTURY = 9 
    PERIHELION_LONGITUDE_PER_CENTURY = 10
    ASCENDING_NODE_LONGITUDE_PER_CENTURY = 11


#Data values for calculations
mercuryValues = [0.38709927, 0.20563593, 7.00497902, 252.25032350, 77.45779628, 48.33076593, 0.00000037, 0.00001906, -0.00594749, 149472.67411175, 0.16047689, -0.12534081]
venusValues = [0.72333566, 0.00677672, 3.39467605, 181.97909950, 131.60246718, 76.67984255, 0.00000390, -0.00004107, -0.00078890, 58517.81538729, 0.00268329, -0.27769418]
earthMoonBarycenterValues = [1.00000261, 0.01671123, -0.00001531, 100.46457166, 102.93768193, 0.0, 0.00000562, -0.00004392, -0.01294668, 35999.37244981, 0.32327364, 0.0]
marsValues = [1.52371034, 0.09339410, 1.84969142, -4.55343205, -23.94362959, 49.55953891, 0.00001847, 0.00007882, -0.00813131, 19140.30268499, 0.44441088, -0.29257343]


#Converting current time to useable values
Teph = 100000
T = (Teph - 2441445.0) / 36525

#Calcuating correct values for the current time
semiMajorAxis = mercuryValues[Values['SEMI_MAJOR_AXIS_INITIAL'].value] + mercuryValues[Values['SEMI_MAJOR_AXIS_PER_CENTURY'].value] * T
eccentricity = mercuryValues[Values['ECCENTRICITY_INITIAL'].value] + mercuryValues[Values['ECCENTRICITY_PER_CENTURY'].value] * T
inclination = mercuryValues[Values['INCLINATION_INITIAL'].value] + mercuryValues[Values['INCLINATION_PER_CENTURY'].value] * T
meanLongitude = mercuryValues[Values['MEAN_LONGITUDE_INITIAL'].value] + mercuryValues[Values['MEAN_LONGITUDE_PER_CENTURY'].value] * T
perihelionLongitude = mercuryValues[Values['PERIHELION_LONGITUDE_INITIAL'].value] + mercuryValues[Values['PERIHELION_LONGITUDE_PER_CENTURY'].value] * T
ascendingNodeLongitude = mercuryValues[Values['ASCENDING_NODE_LONGITUDE_INITIAL'].value] + mercuryValues[Values['ASCENDING_NODE_LONGITUDE_PER_CENTURY'].value] * T


#Calculating the perihelion argument and the mean anomaly
perihelionArgument = perihelionLongitude - ascendingNodeLongitude
meanAnomaly = -((meanLongitude - perihelionLongitude) % 360 - 180)

meanAnomaly = (meanAnomaly + 360) % 360;  
if (meanAnomaly > 180):  
    meanAnomaly -= 360  

#Calculating the eccentricity anomaly
pi = 3.1415926535
eccentricityPrime = ((180) / pi) * eccentricity
eccentrcityAnomaly = meanAnomaly + eccentricityPrime * math.sin(meanAnomaly)
eccentricityAnomalyChange = 1
while abs(eccentricityChange) <= 0.000001
    meanAnomalyChange = meanAnomaly - (eccentricityAnomaly - eccentricityPrime * math.sin(eccentricityAnomaly))
    eccentricityAnomalyChange = meanAnomalyChange / (1 - eccentricity * math.cos(eccentricityAnomaly))
    eccentricityAnomaly = eccentricityAnomaly + eccentricityAnomalyChange
    
#Compute the planet's heliocentric coordinates in its orbital plane, , with the -axis aligned from the focus to the perihelion
xPrimeCoordinate = semiMajorAxis * (math.cos(eccentricityAnomaly) - eccentricity)
yPrimeCoordinate = semiMajorAxis * math.sqrt(1 - math.pow(eccentricity, 2)) * math.sin(eccentricityAnomaly)
zPrimeCoordinate = 0
