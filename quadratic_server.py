# Becky Kozura, Module 02, Project 01, Quadratic Equation Demo

from concurrent import futures
import logging

import grpc
import quadratic_pb2
import quadratic_pb2_grpc


class QuadraticSolver(quadratic_pb2_grpc.QuadraticSolverServicer):
    '''
    gRPC code to run server side of Quadratic Solver
    '''
    def SolveQuadratic(self, request, context):
        '''
        Function to solve the quadratic equation and return the solution to the client
        '''
        def quadratic(a, b, c):   
            '''
            Method to calculate the solution to the quadratic equation
                x = (-b +- (b^2 -4ac)^.5) / 2a
            Takes three Real numbers and returns two values of x in string form
            '''  
            negative_x = (-b - (b**2 - 4*a*c)**.5) / 2*a
            positive_x = (-b + (b**2 - 4*a*c)**.5) / 2*a
            return f"{negative_x} and {positive_x}"
        
        answer = quadratic(request.coeffa, request.coeffb, request.coeffc)
        return quadratic_pb2.QuadraticReply(solution=f"The two values of x are {answer}")

def serve():
    '''
    Function to open a port and start and run the server
    ''' 
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    quadratic_pb2_grpc.add_QuadraticSolverServicer_to_server(QuadraticSolver(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

'''
Driver code for Quadratic Solver Server
'''
if __name__ == "__main__":
    logging.basicConfig()
    serve()