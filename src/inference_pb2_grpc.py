# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import inference_pb2 as inference__pb2


class ServerStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Partial = channel.unary_unary(
                '/Server/Partial',
                request_serializer=inference__pb2.Tensor.SerializeToString,
                response_deserializer=inference__pb2.Result.FromString,
                )


class ServerServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Partial(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Partial': grpc.unary_unary_rpc_method_handler(
                    servicer.Partial,
                    request_deserializer=inference__pb2.Tensor.FromString,
                    response_serializer=inference__pb2.Result.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Server', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Server(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Partial(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server/Partial',
            inference__pb2.Tensor.SerializeToString,
            inference__pb2.Result.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
