import logging
from typing import List, Optional

import boto3
from botocore.exceptions import ClientError
from pydantic import parse_obj_as

from services.organization.models import OrganizationModel, AccountModel, InviteAccountResponseModel

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

client = boto3.client('organizations')


def get_organization() -> Optional[OrganizationModel]:
    try:
        response = client.describe_organization()
        if response:
            plain_org = response['Organization']
            org_response: OrganizationModel = OrganizationModel(**plain_org)
            logging.info(f"Response: {org_response}")
            return org_response
        else:
            return None
    except Exception as e:
        logging.error(f"func get_organization failed with error: {e}")
        raise Exception(f"func get_organization failed with error: {e}")


def get_all_accounts_in_org() -> Optional[List[AccountModel]]:
    try:
        response = client.list_accounts()
        if response:
            plain_list_accounts = response['Accounts']
            acc_response: List[AccountModel] = parse_obj_as(List[AccountModel], plain_list_accounts)
            logging.info(f"Response: {acc_response}")
            return acc_response
        else:
            return None
    except Exception as e:
        logging.error(f"func get_all_accounts_in_org failed with error:  {e}")
        raise Exception(f"func get_all_accounts_in_org failed with error: {e}")


def get_account_based_on_id(account_id: str):
    try:
        logging.info(f"Response: {account_id}")
        response = client.describe_account(AccountId=account_id)
        if response:
            plain_account = response['Account']
            acc_response: AccountModel = AccountModel(**plain_account)
            logging.info(f"Response: {acc_response}")
            return acc_response
        else:
            logging.info(f"Account {account_id} does not exist")
            return []
    except Exception as e:
        logging.error("func get_account_based_on_id failed with error: ", e)
        raise Exception(f"func get_all_accounts_in_org failed with error: {e}")


def create_account_in_org(email_id: str, account_name: str, role_name: Optional[str], iam_user_access_to_billing: str):
    try:
        if role_name:
            response = client.create_account(Email=email_id,
                                             AccountName=account_name,
                                             RoleName=role_name,
                                             IamUserAccessToBilling=iam_user_access_to_billing)
        else:
            response = client.create_account(Email=email_id,
                                             AccountName=account_name,
                                             IamUserAccessToBilling=iam_user_access_to_billing)
        if response:
            print(response)
            plain_account_status = response['CreateAccountStatus']
            acc_response: CreateAccountResponseModel = CreateAccountResponseModel(**plain_account_status)
            if acc_response.FailureReason:
                logging.info(f"Account {acc_response} creation failed with reason: {acc_response.FailureReason}")
            else:
                logging.info(f"Response: {acc_response}")
            return acc_response
        else:
            logging.info(f"Account creation failed")
            return []
    except Exception as e:
        logging.error("func create_account_in_org failed with error: ", e)


def invite_account_to_organization(account_id: Optional[str], email_id: Optional[str]):
    try:
        if email_id:
            response = client.invite_account_to_organization(Target={'Id': email_id, 'Type': 'EMAIL'})
        else:
            response = client.invite_account_to_organization(Target={'Id': account_id, 'Type': 'ACCOUNT'})
        if response:
            handshake_response = response['Handshake']
            acc_response: InviteAccountResponseModel = InviteAccountResponseModel(**handshake_response)
            logging.info(f"Response: {acc_response}")
            return acc_response
        else:
            logging.info(f"Account {account_id} does not exist")
            return []
    except Exception as e:
        logging.error("func invite_account_to_organization failed with error: ", e)
        return e
