# pythales


A primitive implementation of [Thales HSM](https://en.wikipedia.org/wiki/Hardware_security_module) hardware security module) simulator.

## Features

- Concurrent message processing using threads (asynchronous)
- Dynamic (non-hardcoded) message header support
- Automatic client reconnection handling
- Graceful shutdown on Ctrl+C

Only the basic (the most popular) HSM commands are implemented:

- A0 - Generate a Key
- BU - Generate a Key check value 
- CA - Translate PIN from TPK to ZPK 
- CY - Verify CVV/CSC
- DC - Verify PIN
- EC - Verify an Interchange PIN using ABA PVV method
- FA - Translate a ZPK from ZMK to LMK
- HC - Generate a TMK, TPK or PVK
- NC - Diagnostics information
- CW - Generate a Card Verification Code

## Installation

Install git and python3:
```bash
apt-get install git python3 python3-pip
```

Setup virtual environment for python3 (check the [Manual](https://virtualenvwrapper.readthedocs.io/en/latest/)):
```bash
mkvirtualenv pyenv -p /usr/bin/python3
workon pyenv
```

Check out the code and install requirements:
```bash
git clone https://github.com/timgabets/pythales
cd pythales
workon pyenv
pip3 install -r requirements.txt
```
 
Run:
```bash
cd examples/
./hsm_server.py --help # check the options
./hsm_server.py
```

Output example:
```
./examples/hsm_server.py
Listening on port 1500
LMK: DEAFBEEDEAFBEEDEAFBEEDEAFBEEDEAF
Firmware version: 0007-E000

Connected client: 127.0.0.1:57216
22:33:50.207815 << 107 bytes received from 127.0.0.1:57216:
	00 69 95 13 b7 9c 45 43 43 34 45 44 35 39 37 45         .i....ECC4ED597E
	45 30 43 39 36 39 37 31 30 34 45 44 33 39 39 42         E0C9697104ED399B
	45 36 46 38 42 38 37 32 37 33 33 36 44 35 30 43         E6F8B8727336D50C
	34 37 31 32 38 44 37 31 30 44 46 34 35 30 42 43         47128D710DF450BC
	42 32 43 36 34 36 31 42 37 39 33 41 45 36 32 44         B2C6461B793AE62D
	46 43 38 44 32 34 32 36 30 31 34 30 37 30 30 30         FC8D242601407000
	30 30 30 30 31 30 31 33 38 34 33                        00001013843

[ThreadPoolExecutor-0_0] Handling message from 127.0.0.1:57216
Connected client: 127.0.0.1:57217
	[Command Description  ]: [Verify an Interchange PIN using ABA PVV method]
	[ZPK                  ]: [C4ED597EE0C9697104ED399BE6F8B872]
	[PVK Pair             ]: [7336D50C47128D710DF450BCB2C6461B]
	[PIN block            ]: [793AE62DFC8D2426]
	[PIN block format code]: [01]
	[Account Number       ]: [407000000010]
	[PVKI                 ]: [1]
	[PVV                  ]: [3843]

22:33:50.208512 << 107 bytes received from 127.0.0.1:57217:
	00 69 67 11 e9 f3 45 43 43 34 45 44 35 39 37 45         .ig...ECC4ED597E
	45 30 43 39 36 39 37 31 30 34 45 44 33 39 39 42         E0C9697104ED399B
	45 36 46 38 42 38 37 32 37 33 33 36 44 35 30 43         E6F8B8727336D50C
	34 37 31 32 38 44 37 31 30 44 46 34 35 30 42 43         47128D710DF450BC
	42 32 43 36 34 36 31 42 37 39 33 41 45 36 32 44         B2C6461B793AE62D
	46 43 38 44 32 34 32 36 30 31 34 30 37 30 30 30         FC8D242601407000
	30 30 30 30 31 30 31 33 38 34 33                        00001013843

[ThreadPoolExecutor-0_1] Handling message from 127.0.0.1:57217
	[Command Description  ]: [Verify an Interchange PIN using ABA PVV method]
	[ZPK                  ]: [C4ED597EE0C9697104ED399BE6F8B872]
	[PVK Pair             ]: [7336D50C47128D710DF450BCB2C6461B]
	[PIN block            ]: [793AE62DFC8D2426]
	[PIN block format code]: [01]
	[Account Number       ]: [407000000010]
	[PVKI                 ]: [1]
	[PVV                  ]: [3843]

22:33:50.209452 >> [ThreadPoolExecutor-0_0] 10 bytes sent to 127.0.0.1:57216:
	00 08 95 13 b7 9c 45 44 30 30                           ......ED00

[ThreadPoolExecutor-0_0] Active threads: 5
	[Response Code]: [ED]
	[Error Code   ]: [00]

22:33:50.209650 >> [ThreadPoolExecutor-0_1] 10 bytes sent to 127.0.0.1:57217:
	00 08 67 11 e9 f3 45 44 30 30                           ..g...ED00

[ThreadPoolExecutor-0_1] Active threads: 5
	[Response Code]: [ED]
	[Error Code   ]: [00]
```

## Performance

Basic performance test results using `wrk` on a local machine:

```
Thread Stats   Avg      Stdev     Max   +/- Stdev
  Latency     3.37ms    3.45ms  30.47ms   87.43%
  Req/Sec   392.89     87.72   616.00     67.20%
Latency Distribution
   50%    2.06ms
   75%    2.75ms
   90%    8.51ms
   99%   16.61ms
14799 requests in 10.01s, 0.90MB read
Requests/sec:   1477.71
Transfer/sec:     92.36KB
```

You may also check [examples](https://github.com/timgabets/pythales/tree/master/examples) for more sophisticated HSM server implementation with some features like command line options parsing etc. The application works as server that may simultaneously serve only one connected client.