from django.contrib.auth.models import Group
from django import forms
from django.forms import ModelForm
from aplication.security.models import GroupModulePermission, Module

class GroupModulePermissionForm(ModelForm):
    class Meta:
        model = GroupModulePermission
        fields = ["group", "module", "permissions"]
        widgets = {
            "group": forms.Select(
                attrs={
                    "id": "id_group",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:text-gray-400 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "module": forms.Select(
                attrs={
                    "id": "id_module",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:text-gray-400 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "permissions": forms.SelectMultiple(
                attrs={
                    "id": "id_permissions",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:text-gray-400 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
        }
        labels = {
            "group": "Grupo",
            "module": "Módulo",
            "permissions": "Permisos",
        }
