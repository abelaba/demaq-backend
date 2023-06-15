from rest_framework.views import APIView
from rest_framework.response import Response
class TestBase64(APIView):
    def post(self,request,format=None):
        b65_str=request.data.get("data")
        import base64,os

        decodedData = base64.b64decode(b64_str)
        webmfile = (os.getcwd() + file.split('.')[0] + ".webm")
        with open(webmfile, 'wb') as file:
            file.write(decodedData)