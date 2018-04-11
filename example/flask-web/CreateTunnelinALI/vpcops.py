# -*- coding: utf-8 -*-


from aliyunsdkcore import client
from aliyunsdkvpc.request.v20160428 import DescribeRouterInterfacesRequest
from aliyunsdkvpc.request.v20160428 import CreateRouterInterfaceRequest
from aliyunsdkvpc.request.v20160428  import ModifyRouterInterfaceAttributeRequest
import json

# ziji
#clt = client.AcsClient('XXXXX', 'XXXXX', 'cn-hangzhou')

def query(akid,secret,region,query_region):
    try:
        clt = client.AcsClient(akid, secret, region)
        request = DescribeRouterInterfacesRequest.DescribeRouterInterfacesRequest()
        request.set_accept_format('json')
        request.add_query_param('RegionId', query_region)
        response = clt.do_action_with_exception(request)
        response_dic = json.loads(response)
        #return response_dic['RouterInterfaceSet']['RouterInterfaceType'][0]['RouterId']
        return response_dic
    except Exception, e:
        return {'error':e}

def createaccept(dict):
    clt = client.AcsClient(dict['akid'], dict['secret'], dict['region'])
    request = CreateRouterInterfaceRequest.CreateRouterInterfaceRequest()
    request.set_accept_format('json')
    request.add_query_param('RegionId', dict['queryed_region'])
    request.add_query_param('Role', dict['role'])
    request.add_query_param('OppositeRegionId', dict['OppositeRegionId'])
    request.add_query_param('RouterType', dict['router_type'])
    request.add_query_param('Spec', dict['spec'])
    request.add_query_param('RouterId', dict['routerid'])
    # 发起请求
    response_str = clt.do_action_with_exception(request)
    response_dict = json.loads(response_str)
    print(response_dict)
    return response_dict['RouterInterfaceId']


def createainit(dict):
    clt = client.AcsClient(dict['akid'], dict['secret'], dict['region'])
    request = CreateRouterInterfaceRequest.CreateRouterInterfaceRequest()
    request.set_accept_format('json')
    request.add_query_param('RegionId',  dict['queryed_region'])
    request.add_query_param('Role', dict['role'])
    request.add_query_param('OppositeRegionId', dict['OppositeRegionId'])

    # 接收端的路由
    request.add_query_param('OppositeRouterId',  dict['OppositeRouterId'])

    # 接收端的接口
    request.add_query_param('OppositeInterfaceId', dict['OppositeInterfaceId'])

    request.add_query_param('OppositeInterfaceOwnerId',dict['OppositeInterfaceOwnerId'])
    request.add_query_param('RouterType', dict['router_type'])
    request.add_query_param('Spec', dict['spec'])
    request.add_query_param('RouterId',  dict['routerid'])

    # 发起请求
    response_str = clt.do_action_with_exception(request)
    response_dict = json.loads(response_str)
    print(response_dict)
    return response_dict['RouterInterfaceId']

def updateaccept(dict):
    clt = client.AcsClient(dict['akid'], dict['secret'], dict['region'])
    request = ModifyRouterInterfaceAttributeRequest.ModifyRouterInterfaceAttributeRequest()
    request.set_accept_format('json')

    request.add_query_param('RegionId', dict['queryed_region'])
    request.add_query_param('RouterInterfaceId', dict['RouterInterfaceId'])
    request.add_query_param('OppositeInterfaceId', dict['OppositeInterfaceId'])
    request.add_query_param('OppositeRouterId', dict['OppositeRouterId'])
    request.set_OppositeInterfaceOwnerId(dict['OppositeInterfaceOwnerId'])
    request.add_query_param('OppositeRouterType', dict['OppositeRouterTypeId'])
    request.add_query_param('Description', dict['Description'])

    response_str = clt.do_action_with_exception(request)
    response_dict = json.loads(response_str)
    print(response_dict)
    return response_dict


