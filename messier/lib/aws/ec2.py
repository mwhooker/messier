import boto.ec2

from .resource import Resource, json_encoder


class Instances(object):

    @staticmethod
    def list(cxn):
        return [Instance(inst.tags.get("Name", None), **inst.__dict__)
                for inst in cxn.get_only_instances()]

    @staticmethod
    def instance(cxn, inst_id):
        return filter(lambda x: x["id"] == inst_id,
                      Instances.list(cxn))[0]


Connection = boto.ec2.EC2Connection


def Instance(name, **properties):
    def encoder(obj):
        if isinstance(obj, boto.ec2.blockdevicemapping.BlockDeviceType):
            d = obj.__dict__
            del d["connection"]

            return d
        elif isinstance(obj, boto.ec2.group.Group):
            return obj.__dict__
        elif isinstance(obj, boto.ec2.instance.InstancePlacement):
            return obj.__dict__
        elif isinstance(obj, boto.ec2.instance.InstanceState):
            return obj.name

            return json_encoder(obj)

    return Resource(name, "Instance", encoder=encoder, **properties)
