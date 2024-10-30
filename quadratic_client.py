'''
Becky Kozura, Module 02, Project 1, gRPC Quadratic Equation Demo
'''

from __future__ import print_function

import logging

import grpc
import quadratic_pb2
import quadratic_pb2_grpc

'''
Code to run the client side of the Quadratic Solver
'''
def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to solve the quadratic equation...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = quadratic_pb2_grpc.QuadraticSolverStub(channel)
        # coeffa_in = float(input("Enter coefficient a: "))     # Use this to have user input values
        # coeffb_in = float(input("Enter coefficient b: "))
        # coeffc_in = float(input("Enter coefficient b: "))
        coeffa_in, coeffb_in, coeffc_in = 1, -2, -15        # Use this for hard coded values
        response = stub.SolveQuadratic(quadratic_pb2.QuadraticRequest(coeffa=coeffa_in, coeffb=coeffb_in, coeffc=coeffc_in))
    print("Quadratic solver client received: " + response.solution) # prints response solution as a string

'''
Driver code
'''
if __name__ == "__main__":
    logging.basicConfig()
    run()
