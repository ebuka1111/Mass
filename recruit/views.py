from django.shortcuts import render, redirect
from .forms import EmployeeForm
from rest_framework import status
from rest_framework.response import Response



# def Homepage(request):
#     if request.method == "POST":
#         first_name = request.POST.get("first_name")
#         middle_name = request.POST.get("middle_name")
#         last_name = request.POST.get("last_name")
#         home_address = request.POST.get("home_address")
#         phone_number = request.POST.get("phone_number")
#         ssn = request.POST.get("ssn")
#         id_document = request.POST.get("id_documents")
#         Images = request.POST.get("images")
#         former_workplace = request.POST.get("former_workplace")
#         workplace_address = request.POST.get("workplace_address")
#         reason_for_leaving = request.POST.get("reason_for_leaving")
#         Employee.objects.create(first_name=first_name, middle_name=middle_name, last_name=last_name, home_address=home_address,
#                                phone_number=phone_number, ssn=ssn, id_document=id_document, Images=Images, former_workplace=former_workplace,
#                                  workplace_address=workplace_address,reason_for_leaving=reason_for_leaving)
#         return redirect("home")
        
#     else:
#         return render(request, "recruit/index.html")
    





def Homepage(request):
    form = EmployeeForm(request.POST) 

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'recruit/index.html') 
        else:
            return render(request, 'recruit/index.html', {'form': form})
        
    return render(request, 'recruit/index.html', {'form': form})
