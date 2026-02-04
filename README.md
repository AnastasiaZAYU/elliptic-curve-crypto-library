# Elliptic Curve Cryptography Library

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: Python](https://img.shields.io/badge/Language-Python-3776AB.svg)](https://www.python.org/)

A modular Python implementation of Elliptic Curve Cryptography (ECC) from scratch. This library provides low-level arithmetic operations on elliptic curves and high-level cryptographic protocols, specifically tested on the **NIST P-224** curve.

## 📐 Mathematical Basis

The library implements elliptic curves over a finite field $F_p$ defined by the short Weierstrass equation:

$$y^2 \equiv x^3 + ax + b \pmod{p}$$

For the **NIST P-224** curve, the parameters $a$ and $b$ are specifically chosen to ensure security and efficiency, with the field prime $p = 2^{224} - 2^{96} + 1$.

## 🚀 Features

### Core Arithmetic (`src/`)
* **Point Operations**: Implementation of Point Addition, Point Doubling, and Scalar Multiplication.
* **Coordinate Systems**: Support for both **Affine** and **Projective** (Jacobian-like) coordinates for efficiency.
* **Validation**: Methods to verify if a point belongs to a specific curve.

### Cryptographic Protocols (`notebooks/`)
* **ECDH (Elliptic Curve Diffie-Hellman)**: Secure key exchange and shared secret agreement.
* **ECDSA (Elliptic Curve Digital Signature Algorithm)**: Message signing and verification using SHA-3 256.
* **Hybrid Encryption**: Directed encryption scheme using ephemeral ECDH keys and AES-CBC for message confidentiality.

## 📂 Project Structure

```text
elliptic-curve-crypto-library/
├── notebooks/              # Interactive demos and labs
│   ├── 01_arithmetic_demo.ipynb
│   └── 02_crypto_protocols.ipynb
├── src/                    # Core library (Python package)
│   ├── __init__.py         # Package initialization
│   ├── elliptic_curve.py   # EllipticCurve class logic
│   └── curve_point.py      # CurvePoint arithmetic logic
├── .gitignore
├──  README.md
└── requirements.txt        # Project dependencies
```

## 📓 Quick Start (Google Colab)

The easiest way to explore this library is through interactive notebooks. They are configured to automatically set up the environment and clone the library directly in the cloud.

1. Open a notebook:
   * [01_arithmetic_demo.ipynb](https://colab.research.google.com/github/AnastasiaZAYU/elliptic-curve-crypto-library/blob/main/notebooks/01_arithmetic_demo.ipynb) — Explore P-224 curve operations.
   * [02_crypto_protocols.ipynb](https://colab.research.google.com/github/AnastasiaZAYU/elliptic-curve-crypto-library/blob/main/notebooks/02_crypto_protocols.ipynb) — Test ECDH, ECDSA, and Hybrid Encryption.
2. Click the **"Open in Colab"** button at the top.
3. Run all cells (`Ctrl + F9`). Everything will work out-of-the-box!

## 🛠 Local Setup

If you prefer to run the project on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AnastasiaZAYU/elliptic-curve-crypto-library.git
   cd elliptic-curve-crypto-library
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Usage Example**:

   ```python
   from src import EllipticCurve, CurvePoint

   # NIST P-224 Example
   p = "0xffffffffffffffffffffffffffffffff000000000000000000000001"
   a = "0xfffffffffffffffffffffffffffffffefffffffffffffffffffffffe"
   b = "0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4"

   curve = EllipticCurve(p, a, b)
   G = CurvePoint(curve, "0xb70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21", 
                      "0xbd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34", "0x1")
   ```

## 📜 Requirements
* Python 3.x
* `pycryptodome` (used for AES and SHA-3 in high-level protocols)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👩‍💻 Author
**Anastasiia Zatsarenko**  
Institute of Physics and Technology (IPT), Igor Sikorsky KPI, 2024
