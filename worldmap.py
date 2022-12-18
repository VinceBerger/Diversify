import streamlit as st
import leafmap 

filepath = "https://github.com/VinceBerger/Diversify/blob/Streamlit/worldmapliste.csv"
m = leafmap.Map(center=[40, -100], zoom=4, tiles="stamentoner")
m.add_heatmap(
    filepath,
    latitude="latitude",
    longitude="longitude",
    value="pop_max",
    name="Heat map",
    radius=20,
)
