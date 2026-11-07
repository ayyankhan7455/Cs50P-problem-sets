from fpdf import FPDF


class PDF(FPDF):

    def header(self):
        self.set_font("helvetica", "B", 24)
        self.cell(0, 50, "CS50 Shirtificate", align="C")
        self.ln(20)


def main():
    name = input("Name: ")

    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.image("shirtificate.png", x=10, y=70, w=190)

    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 26)

    pdf.set_xy(0, 140)
    pdf.cell(210, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
