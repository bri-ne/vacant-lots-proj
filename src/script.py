from classes.featurelayer import FeatureLayer
from config.psql import conn
from constants.services import VACANT_PROPS_LAYERS_TO_LOAD
from data_utils.city_owned_properties import city_owned_properties
from data_utils.phs_properties import phs_properties
from data_utils.l_and_i import l_and_i
from data_utils.rco_geoms import rco_geoms
from data_utils.tree_canopy import tree_canopy
from data_utils.gun_crimes import gun_crimes


"""
Load Vacant Properties Datasets
"""


vacant_properties = FeatureLayer(
    name="Vacant Properties", esri_rest_urls=VACANT_PROPS_LAYERS_TO_LOAD
)


"""
Load City Owned Properties
"""
vacant_properties = city_owned_properties(vacant_properties)


"""
Load PHS Data
"""
vacant_properties = phs_properties(vacant_properties)


"""
Load L&I Data
"""
vacant_properties = l_and_i(vacant_properties)

"""
Merge RCOs
"""
vacant_properties = rco_geoms(vacant_properties)


"""
Load Tree Canopy Data
"""
vacant_properties = tree_canopy(vacant_properties)


"""
Gun Crime Data
"""
vacant_properties = gun_crimes(vacant_properties)


# Clean up
vacant_properties.gdf.to_postgis(
    "vacant_properties_end", conn, if_exists="replace", index=False
)
conn.close()
