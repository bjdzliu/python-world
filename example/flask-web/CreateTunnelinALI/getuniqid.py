# -*- coding: utf-8 -*-
dict={
	'TotalCount': 2, 'RouterInterfaceSet': {
		'RouterInterfaceType': [{
			'Status': 'Idle',
			'OppositeRegionId': 'cn-beijing',
			'BusinessStatus': 'Normal',
			'EndTime': '2999-09-08T16:00:00Z',
			'OppositeInterfaceSpec': 'Negative',
			'VpcInstanceId': 'vpc-2zeenjp66666666ct3j135',
			'RouterInterfaceId': 'ri-2zea66666666ulx7ssh84',
			'CreationTime': '2018-02-06T08:33:00Z',
			'RouterType': 'VRouter',
			'OppositeInterfaceOwnerId': '',
			'RouterId': 'vrt-2zenp80666666du0z39e',
			'Role': 'InitiatingSide',
			'ChargeType': 'AfterPay',
			'OppositeInterfaceBusinessStatus': 'Normal',
			'Spec': 'Large.2',
			'OppositeRouterType': 'VRouter'
		}, {
			'Status': 'Idle',
			'OppositeRegionId': 'cn-beijing',
			'BusinessStatus': 'Normal',
			'OppositeRouterId': 'vrt-2zenp66lutkhphdu0z39e',
			'VpcInstanceId': 'vpc-2zee6666paz2ct3j135',
			'Description': 'ecitic',
			'RouterInterfaceId': 'ri-2zej1t66666666y9zdkbb',
			'CreationTime': '2018-02-05T10:34:11Z',
			'RouterType': 'VRouter',
			'OppositeInterfaceOwnerId': '178036666662858',
			'RouterId': 'vrt-2zenp80lutkhphdu0z39e',
			'OppositeInterfaceId': 'ri-2zea066666666ssh84',
			'ChargeType': 'AfterPay',
			'OppositeVpcInstanceId': 'vpc-2zeenj666666663j135',
			'EndTime': '2999-09-08T16:00:00Z',
			'Role': 'AcceptingSide',
			'OppositeInterfaceBusinessStatus': 'Normal',
			'Spec': 'Negative',
			'OppositeRouterType': 'VRouter'
		}]
	}, 'PageNumber': 1, 'RequestId': '0EE7EA2B-9F6A-40D1-809B-74FF87108F24', 'PageSize': 10
}

def getuniqid(dict):
    #找到有几个router
    for k,v in dict.items():
        if k == 'RouterInterfaceSet' :
            router_type_list = v['RouterInterfaceType']
            routerid_list=[]
            #取每个个RouterId放进list中，去重后，得到一个
            for i in range(len(router_type_list)):
                routerid_list.append(router_type_list[i]['RouterId'])
    return list(set(routerid_list))




