from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def gerar_relatorio(nome, cargo, horas):
    c = canvas.Canvas("relatorio.pdf", pagesize=A4)
    c.setFont("Helvetica", 12)
    c.drawString(100, 800, f"Relatório de Funcionário")
    c.drawString(100, 770, f"Nome: {nome}")
    c.drawString(100, 750, f"Cargo: {cargo}")
    c.drawString(100, 730, f"Horas Trabalhadas: {horas}")
    c.save()
    print("Relatório gerado com sucesso!")

gerar_relatorio("Alexandre", "Estagiário de TI", 120)