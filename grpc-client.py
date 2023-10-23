import grpc
import sys
import lab6_pb2
import lab6_pb2_grpc
from time import perf_counter
import random
import base64

if len(sys.argv) != 4:
    print("\npython grpc-client.py <server address> <endpoint> <iterations>")
    exit()

addr = sys.argv[1] + ':50051'

endpoint = sys.argv[2]
num_iterations = sys.argv[3]
n = int(num_iterations)

#Open gRPC channel
channel = grpc.insecure_channel(addr)

#Random vector generation
def generate_random_vector(length):
    return [random.random() for _ in range(length)]

def doAdd():
    stub = lab6_pb2_grpc.addStub(channel)
    number = lab6_pb2.addMsg(a=random.randint(1, 100), b=random.randint(1, 100))
    response = stub.add(number)

def doDotProduct():
    stub = lab6_pb2_grpc.dotProductStub(channel)
    number = lab6_pb2.dotProductMsg(a=generate_random_vector(100), b=generate_random_vector(100))
    response = stub.dotProduct(number)

def doRawImage():
    stub = lab6_pb2_grpc.imageStub(channel)
    img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    number = lab6_pb2.rawImageMsg(img=img)
    response = stub.image(number)

def doJsonImage():
    stub = lab6_pb2_grpc.jsonImageStub(channel)
    with open('Flatirons_Winter_Sunrise_edit_2.jpg' , "rb") as image_file:
        image_binary = image_file.read()
    base64_encoded = base64.b64encode(image_binary).decode()
    number = lab6_pb2.jsonImageMsg(img=base64_encoded)
    response = stub.jsonImage(number)

if(endpoint == 'add') :
    start = perf_counter()
    count=1
    while(count <=n ):
        doAdd()
        count += 1
    total_time = perf_counter() - start
    print("Took", str(total_time/n * 1000), "ms per operation")

elif(endpoint == 'dotProduct') :
    start = perf_counter()
    count=1
    while(count <=n ):
        doDotProduct()
        count += 1
    total_time = perf_counter() - start
    print("Took", str(total_time/n * 1000), "ms per operation")

elif(endpoint == 'rawImage') :
    start = perf_counter()
    count=1
    while(count <=n ):
        doRawImage()
        count += 1
    total_time = perf_counter() - start
    print("Took", str(total_time/n * 1000), "ms per operation")

elif(endpoint == 'jsonImage') :
    start = perf_counter()
    count=1
    while(count <=n ):
        doJsonImage()
        count += 1
    total_time = perf_counter() - start
    print("Took", str(total_time/n * 1000), "ms per operation")

else:
    print("Unknown option", endpoint)