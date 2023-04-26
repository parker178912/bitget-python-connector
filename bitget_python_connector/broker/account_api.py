from ..client import Client
from ..consts import *


class AccountApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    def info(self):
        '''
        get broker info
        :return:
        '''
        return self._request_without_params(GET, BROKER_ACCOUNT_V1_URL + '/info')

    def sub_create(self, subName, remark):
        '''
        broker create sub account
        :return:
        '''
        params = {}
        if subName:
            params["subName"] = subName
            params["remark"] = remark
            return self._request_with_params(POST, BROKER_ACCOUNT_V1_URL + '/sub-create', params)
        else:
            return "pls check args "

    def sub_list(self, pageSize, lastEndId, status):
        '''
        get sub info list
        :return:
        '''
        params = {}
        params["pageSize"] = pageSize
        params["lastEndId"] = lastEndId
        params["status"] = status
        return self._request_with_params(GET, BROKER_ACCOUNT_V1_URL + '/sub-list', params)
        return "pls check args"


    def sub_modify(self, subUid, perm, status):
        '''
        modify sub info list
        :return:
        '''
        params = {}
        if subUid and perm and status:
            params["subUid"] = subUid
            params["perm"] = perm
            params["status"] = status
            return self._request_with_params(POST, BROKER_ACCOUNT_V1_URL + '/sub-modify', params)
        else:
            return "pls check args "

    def sub_modify_email(self, subUid, subEmail):
        '''
        modify sub email
        :return:
        '''
        params = {}
        if subUid and subEmail:
            params["subUid"] = subUid
            params["subEmail"] = subEmail
            return self._request_with_params(POST, BROKER_ACCOUNT_V1_URL + '/sub-modify-email', params)
        else:
            return "pls check args "

    def sub_spot_assets(self, subUid):
        '''
        get sub spot assets
        :return:
        '''
        params = {}
        if subUid :
            params["subUid"] = subUid
            return self._request_with_params(GET, BROKER_ACCOUNT_V1_URL + '/sub-spot-assets', params)
        else:
            return "pls check args "

    def sub_future_assets(self, subUid):
        '''
        get sub future assets
        :return:
        '''
        params = {}
        if subUid:
            params["subUid"] = subUid
            return self._request_with_params(GET, BROKER_ACCOUNT_V1_URL + '/sub-future-assets', params)
        else:
            return "pls check args "

    def sub_address(self, subUid, subEmail):
        '''
        get sub deposit address
        :return:
        '''
        params = {}
        if subUid and subEmail:
            params["subUid"] = subUid
            params["subEmail"] = subEmail
            return self._request_with_params(POST, BROKER_ACCOUNT_V1_URL + '/sub-address', params)
        else:
            return "pls check args "

    def sub_withdrawal(self, subUid, coin, chain, address, amount, tag, clientOid):
        '''
        sub withdrawal
        :return:
        '''
        params = {}
        if subUid and coin and chain and address and amount:
            params["subUid"] = subUid
            params["coin"] = coin
            params["chain"] = chain
            params["address"] = address
            params["amount"] = amount
            params["tag"] = tag
            params["clientOid"] = clientOid
            return self._request_with_params(POST, BROKER_ACCOUNT_V1_URL + '/sub-withdrawal', params)
        else:
            return "pls check args "

    def sub_auto_transfer(self, subUid, coin, toAccountType):
        '''
        sub auto transfer 
        deposit success auto transfer future
        :return:
        '''
        params = {}
        if subUid and coin and toAccountType:
            params["subUid"] = subUid
            params["coin"] = coin
            params["toAccountType"] = toAccountType
            return self._request_with_params(POST, BROKER_ACCOUNT_V1_URL + '/sub-auto-transfer', params)
        else:
            return "pls check args "