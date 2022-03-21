# PQ-crypto-test-app
School project orientated around post-quantum cryptography.

# Features (using various PQ algorithms from pqcrypto library)
- key generation
- PK encryption + decryption
- digital signing + verification
- performance statistics and algorithm comparison
- generated keypairs can be stored and re-used from file encrypted with AES-GCM using a master password

# Usage
- run `gui/main.py` with python interpreter

# HOW TO BUILD PQCRYPTO DIRECTLY
1) unpack ".tar.gz" file into the repozitory folder (default name of folder: "pqcrypto-0.1.3")
2) go to terminal, cd into the "pqcrypto-0.1.3" folder and run script:

python setup.py install --prefix=<path-to-python-files>

- <path-to-python-files> should be folder where "lib" (with "pythonX.X"->"site-packages") is located for your python
- for me, it was virtual environment folder right in this repository folder
- script "setup.py" looks into this <path-to-python-files>, goes to lib->pythonX.X->site-packages and installs pqcrypto there + builds files inside "pqcrypto-0.1.3" folder
