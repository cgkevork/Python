#! usr/bin/python

# Now that we've processed JSON, moved into into a database an set up some helpful 
# prewritten queries for new records, we're going to talk about the flip side of that: 
# exporting data to JSON for use elsewhere.

# PROBLEM: We have some cool crime data and have set up the automated analysis
# of weekly records for interesting trends we may want to keep regular tabs
# on. It all comes with coordinates, though; why don't we use that to our
# advantage and generate some stuff we can actually see?

# HOW WE'RE GOING TO DEAL WITH IT:
#   - Query our database, crawl through the rows of results to make a GeoJSON
#     file of points from scratch for display when connected to a Leaflet map.
#   - Query our database again while going through an existing GeoJSON and
#     adding data to it, that way we can display the result.





# Connect to the crime.db we made earlier and grab all the homicide records.










# The GeoJSON format for points we'll need to write. Don't worry, we'll break it down!
#
# { "type": "FeatureCollection",
# 	"features": [
# 		{ "type": "Feature",
# 		"geometry": {"type": "Point", "coordinates": [<LONG_X>, <LAT_Y>]},
#         "properties": {"<PROPNAME>": "<PROPVALUE>"}
#         },
# 		{ "type": "Feature",
#         <...>
#         }
#     ]
# }

# As we've learned, the dict data type doesn't have an order. Fortunately,
# there's an OrderedDict object we can pull out here to keep our GeoJSON
# structured properly.














	
# Check the format to make sure it's looking like we expect:
# print json.dumps(homicide_json, indent=4)

# Let's open a file and write all of it. Because JavaScript is a weird beast,
# we need to prefix our GeoJSON output with a "var <whatever> ="




	

# The next step's a little more complicated; we're going to parse an existing 
# GeoJSON file that shows all of Chicago's communities and add a property 
# to it. 

# First thing to do is load the GeoJSON




	
# Let's also summon that long query from last time that calculates a violent 
# crime rate from the same data. Slight tweak: we're adding the column with
# community ID numbers.

# viol_rate_sql = '''SELECT chicago_areas.comm_id, chicago_areas.comm_name, ROUND((crime_query.violent_crimes*1.0/chicago_areas.pop2010) * 10000,2) as rate
#          FROM (
#                SELECT community_area, COUNT(*) AS violent_crimes
#                FROM week
#                WHERE primary_type in ('HOMICIDE', 'CRIM SEXUAL ASSAULT', 'ROBBERY', 'ASSAULT', 'BATTERY')
#                GROUP BY 1
#                ) as crime_query, chicago_areas
#          WHERE crime_query.community_area = chicago_areas.comm_id
#          ORDER BY 3 DESC'''
         



# Now we need to walk through the list of 'features' in our GeoJSON file, checking
# the community ID number against the community IDs in our violent crime list. If
# they match, we're going to insert a property called 'VC_RATE.'











# Close the database when we're all done. 	

