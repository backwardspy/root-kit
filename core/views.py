from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


class Index(LoginRequiredMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "index.html")


class Register(View):
    form_class = UserCreationForm

    def get(self, request: HttpRequest) -> HttpResponse:
        form = self.form_class()
        return render(request, "registration/register.html", {"form": form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            return render(request, "registration/register.html", {"form": form})
