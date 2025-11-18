# Psychrometric Analysis — Uberlândia (INMET EPW)

This repository contains the workflow used to perform a complete psychrometric analysis of the city of Uberlândia (Brazil), based on hourly climate data obtained from the INMET EPW file.  
The project extracts, processes, and summarizes the main thermodynamic variables required for comfort analysis, HVAC sizing, and thermodynamics coursework.

<img width="1132" height="591" alt="image" src="https://github.com/user-attachments/assets/d2f6cf47-a24f-4aab-b2e9-2ba3937f1db1" />


---

## Repository Structure

```
psychometric/
│
├── BRA_MG_Uberlandia.867760_INMET.epw      # EPW climate file (INMET)
├── main.py                                 # Data extraction and analysis script
├── json-process-lines.json                 # Psychrometric process lines from Andrew Marsh
├── svg-dos-resultados.svg                  # Psychrometric chart with representative points
├── .venv/                                  # Python virtual environment (optional)
└── README.md
```

---

## Overview

The project performs:

- Extraction of hourly meteorological data from an EPW file  
- Computation of:
  - Monthly mean dry-bulb temperature (°C)
  - Monthly mean relative humidity (%)
  - Mean atmospheric pressure
- Identification of representative psychrometric points:
  - Hottest month  
  - Coldest month  
  - Most humid month  
  - Driest winter month (fixed as August for consistency)  
  - Typical comfort month (closest to 24 °C, 50% RH)
- Export of psychrometric process lines from the Andrew Marsh online tool
- Generation of tables used in the final thermodynamics report

---

## Methodology Summary

### 1. Climate Data
The input EPW file is provided by INMET (Brazilian National Institute of Meteorology).

### 2. Data Processing
`main.py` loads the EPW file, assigns EnergyPlus column names, converts pressure to kPa, and computes monthly means.

### 3. Representative Psychrometric Points
The script identifies five key situations:

| Situation                 | Meaning |
|--------------------------|---------|
| Hottest month            | Highest mean dry-bulb temperature |
| Most humid month         | Highest mean RH |
| Driest winter month      | Lowest winter RH (August) |
| Coldest month            | Lowest mean dry-bulb temperature |
| Typical comfort month    | Month closest to 24 °C and 50% RH |

The resulting points are plotted on the psychrometric chart (SVG file).

---

## Requirements

- Python 3.10+
- Pandas

Optional:
- Virtual environment

---

## Installation and Usage

### Create a virtual environment
```bash
python -m venv .venv
```

### Activate it
Linux/Mac:
```bash
source .venv/bin/activate
```

Windows:
```bash
.venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the analysis
```bash
python main.py
```

---

## Example Output

```
=== EPW mean pressure ===
Mean:   91.71 kPa
Min:    90.57 kPa
Max:    92.53 kPa

=== Monthly mean table ===
 Month     Mean Tdb (°C)   Mean RH (%)
 January        22.97          78.22
 ...
 December       24.22          72.29

=== Representative points table ===
         Situation             Month   Tdb   RH        Note
  Hottest month             September 24.69  37.65  Highest annual mean temperature
  Most humid month           January  22.97  78.22  Highest annual mean RH
  Driest winter month        August   21.97  40.61  Lowest winter RH
  Coldest month               July    20.39  52.99  Lowest annual temperature
  Typical comfort condition   October 24.24  58.96  Close to (24°C, 50%)
```

---

## Psychrometric Chart

The file `svg-dos-resultados.svg` contains:

- Five representative climate points
- The selected indoor comfort point (24 °C, 50% RH)
- Process lines exported from Andrew Marsh’s web tool

These process lines are saved in `json-process-lines.json`, matching the graphical representation.

---

