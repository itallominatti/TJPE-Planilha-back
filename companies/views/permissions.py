from companies.views.base import Base
from companies.utils.permissions import EmployeesPermission, GroupsPermission
from companies.models import Employee, Tjpe
from companies.serializers import PermissionsSerializer
from companies.utils.enum import CompanyStatus

from rest_framework.response import Response

from django.contrib.auth.models import Permission

class PermissionDetail(Base):
    permission_classes = [GroupsPermission]

    def get(self, request):
        permissions = Permission.objects.filter(
            content_type_id__in=[
                CompanyStatus.PERMISSION.value,
                CompanyStatus.GROUP_PERMISSIONS.value,
                CompanyStatus.EMPLOYEE.value,
                CompanyStatus.TASK.value
            ]
        ).all()

        serializer = PermissionsSerializer(permissions, many=True)

        return Response({
            'permissions': serializer.data
        })

        ...