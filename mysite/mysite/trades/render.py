from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa

import os
from random import randint
from trades.models import Report

class Render:

    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)

    @staticmethod
    def render_to_file(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        file_name = "{0}.pdf".format(randint(1, 1000000))
        '''### IMPORTANT ###'''
        ''' CHANGE location TO AN EQUIVALENT PATH ON YOUR MACHINE '''
        ''' (mysite/trades/static/trades/uploads should be the same) '''
        location = 'C:/Users/Callum/Documents/CS261/CS261_SE_Group2-master/mysite/trades/static/trades/uploads'
        file_path = os.path.join(location, file_name)
        with open(file_path, 'wb') as pdf:
            pisa.pisaDocument(BytesIO(html.encode("UTF-8")), pdf)
        r = Report(upload = file_path)
        r.save()
        return #[file_name, file_path]
