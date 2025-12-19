import pandas as pd

COLUMN_MAP = {
    "First Name": "prospect_name",
    "Title": "title",
    "Company Name": "company_name",
    "Email": "email",
    "Person Linkedin Url": "linkedin_url",
    "# Employees": "company_size",
    "Industry": "industry",
    "Country": "country",
}

def load_leads_from_csv(file_path):
    df = pd.read_csv(file_path)
    leads = []

    for row in df.to_dict(orient="records"):
        lead = {}

        for csv_key, schema_key in COLUMN_MAP.items():
            value = row.get(csv_key)
            if pd.isna(value):
                lead[schema_key] = None
            else:
                lead[schema_key] = str(value)

        leads.append(lead)

    return leads
