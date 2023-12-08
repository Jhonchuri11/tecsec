from rest_framework.views import APIView
from .serializers import UserSerializer, clienteLoginSerializer, clienteSerializer
from rest_framework.response import Response
from .models import User, Clientes
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework import generics
from rest_framework import status
from django.contrib.auth import authenticate, login

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
           serializer.save()
           response_data = {
             "message": "Registro exitoso"
           }
           return Response(response_data, status=201)
        else:
            return Response(serializer.errors, status=400)

# Otra muestra
class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED , headers=headers)

# Usando la entidad cliente para registro
class RegisterClient(generics.CreateAPIView):
    queryset = Clientes.objects.all()
    serializer_class = clienteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'message': 'Cliente creado correctamente'}, status=status.HTTP_201_CREATED, headers=headers)
        except ValueError as error:
            return Response({'error': error.detail}, status=status.HTTP_400_BAD_REQUEST)

class LoginClient(APIView):
    def post(self, request, *args, **kwargs):
        serializer = clienteLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        # Autenticar al usuario utilizando tu modelo Cliente
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            return Response({'message': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciales no válidas'}, status=status.HTTP_401_UNAUTHORIZED)
# Login 
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('Usuario no funcional')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Contraseña incorrecta')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'numero': user.numero,
            'password': user.password
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'success': True,
            'data': {
                'user': user_data,
            },
            'jwt': token,
            'message': "Inicio de sesión exitoso"
        }
        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('No conectado!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('No conectado!')
        
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)
    
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data =  {
            'message': 'success' 
        }
        return response




