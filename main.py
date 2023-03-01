"""ESTIMATE GAS WEB3PY"""
import time
from web3 import Web3
# Create a Web3 instance and connect to an Ethereum node
w3 = Web3(Web3.HTTPProvider('Node'))
from web3.middleware import geth_poa_middleware
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

amount = 0.009
sender = w3.toChecksumAddress('your address')
inputToken = w3.toChecksumAddress('token address')
wbnb_token = w3.toChecksumAddress('bnb token address') #testnet 0xae13d989dac2f0debff460ac112a837c89baa7cd
router = w3.eth.contract(address=routeraddress,abi=rouerabi)
input_contract = w3.eth.contract(address=inputToken, abi=inputToken_abi)
#Calculate minimum amount of tokens to receive
amountIn = (w3.toWei(amount, 'ether'))
receive = router.functions.getAmountsOut(amountIn, [wbnb_token, inputToken]).call()
minReceived = receive[1] * (9/10)                                        
receiveReadable = w3.fromWei(minReceived,'ether')
nonce = w3.eth.get_transaction_count()
gas_est = router.functions.swapExactETHForTokens(
        # set to 0, or specify minimum amount of token you want to receive - consider decimals!!!
        int(minReceived),
        [wbnb_token, inputToken],
        sender, #
        (int(time.time()) + 10000)
        ).estimate_gas({
        'from': sender,
        'value': amountIn,
        'gasPrice': w3.eth.gas_price,
        'nonce': nonce,
        })
gases = gas_est + 21000
total_gas = gases * w3.eth.gas_price
total_val = amountIn - total_gas
print("gases:", gases)
print("gasprime:", total_gas)
total_val = amountIn - total_gas
print("gas est:", gas_est)
print("total value:" ,total_val)
print(w3.fromWei(total_val, 'ether'))
