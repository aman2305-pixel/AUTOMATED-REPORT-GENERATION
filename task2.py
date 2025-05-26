import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Sample data
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 90, 78]
})

# Create bar chart and save as image
plt.figure(figsize=(6, 4))
plt.bar(data['Name'], data['Score'], color='skyblue')
plt.title('Student Scores')
plt.xlabel('Name')
plt.ylabel('Score')
plt.tight_layout()
chart_path = 'score_chart.png'
plt.savefig(chart_path)
plt.close()

# PDF class with header and table
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 10, "Student Score Report", border=False, ln=True, align='C')
        self.ln(10)

    def table_header(self):
        self.set_font("Arial", 'B', 12)
        self.cell(90, 10, "Name", border=1, align='C')
        self.cell(40, 10, "Score", border=1, align='C')
        self.ln()

    def table_rows(self, data):
        self.set_font("Arial", '', 12)
        for i, row in data.iterrows():
            self.cell(90, 10, row['Name'], border=1, align='L')
            self.cell(40, 10, str(row['Score']), border=1, align='C')
            self.ln()

# Create PDF
pdf = PDF()
pdf.add_page()
pdf.table_header()
pdf.table_rows(data)

# Add the chart image
pdf.ln(10)
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Score Chart:", ln=True)
pdf.image(chart_path, x=30, w=150)

# Save PDF
pdf.output("report_with_chart.pdf")
