import json

from .BaseCtl import BaseCtl
from django.shortcuts import render
from ..utility.DataValidator import DataValidator
from ..models import User
from ..service.ChangePasswordService import ChangePasswordService
from ..service.EmailService import EmailService
from ..service.EmailMessege import EmailMessege
from ..service.UserService import UserService


class ChangePasswordCtl(BaseCtl):

    def request_to_form(self, requestFrom):
        self.form['id'] = requestFrom['id']
        self.form['oldPassword'] = requestFrom['oldPassword']
        self.form['newPassword'] = requestFrom['newPassword']
        self.form['confirmPassword'] = requestFrom['confirmPassword']

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if (pk > 0):
            obj.id = pk
        obj.oldPassword = self.form['oldPassword']
        obj.newPassword = self.form['newPassword']
        obj.confirmPassword = self.form['confirmPassword']
        return obj

    def model_to_form(self, obj):
        if (obj == None):
            return
        self.form['id'] = obj.id
        self.form['oldPassword'] = obj.oldPassword
        self.form['newPassword'] = obj.newPassword
        self.form['confirmPassword'] = obj.confirmPassword

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['oldPassword'])):
            inputError['oldPassword'] = "Old Password can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['newPassword'])):
            inputError['newPassword'] = "New Password can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['confirmPassword'])):
            inputError['confirmPassword'] = "Confirm Password can not be null"
            self.form['error'] = True

        return self.form['error']

    def display(self, request, params={}):
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def submit(self, request, params={}):
        json_request = json.loads(request.body)
        self.request_to_form(json_request)
        res = {"result": {}, "success": True}
        if (self.input_validation()):
            res["success"] = False
            res["result"]["inputerror"] = self.form["inputError"]
        else:
            user_json = request.session.get('user', None)
            q = User.objects.filter(loginId=user_json.get('loginId'), password=self.form['oldPassword'])
            user = q[0]
            if q.count() > 0:
                if self.form['newPassword'] == self.form['confirmPassword']:
                    emailMessege = EmailMessege()
                    emailMessege.to = [user.loginId]
                    emailMessege.subject = "Change Password"
                    mailResponse = EmailService.send(emailMessege, 'changePassword', user)

                    # if mailResponse == 1:
                    if True:
                        user.password = self.form['newPassword']
                        user.confirmPassword = self.form['confirmPassword']

                        UserService().save(user)

                        res["success"] = True
                        res["result"]["inputerror"] = "your password has been changed successfully, please check your mail..."
                    else:
                        res["success"] = False
                        res["result"]["inputerror"] = "Please Check Your Internet Connection"
                else:
                    res["success"] = False
                    res["result"]["inputerror"] = "Confirm Password are not matched"
            else:
                res["success"] = False
                res["result"]["inputerror"] = "Old Password is wrong"
        return JsonResponse(res)

    def get_service(self):
        return ChangePasswordService()
