from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.image("shirtificate.png", x=10, y=60 , w=pdf.epw)
    pdf.set_font("helvetica", size=32)
    pdf.cell(0, 50,txt="CS50 Shirtificate", align="C", center=True)
    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 250,txt=f"{name} took CS50", align="C", center=True)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()