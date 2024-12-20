from django.contrib.auth import get_user_model, login
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.decorators.http import require_POST
from djapy import djapify, SessionAuth

from authentication.schemas.auth_schema import LoginSchema
from authentication.models import ConfirmMailToken
from authentication.schemas import UserRegisterSchema, AuthOutSchema
from generics.schemas import MessageOut, Inline, ActionMessageOut


@djapify(allowed_method="POST")
@csrf_exempt
def register_user(request, user_payload: UserRegisterSchema) -> {201: MessageOut, 400: MessageOut | Inline}:
   """
   Register User
   If user is registered successfully, user will be logged in, and email will be sent to user's email
   with confirmation link. Also, login token will be returned in response headers.
   ```
   Set-Cookie: sessionid=<session_string>; expires=<time>; HttpOnly; Max-Age=<time>; Path=/; SameSite=Lax
   ```
   """
   try:
      user = get_user_model().objects.create_user(
         username=user_payload.username,
         email=user_payload.email,
         password=user_payload.password
      )
      ConfirmMailToken.send_token(request, user)
   except IntegrityError:
      return 400, {
         "inline": {
            "username": "User with this username already exists.",
            "email": "User with this email already exists."
         }
      }
   except ConnectionRefusedError:
      return 400, {
         "message": "User registered, but email could not be sent.",
         "message_type": "error",
         "alias": "email_not_sent"
      }

   login(request, user)

   return 201, {
      "message": "User registered successfully.",
      "message_type": "success",
      "alias": "register_success",
      "redirect": "/"
   }


@ensure_csrf_cookie
@csrf_exempt
@djapify(allowed_method="POST")
def login_user(request, data: LoginSchema) -> {200: ActionMessageOut, 400: Inline}:
   """
   Login User
   If user is logged in successfully, login token will be returned in response headers.
   ```
   Set-Cookie: sessionid=<session_string>; expires=<time>; HttpOnly; Max-Age=<time>; Path=/; SameSite=Lax
   ```
   """

   try:
      if data.username:
         user_dict = dict(username=data.username)
      else:
         user_dict = dict(email=data.email)
      user = get_user_model().objects.get(**user_dict)
   except get_user_model().DoesNotExist or get_user_model().MultipleObjectsReturned:
      return 400, {
         "inline": {
            "username": "User with this username does not exist.",
            "email": "User with this email does not exist."
         }
      }

   success = user.check_password(data.password)

   if success:
      login(request, user)
      return {
         "message": "User logged in successfully.",
         "message_type": "success",
         "alias": "register_success",
         "redirect": "/"
      }
   else:
      return 400, {
         "inline": {
            "password": "Password is incorrect."
         }
      }

@djapify(auth=SessionAuth)
def logout_user(request) -> {200: AuthOutSchema}:
   """
   Logout user
   """
   request.user.auth_token.delete()
   return 200, request

# @ensure_csrf_cookie
# @djapify(allowed_method="OPTIONS")
# @csrf_exempt
# def assign_csrf_token(request, response: HttpResponse) -> Any:
#     return response
