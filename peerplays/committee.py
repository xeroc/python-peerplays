from peerplays.instance import shared_peerplays_instance
from .account import Account
from .exceptions import CommitteeMemberDoesNotExistsException
from .blockchainobject import BlockchainObject


class Committee(BlockchainObject):
    """ Read data about a Committee Member in the chain

        :param str member: Name of the Committee Member
        :param peerplays peerplays_instance: PeerPlays() instance to use when accesing a RPC
        :param bool lazy: Use lazy loading

    """
    def __init__(
        self,
        member,
        peerplays_instance=None,
    ):
        super().__init__(
            member,
            peerplays_instance=peerplays_instance,
        )

    def refresh(self):
        account = Account(self.identifier)
        member = self.peerplays.rpc.get_committee_member_by_account(account["id"])
        if not member:
            raise CommitteeMemberDoesNotExistsException
        super(Committee, self).__init__(member)
        self.cached = True

    @property
    def account(self):
        return Account(self.identifier)
