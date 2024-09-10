from django.http import HttpResponse
import openpyxl
from django.shortcuts import render
from reportlab.pdfgen import canvas
from user.models.user_model import UserModel
from teacher.models import TeacherModel
from student.models import StudentModel
from django.contrib.auth.decorators import login_required
from school.views.decorator_views import check_settings

@login_required(login_url='user:login')
@check_settings
def generate_pdf_report(request, report_type):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{report_type}_report.pdf"'

    p = canvas.Canvas(response)

    # Récupérer les données en fonction du type de rapport
    if report_type == 'users':
        items = UserModel.objects.all()
        p.drawString(100, 750, "Liste des Utilisateurs")
    elif report_type == 'teachers':
        items = TeacherModel.objects.all()
        p.drawString(100, 750, "Liste des Professeurs")
    elif report_type == 'students':
        items = StudentModel.objects.all()
        p.drawString(100, 750, "Liste des Élèves")
    else:
        p.drawString(100, 750, "Type de rapport non valide")
        p.showPage()
        p.save()
        return response

    # Ajouter les données dans le PDF
    y = 730
    for item in items:
        p.drawString(100, y, str(item))
        y -= 20

    p.showPage()
    p.save()
    return response

@login_required(login_url='user:login')
@check_settings
def generate_excel_report(request, report_type):
    # Créer un nouveau fichier Excel
    wb = openpyxl.Workbook()
    ws = wb.active

    # Récupérer les données en fonction du type de rapport
    if report_type == 'users':
        ws.title = "Utilisateurs"
        items = UserModel.objects.all()
        ws.append(['Pseudo', 'Date de création'])
        for item in items:
            # Vérification pour s'assurer que la date n'a pas de timezone
            created_at = item.created_at.replace(tzinfo=None) if item.created_at and item.created_at.tzinfo else item.created_at
            ws.append([item.pseudo, created_at])  # Adapte selon ton modèle

    elif report_type == 'teachers':
        ws.title = "Professeurs"
        items = TeacherModel.objects.all()
        ws.append(['Nom', 'Prénom', 'Numéro'])
        for item in items:
            ws.append([item.last_name, item.first_name, item.phone_number])  # Adapte selon ton modèle

    elif report_type == 'students':
        ws.title = "Élèves"
        items = StudentModel.objects.all()
        ws.append(['Nom', 'Prénom', 'Matricule'])
        for item in items:
            ws.append([item.last_name, item.first_name, item.matricule])  # Adapte selon ton modèle

    else:
        ws.append(['Type de rapport non valide'])

    # Configurer la réponse HTTP
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{report_type}_report.xlsx"'
    wb.save(response)
    return response

@login_required(login_url='user:login')
@check_settings
def report(request):
    
    return render(request, "report/report.html")