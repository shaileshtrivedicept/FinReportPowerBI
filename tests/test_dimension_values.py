import pandas as pd
import os

def test_entity_values():
    df = pd.read_csv("data/templates/dim_entity.csv")
    assert set(df["Entity"].tolist()) == {"CRDF", "CAF", "Combined"}

def test_centre_values():
    df = pd.read_csv("data/templates/dim_centre.csv")
    expected = ["CUPP", "CARBSE", "CWAS", "CEI", "CHC", "CAG", "CAU", "CoEUT", "HO", "Legacy", "Other"]
    assert all(c in df["Centre"].tolist() for c in expected)

def test_month_range():
    df = pd.read_csv("data/templates/dim_month.csv")
    assert df["Month"].iloc[0] == "2024-04-30"
    assert df["Month"].iloc[-1] == "2028-03-31"
