import unittest

import boto3

from services.organization.grpc_handler import serve
from services.organization.models import OrganizationModel, Account
from services.organization.organization import get_organization, get_all_accounts_in_org, get_account_based_on_id


class TestOrganization(unittest.TestCase):
    def setUp(self) -> None:
        client = boto3.client('organizations')

    def test_get_organization(self):
        res = get_organization()
        self.assertEqual(isinstance(res, OrganizationModel), True)
        self.assertIsNotNone(res)

    def test_get_accounts(self):
        res = get_all_accounts_in_org()
        self.assertIsNotNone(res)

    def test_get_account_based_on_id(self):
        account_id = "207356624860"
        res = get_account_based_on_id(account_id)
        self.assertIsNotNone(res)

    def test_serve(self):
        serve()
