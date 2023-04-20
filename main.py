import pandas as pd
from fpdf import FPDF

pdf = FPDF(orientation = "P", unit = "mm", format = "A4")

df = pd.read_csv("topics.csv")

for inxex, row in  df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10.0, 21.0, 200.0, 21.0)
    for i in range(row["Pages"] - 1):
        pdf.add_page()

pdf.output("output.pdf")
