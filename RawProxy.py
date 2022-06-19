# Bitcoin Node muss gestartet sein

#from bitcoin.rpc import RawProxy
from bitcoin.rpc.authproxy import AuthServiceProxy

#Connection to local Bitcoin Core
p = RawProxy()

#GetBlockChainInfo ausführen
info = p.getblockchaininfo()

#Block Element aus dem Ergebnis JSON rausholen
print(info['blocks'])