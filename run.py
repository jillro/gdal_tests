from django.contrib.gis.geos import GEOSGeometry

assert GEOSGeometry('POINT(2.350643 48.880848)', srid=4326).ewkt == 'SRID=4326;POINT (2.350643 48.880848)'

assert GEOSGeometry('POINT(2.350643 48.880848)', srid=4326).transform(3857, True).ewkt == 'SRID=3857;POINT (261672.381796773 6254667.92282535)'