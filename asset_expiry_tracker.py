import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta


# Read Excel asset data
file = "Asset_Inventory.xlsx"

assets = pd.read_excel(file)


# Define warranty period for each device type (in years)

warranty_periods = {
    "Dell Laptop": 3,
    "HP Printer": 1,
    "Cisco IP Phone": 5,
    "Monitor": 2,
    "Lenovo Laptop": 3
}


# Convert Purchase Date into date format

assets["Purchase Date"] = pd.to_datetime(
    assets["Purchase Date"],
    dayfirst=True
)


# Function to calculate warranty expiry date

def calculate_expiry(row):

    device = row["Device"]
    purchase_date = row["Purchase Date"]

    warranty_years = warranty_periods.get(device, 1)

    expiry_date = purchase_date + relativedelta(
        years=warranty_years
    )

    return expiry_date


# Add Warranty Expiry column

assets["Warranty Expiry"] = assets.apply(
    calculate_expiry,
    axis=1
)


# Check warranty status

today = datetime.today()


def check_status(expiry_date):

    if expiry_date < today:
        return "Expired"

    elif expiry_date <= today + relativedelta(months=3):
        return "Expiring Soon"

    else:
        return "Active"



# Add Status column

assets["Status"] = assets["Warranty Expiry"].apply(
    check_status
)


# Generate final report

report_file = "Asset_Warranty_Report.xlsx"

assets.to_excel(
    report_file,
    index=False
)


print("Asset Warranty Report Generated Successfully!")
