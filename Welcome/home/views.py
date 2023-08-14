from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
from home.models import Contact
from home.forms import UpdateForm


# Create your views here.
def index(request):
    # return HttpResponse("THIS IS THE HOMEPAGE")
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def services(request):
    contacts = Contact.objects.all()
    return render(request, "services.html", {"contacts": contacts})


def contact(request):
    if request.method == "POST":
        id = request.POST.get("id")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        issue = request.POST.get("issue")
        contact = Contact(
            id=id,
            name=name,
            email=email,
            phone=phone,
            issue=issue,
            date=datetime.today(),
        )
        contact.save()

    return render(request, "contact.html")


def delete(request, id):
    delete = Contact.objects.get(id=id)
    delete.delete()
    return redirect("/services")


def update(request, id):
    updateData = Contact.objects.get(id=id)
    form = UpdateForm(instance=updateData)
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=updateData)
        if form.is_valid():
            form.save()
        return redirect("/services")
    context = {"form": form}
    return render(request, "update.html", context)
