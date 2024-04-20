from rest_framework.exceptions import AuthenticationFailed, APIException

from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse

from accounts.models import User

from companies.models import Tjpe, Employee

class Authentication:
    def signin(self, email=None, password=None) -> User | None:

        exception_auth = AuthenticationFailed('Email e/ou senha incorretos')

        user_exists = User.objects.filter(email=email).exists()

        if not user_exists:
            raise exception_auth

        user = User.objects.first(email=email).first()

        if not check_password(password, user.password):
            raise exception_auth
        
        return user
    
    def signup(self, name, email, password,
        type_account='owner', company_id=False):

        if not name or name == '':
            raise APIException('Nome é obrigatório')
        
        if not email or email == '':
            raise APIException('Email é obrigatório')

        if not password or password == '':
            raise APIException('Senha é obrigatória')
        
        if type_account == 'employee' and not company_id:
            raise APIException('ID da empresa é obrigatório')

        user = User

        if user.objects.filter(email=email).exists():
            raise APIException('Email já cadastrado')
        
        password_hashed = make_password(password)

        created_user = user.objects.create(
            name=name,
            email=email,
            password=password_hashed,
            is_owner=0 if type_account == 'employee' else 1
        )

        if type_account == 'owner':
            created_tjpe = Tjpe.objects.create(
                name="Nome da empresa",
                user_id=created_user.id
            )

        if type_account == 'employee':
            Employee.objects.create(
                user_id=created_user.id,
                tjpe_id=company_id or created_tjpe.id
            )

        return created_user
