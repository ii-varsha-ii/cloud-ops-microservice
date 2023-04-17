from concurrent import futures
from typing import List

import grpc

from services.organization import organization_pb2_grpc, organization_pb2
from services.organization.models import OrganizationModel, AccountModel
from services.organization.organization import get_organization, get_all_accounts_in_org, get_account_based_on_id, \
    create_account_in_org, invite_account_to_organization


def convertOrganizationModelToMessage(_organization: OrganizationModel) -> organization_pb2.Organization:
    return organization_pb2.Organization(
        id=_organization.Id,
        arn=_organization.Arn,
        master_account_arn=_organization.MasterAccountArn,
        master_account_id=_organization.MasterAccountId,
        master_account_email=_organization.MasterAccountEmail
    )


def convertAccountModelToMessage(_account: AccountModel) -> organization_pb2.Account:
    print(_account)
    return organization_pb2.Account(
        id=_account.Id,
        arn=_account.Arn,
        email=_account.Email,
        name=_account.Name,
        status=_account.Status,
        joined_method=_account.JoinedMethod,
        joined_timestamp=str(_account.JoinedTimestamp)
    )


class OrganizationService(organization_pb2_grpc.OrganizationServiceServicer):
    def GetOrganization(self, request, context):
        try:
            organization: OrganizationModel = get_organization()
            if organization:
                return convertOrganizationModelToMessage(organization)
            else:
                return organization_pb2.Organization()
        except Exception as e:
            context.set_code(grpc.StatusCode.ABORTED)
            context.set_details(str(e))
            return None

    def GetAccountsInOrganization(self, request, context):
        try:
            accounts = get_all_accounts_in_org()
            list_of_accounts = organization_pb2.ListOfAccounts()
            if accounts:
                for account in accounts:
                    list_of_accounts.accounts.append(convertAccountModelToMessage(account))
                return list_of_accounts
            else:
                return None
        except Exception as e:
            context.set_code(grpc.StatusCode.ABORTED)
            context.set_details(str(e))
            return None

    def GetAccountInOrganizationBasedOnId(self, request, context):
        try:
            account = get_account_based_on_id(request.account_id)
            if account:
                return convertAccountModelToMessage(account)
            else:
                return None
        except Exception as e:
            context.set_code(grpc.StatusCode.ABORTED)
            context.set_details(str(e))
            return None

    def InviteAccountToOrganization(self, request, context):
        response = invite_account_to_organization(request.account_id, request.email_id)
        if response:
            return organization_pb2.InviteAccountResponse(
                id=response.Id,
                arn=response.Arn,
                action=response.Action,
                requested_timestamp=str(response.RequestedTimestamp),
                expiration_timestamp=str(response.ExpirationTimestamp),
                parties=response.Parties,
                state=response.State
            )
        else:
            return None


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    organization_pb2_grpc.add_OrganizationServiceServicer_to_server(
        OrganizationService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server started at port 50051")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
