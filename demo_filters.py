#def setcoords():
#    L=[]
#    print("saisissez les coordonnées: absisse et ordonnées séparée par un espace, deux points séparés par une virgule")
#    ch=input()
#    L=ch.split(',')
#    for i in range (len(L)):
#        L[i]=L[i].split(' ')
#    geo_json_geometry["coordinates"]=[L]
#    
#def settime():
#    print("Saisissez la date de début: format aaa-mm-jjThh:mm:ss.000Z")
#    ch=input()
#    

geo_json_geometry = {
  "type": "Polygon",
  "coordinates": [
    [
       [
              -122.05398559570312,
              37.421435292172944
            ],
            [
              -121.94000244140624,
              37.421435292172944
            ],
            [
              -121.94000244140624,
              37.49229399862877
            ],
            [
              -122.05398559570312,
              37.49229399862877
            ],
            [
              -122.05398559570312,
              37.421435292172944
            ]
    ]
  ]
}

# filter for items the overlap with our chosen geometry
geometry_filter = {
  "type": "GeometryFilter",
  "field_name": "geometry",
  "config": geo_json_geometry
}

# filter images acquired in a certain date range
date_range_filter = {
  "type": "DateRangeFilter",
  "field_name": "acquired",
  "config": {
    "gte": "2016-09-01T00:00:00.000Z",
    "lte": "2017-01-01T00:00:00.000Z"
  }
}

# filter any images which are more than 50% clouds
cloud_cover_filter = {
  "type": "RangeFilter",
  "field_name": "cloud_cover",
  "config": {
    "lte": 0.1
  }
}

# create a filter that combines our geo and date filters
# could also use an "OrFilter"
redding_reservoir = {
  "type": "AndFilter",
  "config": [geometry_filter, date_range_filter, cloud_cover_filter]
}