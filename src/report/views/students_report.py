import openpyxl
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from user.models.user_model import UserModel
from teacher.models.teacher_model import TeacherModel
from student.models.student_model import StudentModel

def export_to_excel(request, report_type):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = report_type.capitalize()

    if report_type == 'users':
        headers = ['Pseudo', 'Role', 'School', 'Is Active']
        sheet.append(headers)
        for user in UserModel.objects.all():
            sheet.append([user.pseudo, user.role.name, user.school.name, user.is_active])
    elif report_type == 'teachers':
        headers = ['First Name', 'Last Name', 'Specialty', 'Available']
        sheet.append(headers)
        for teacher in TeacherModel.objects.all():
            sheet.append([teacher.first_name, teacher.last_name, teacher.specialty, teacher.available])
    elif report_type == 'students':
        headers = ['First Name', 'Last Name', 'Matricule', 'Phone Number Father']
        sheet.append(headers)
        for student in StudentModel.objects.all():
            sheet.append([student.first_name, student.last_name, student.matricule, student.phone_number_father])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={report_type}.xlsx'
    workbook.save(response)
    return response

def export_to_pdf(request, report_type):
    if report_type == 'users':
        data = UserModel.objects.all()
        template_name = 'user_report.html'
    elif report_type == 'teachers':
        data = TeacherModel.objects.all()
        template_name = 'teacher_report.html'
    elif report_type == 'students':
        data = StudentModel.objects.all()
        template_name = 'student_report.html'

    html = render_to_string(template_name, {'data': data})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename={report_type}.pdf'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Erreur lors de la génération du PDF', status=400)
    return response
