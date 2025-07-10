import streamlit as st
from st_cytoscape import cytoscape

elements = [
    {"data": {"id": "X"}, "selected": True, "selectable": False},
    {"data": {"id": "Y"}},
    {"data": {"id": "Z"}},
    {"data": {"source": "X", "target": "Y", "id": "X➞Y"}},
    {"data": {"source": "Z", "target": "Y", "id": "Z➞Y"}},
    {"data": {"source": "Z", "target": "X", "id": "Z➞X"}},
]

stylesheet = [
    {"selector": "node", "style": {"label": "data(id)", "width": 20, "height": 20}},
    {
        "selector": "edge",
        "style": {
            "width": 3,
            "curve-style": "bezier",
            "target-arrow-shape": "triangle",
        },
    },
]

selected = cytoscape(elements, stylesheet, key="graph")

st.markdown("**Selected nodes**: %s" % (", ".join(selected["nodes"])))
st.markdown("**Selected edges**: %s" % (", ".join(selected["edges"])))