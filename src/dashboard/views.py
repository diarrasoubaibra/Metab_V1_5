from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from school.models.app_setting_model import AppSettingsModel
from school.models.school_model import SchoolModel
from school.views.decorator_views import check_settings

@login_required(login_url='user:login')
@check_settings
def dashboard(request):
    appsettings = AppSettingsModel.objects.all()
    schools = SchoolModel.objects.all()
    context = {
        'appsettings': appsettings,
        'schools': schools,
    }
    
    return render(request, "dashboard/dashboard.html", context)