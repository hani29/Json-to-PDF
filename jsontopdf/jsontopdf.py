from fpdf import FPDF
import json

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 12)
        # Move to the right
        self.cell(30)
        # Title
        self.cell(150, 10, 'General Visual Inspection of EWIS on the Main Landing Gears (EZAP)', 1, 0, 'C')

        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)
with open('files.json') as json_file:
    data = json.load(json_file)

    material = ('Materials:\n' + data['materials'])
    tools = ('\n\nSpecial_Tools_and_Equipment\n'+ data['special tools and equipment'])
    equipments = ('\n\nStandard_Tools_and_Equipment\n' + data['standard tools and equipment'])
    consumable = ('\n\nConsumable_Materials\n' + data['consumable materials'])
    Expendable = ('\n\nExpendable_Parts\n' + data['expendable parts'])
    job = ('\n\nJob_Set-up\n' + data['job set-up'])
    procedure = ('\n\nProcedure\n')
    for p in data['procedure']:
        a = ('A. ' + p['a'])
        b = ('B. ' + p['b'])
        c = ('C. ' + p['c'])
        d = ('D. ' + p['d'])
        e = ('E. ' + p['e'])
        f = ('F.' + p['f'])
        g = ('G.' + p['g'])
    jobs = ('Job Close-up')
    for p in data['job close-up']:
        aa = ('A.' + p['a'])
        bb = ('B.' + p['b'])

pdf.write(5,material)
pdf.write(5,tools)
pdf.write(5,equipments)
pdf.write(5,consumable)
pdf.write(5,Expendable)
pdf.write(5,job)
pdf.write(5,procedure)
pdf.write(5,a)
pdf.write(5,'\n\n\n')
pdf.write(5,b)
pdf.write(5,'\n\n\n')
pdf.write(5,c)
pdf.write(5,'\n\n\n')
pdf.write(5,d)
pdf.write(5,'\n\n\n')
pdf.write(5,e)
pdf.write(5,'\n\n\n')
pdf.write(5,f)
pdf.write(5,'\n\n\n')
pdf.write(5,g)
pdf.write(5,'\n\n\n')
pdf.write(5,jobs)
pdf.write(5,'\n')
pdf.write(5,aa)
pdf.write(5,'\n\n')
pdf.write(5,bb)

pdf.output('Writedata.pdf', 'F')