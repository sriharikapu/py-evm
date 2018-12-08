from rlp.sedes import (
    CountableList,
)
from eth.rlp.headers import (
    BlockHeader,
)
from eth.vm.forks.byzantium.blocks import (
    SpuriousDragonBlock,
)

from eth.vm.forks.byzantium.transactions import (
    ByzantiumTransaction,
)

from eth.vm.forks.stretch.xmessage import {
    StretchXMessage,
    StretchXMessageReceived
}

class StretchBlock(ByzantiumBlock):
    transaction_class = ByzantiumTransaction
    xmessage_sent_class = StretchXMessage
    xmessage_received_class = StretchXMessageReceived
    fields = [
        ('header', BlockHeader),
        ('transactions', CountableList(transaction_class)),
        ('xmessages_sent', CountableList(xmessage_sent_class)),
        ('xmessages_received', CountableList(xmessage_received_class)),
        ('uncles', CountableList(BlockHeader))
    ]
