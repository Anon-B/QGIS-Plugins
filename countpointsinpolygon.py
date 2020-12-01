import processing

input_polygon = r"C:\Users\Anon\Desktop\UP\gis\hexagon.shp"
input_point =r"C:\Users\Anon\Desktop\UP\gis\accident.shp"
Result = r"D:\saved_output.shp"

# Count points in polygon
alg_params = {
    'POINTS': input_point,
    'POLYGONS': input_polygon,
    'CLASSFIELD': '',
    'WEIGHT': '',
    'FIELD': 'count',    
    'OUTPUT': Result
    }
    
processing.run('native:countpointsinpolygon', alg_params)
