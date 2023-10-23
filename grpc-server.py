import grpc
import lab6_pb2
import lab6_pb2_grpc
from concurrent import futures
import io
from PIL import Image
import base64

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)


class addServicer(lab6_pb2_grpc.addServicer):
    def add(self, request, context):
        response = lab6_pb2.addMsg()
        response.a = request.a + request.b
        return response

class dotProductServicer(lab6_pb2_grpc.dotProductServicer):
    def dotProduct(self, request, context):
        result = 0
        vector1 = request.a
        vector2 = request.b
        for i in range(len(vector1)):
            result += vector1[i] * vector2[i]
        response = lab6_pb2.dotProductReply()
        response.dotproduct = result
        return response

class imageServicer(lab6_pb2_grpc.imageServicer):
    def image(self, request, context):
        r = request
        ioBuffer = io.BytesIO(r.img)
        req_img = Image.open(ioBuffer)
        result = {
            'width': req_img.size[0],
            'height': req_img.size[1]
        }
        print("result", result['width'])
        response = lab6_pb2.imageReply()
        response.width = result['width']
        response.height = result['height']
        print("response", response)
        return response
    
class jsonImageServicer(lab6_pb2_grpc.jsonImageServicer):
    def jsonImage(self, request, context):
        r = request
        image_data = base64.b64decode(r.img)
        ioBuffer = io.BytesIO(image_data)
        img = Image.open(ioBuffer)
        result = {
            'width' : img.size[0],
            'height' : img.size[1]
            }
        response = lab6_pb2.imageReply()
        response.width = result['width']
        response.height = result['height']
        print("response", response)
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

lab6_pb2_grpc.add_addServicer_to_server(addServicer(), server)
lab6_pb2_grpc.add_dotProductServicer_to_server(dotProductServicer(), server)
lab6_pb2_grpc.add_imageServicer_to_server(imageServicer(), server)
lab6_pb2_grpc.add_jsonImageServicer_to_server(jsonImageServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()
