import boto.cloudformation

from .resource import Resource, json_encoder


class Stacks(object):

    @staticmethod
    def new_stack(name, template, connection):
        return connection.create_stack(name, template_body=template)

    @staticmethod
    def list(connection):
        return [Stack(stack.stack_name, **stack.__dict__)
                for stack in connection.list_stacks()
                if stack.stack_status != "DELETE_COMPLETE"]

    @staticmethod
    def delete(stack_id, connection):
        connection.delete_stack(stack_id)

    @staticmethod
    def stack(stack_id, connection):
        return filter(lambda x: x["stack_id"] == stack_id,
                      Stacks.list(connection))[0]


def Connection(aws_access_key_id, aws_secret_access_key):
    return boto.cloudformation.connection.\
        CloudFormationConnection(aws_access_key_id=aws_access_key_id,
                                 aws_secret_access_key=aws_secret_access_key)


def Stack(name, **properties):
    return Resource(name, **properties)
