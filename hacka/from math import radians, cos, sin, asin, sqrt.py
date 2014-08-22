from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    return km

allcoord[] = [[37.874379, -122.263606, "Tolman Hall: Hearst Avenue @ Arch Street"],
[37.87482, -122.26403, "North Gate Hall: Hearst Avenue @ Euclid Avenue"],
[37.875209, -122.257919, "Cory Hall: Hearst Avenue @ LeRoy Avenue"],
[37.873346, -122.257512, "Evans Hall: Hearst Mining Circle side"], 
[37.872533, -122.2541, "Gayley @ Stadium Rimway"], 
[37.871364, -122.252887, "Haas School of Business: Piedmont Avenue Side"],
[37.869738, -122.252491, "International House: Piedmont Avenue @ Bancroft Way"], 
[37.867985, -122.252212, "Piedmont Avenue @ Channing Way"], 
[37.867079, -122.25395, "College Avenue @ Haste Street"], 
[37.869408, -122.25484, "Kroeber Hall: Bancroft Way @ College Avenue"], 
[37.869103, -122.257222, "Hearst Memorial Gym: Bancroft Way @ Bowditch Street"], 
[37.868612, -122.261245, "Sproul Hall: Bancroft Way @ Barrow Lane"], 
[37.868209, -122.263606, "RSF: Bancroft Way @ Ellsworth Street"], 
[37.867765, -122.267039, "Banway Building: Bancroft Way @ Shattuck Avenue"], 
[37.868273, -122.267661, "Shattuck Avenue @ Kittredge Street"], 
[37.870178, -122.267876, "Downtown Berkeley Bart Station"], 
[37.872618, -122.265794, "Oxford Street @ University Avenue"]]

#returns string
def findcloseststop(curlon, curlat):
    maxdistance = float('inf')
    busstop = ''
    for i in range (0, 17):
        distance = haversine(curlon, curlat, allcoord[i][0], allcoord[i][1])
        if distance < maxdistance:
            maxdistance = distance
            busstop = allcoord[i][2]
    return (maxdistance, busstop)



        


