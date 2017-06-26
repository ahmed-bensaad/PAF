geo_json_geometry = {
  "type": "Polygon",
  "coordinates": [
    [
       [
              -122.431640625,
              37.65338320128765
            ],
            [
              -122.31628417968749,
              37.65338320128765
            ],
            [
              -122.31628417968749,
              37.75334401310656
            ],
            [
              -122.431640625,
              37.75334401310656
            ],
            [
              -122.431640625,
              37.65338320128765
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
    "gte": "2016-04-30T00:00:00.000Z",
    "lte": "2016-09-10T00:00:00.000Z"
  }
}

# filter any images which are more than 10% clouds
cloud_cover_filter = {
  "type": "RangeFilter",
  "field_name": "cloud_cover",
  "config": {
    "lte": 0.1
  }
}
# filter any images which are more than 50% black
black_filter = {
  "type": "RangeFilter",
  "field_name": "black_fill",
  "config": {
    "lte": 0.5
  }
}

# create a filter that combines our geo and date filters
# could also use an "OrFilter"
redding_reservoir = {
  "type": "AndFilter",
  "config": [geometry_filter, date_range_filter, cloud_cover_filter,black_filter]
}



