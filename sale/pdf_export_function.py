from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from openpyxl import Workbook
from django.http import JsonResponse, HttpResponse



def export_products_to_pdf(products):
    
    response = HttpResponse(content_type='application/pdf')

   
    response['Content-Disposition'] = 'attachment; filename=sotuvlar.pdf'

   
    pdf = SimpleDocTemplate(response, pagesize=letter)


    data = [["Klient", "Mahsulot", "soni", "summa", "Valyuta", "tolov turi", "muddati", "jami"]]
    for i in products:
        data.append([i.customer_name,i.product.category.name, i.quantity, i.product.price, i.currency, i.payment_type,i.deadline, i.sum_()])

   
    table = Table(data)

  
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)


    pdf.build([table])

    return response