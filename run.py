from django.contrib.gis.geos import GEOSGeometry

assert GEOSGeometry('POINT(2.350643 48.880848)', srid=4326).ewkt == 'SRID=4326;POINT (2.350643 48.880848)'

print(GEOSGeometry('POINT(2.350643 48.880848)', srid=4326).transform(3857, True).ewkt)
ewkt = GEOSGeometry('POINT(2.350643 48.880848)', srid=4326).transform(3857, True).ewkt

assert "(261672" in ewkt
assert "6254667" in ewkt
