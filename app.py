# -*- coding:utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
import plotly.plotly as py


def main():

    st.markdown("# Hello World")
    st.write(np.__version__)
    st.write(pd.__version__)
    st.write(plt.__version__)
    st.write(sns.__version__)
    st.write(sk.__version__)
    st.write(py.__version__)

if __name__ == "__main__":
        main()