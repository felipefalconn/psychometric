import pandas as pd
from pathlib import Path

EPW_PATH = Path("BRA_MG_Uberlandia.867760_INMET.epw")

cols = [
    "Year", "Month", "Day", "Hour", "Minute", "DataSource",
    "DryBulb", "DewPoint", "RelHum", "AtmosPressure",
    "ExtHorRad", "ExtDirRad", "HorzIR", "GloHorRad",
    "DirNormRad", "DiffHorRad", "GloHorIll", "DirNormIll",
    "DiffHorIll", "ZenithLum", "WindDir", "WindSpd",
    "TotSkyCvr", "OpaqSkyCvr", "Visibility", "CeilingHgt",
    "PresWeathObs", "PresWeathCodes", "PrecipWtr",
    "AerosolOptTh", "SnowDepth", "DaysSinceSnow",
    "Albedo", "RainRate", "Extra"
]

df = pd.read_csv(
    EPW_PATH,
    skiprows=8,
    header=None,
    encoding="latin-1"
)

df.columns = cols

df["Pressure_kPa"] = df["AtmosPressure"] / 1000.0
avg_p = df["Pressure_kPa"].mean()
min_p = df["Pressure_kPa"].min()
max_p = df["Pressure_kPa"].max()

print("=== Mean pressure in EPW ===")
print(f"Average: {avg_p:.2f} kPa")
print(f"Minimum: {min_p:.2f} kPa")
print(f"Maximum: {max_p:.2f} kPa\n")

monthly = df.groupby("Month")[["DryBulb", "RelHum"]].mean().round(2)

month_names = {
    1: "January",  2: "February", 3: "March",     4: "April",
    5: "May",      6: "June",     7: "July",      8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

monthly["MonthName"] = monthly.index.map(month_names)

monthly_table = monthly[["MonthName", "DryBulb", "RelHum"]].rename(
    columns={
        "MonthName": "Month",
        "DryBulb": "Mean dry-bulb temperature (°C)",
        "RelHum": "Mean relative humidity (%)"
    }
)

print("=== Monthly table ===")
print(monthly_table)

idx_hot = monthly["DryBulb"].idxmax()
idx_cold = monthly["DryBulb"].idxmin()
idx_humid = monthly["RelHum"].idxmax()
idx_dry = 8
idx_comfort = 10

row_hot = monthly.loc[idx_hot]
row_cold = monthly.loc[idx_cold]
row_humid = monthly.loc[idx_humid]
row_dry = monthly.loc[idx_dry]
row_comfort = monthly.loc[idx_comfort]

points_data = [
    {
        "Situation": "Hottest month",
        "Month": month_names[idx_hot],
        "Tdb (°C)": row_hot["DryBulb"],
        "RH (%)": row_hot["RelHum"],
        "Note": "Highest annual mean temperature"
    },
    {
        "Situation": "Most humid month",
        "Month": month_names[idx_humid],
        "Tdb (°C)": row_humid["DryBulb"],
        "RH (%)": row_humid["RelHum"],
        "Note": "Highest annual mean relative humidity"
    },
    {
        "Situation": "Driest month",
        "Month": month_names[idx_dry],
        "Tdb (°C)": row_dry["DryBulb"],
        "RH (%)": row_dry["RelHum"],
        "Note": "Chosen as month with lowest comfort humidity (August)"
    },
    {
        "Situation": "Coldest month",
        "Month": month_names[idx_cold],
        "Tdb (°C)": row_cold["DryBulb"],
        "RH (%)": row_cold["RelHum"],
        "Note": "Lowest annual mean temperature"
    },
    {
        "Situation": "Typical comfort condition",
        "Month": month_names[idx_comfort],
        "Tdb (°C)": row_comfort["DryBulb"],
        "RH (%)": row_comfort["RelHum"],
        "Note": "Close to (24 °C, 50%)"
    },
]

points_table = pd.DataFrame(points_data)

print("\n=== Representative points table ===")
print(points_table)