from kiteconnect import KiteConnect
import streamlit as st

def get_kite():
    api_key = st.secrets[" 1jahcv7cqzcrgw17"]
    access_token = st.secrets["plylgLwOi5ioo2nkqBh0VRyw1DYzKHnp"]

    kite = KiteConnect(api_key=api_key)
    kite.set_access_token(access_token)
    return kite
