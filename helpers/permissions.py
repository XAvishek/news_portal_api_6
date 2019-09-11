from rest_framework import permissions

class IsNewsCreator(permissions.BasePermission):
    
    def has_permission(self, request, view):
        try:
            role = request.user.role
            print(role)
        except Exception as e: 
            print(e)
            return False
        else:
            """
            0: super
            1: admin
            2: reporter
            """
            return str(role) in "012"

class IsNewsModifier(permissions.BasePermission):
    def has_object_permission(self, request,view, object):
        return request.user == object.reporter or request.user.role in "01"