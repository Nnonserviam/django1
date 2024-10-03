from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Producto, Categoria

admin.site.register(Producto)
admin.site.register(Categoria)  
