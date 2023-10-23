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

img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()

#Open gRPC channel
channel = grpc.insecure_channel(addr)

#Rondom vector generation
def generate_random_vector(length):
    return [random.random() for _ in range(length)]

#Image service
if(endpoint == 'rawImage'):
    stub = lab6_pb2_grpc.imageStub(channel)
    count = 1
    start = perf_counter()

    while(count <= n):
        number = lab6_pb2.rawImageMsg(img=img)
        response = stub.image(number)
        print("response:", response)
        count += 1

    total_time = perf_counter() - start
    print(str(total_time/n * 1000) + ' ms')

#JsonImage service
elif(endpoint == 'jsonImage'):
    stub = lab6_pb2_grpc.jsonImageStub(channel)
    count = 1
    start = perf_counter()

    while(count <= n):
        with open('Flatirons_Winter_Sunrise_edit_2.jpg' , "rb") as image_file:
            image_binary = image_file.read()
        base64_encoded = base64.b64encode(image_binary).decode()
        number = lab6_pb2.jsonImageMsg(img=base64_encoded)
        #print("inside client", number)
        response = stub.jsonImage(number)
        print("response", response)
        count += 1

    total_time = perf_counter() - start
    print(str(total_time/n * 1000) + ' ms')

#Add service
elif(endpoint == 'add'):
    stub = lab6_pb2_grpc.addStub(channel)
    count = 1
    start = perf_counter()

    while(count <= n):
        number = lab6_pb2.addMsg(a=random.randint(1, 100), b=random.randint(1, 100))
        response = stub.add(number)
        print(response.a)
        count += 1

    total_time = perf_counter() - start
    print(str(total_time/n * 1000) + ' ms')

#DotProduct service
elif(endpoint == 'dotProduct'):
    stub = lab6_pb2_grpc.dotProductStub(channel)
    count = 1
    start = perf_counter()

    while(count <= n):
        #print("inside while. count: ", count)
        number = lab6_pb2.dotProductMsg(a=generate_random_vector(100), b=generate_random_vector(100))
        response = stub.dotProduct(number)
        print(response.a)
        count += 1

    total_time = perf_counter() - start
    print(str(total_time/n * 1000) + ' ms')