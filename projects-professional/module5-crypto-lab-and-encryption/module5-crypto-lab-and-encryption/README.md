# Module 5 – Cryptographic Algorithms & Disk Encryption Tools

This module combined practical experimentation with encryption tools and real cryptographic analysis using CyberChef.

---

## 🔐 Part 1 – Cryptographic Algorithm Analysis (CyberChef)

**Objective:**  
Understand and compare symmetric, asymmetric, and hashing algorithms through hands-on use of CyberChef.

**Algorithms Used:**
- **AES (Symmetric):** Fast, secure, ideal for file and data encryption
- **RSA (Asymmetric):** Used for secure key exchange and digital signatures
- **SHA256 (Hashing):** One-way encryption for passwords and integrity verification

**What We Did:**
- Encrypted and decrypted plaintext using AES and RSA
- Generated SHA256 hash and analyzed its properties
- Compared algorithms on speed, key length, security, and use case
- Attempted to crack MD5 and SHA256 hashes using online tools
  - Example cracked MD5: "f!r5t"
  - SHA256: Too complex to break without brute-force resources

📄 Summary: AES is fast and efficient, RSA is ideal for key exchange, and SHA256 is secure but irreversible.

---

## 💽 Part 2 – Disk Encryption Tools (VeraCrypt + BitLocker)

**Objective:**  
Explore the real-world application of full-disk encryption tools in a safe virtual environment.

### 🔐 VeraCrypt (on Linux or Windows):
- Created a standard encrypted volume
- Used AES encryption with SHA-512 hashing
- Mounted encrypted volume using passphrase
- Verified successful creation and usage

### 🛡️ BitLocker (on Windows 10 VM):
- Enabled BitLocker on the virtual drive
- Used password-based unlock
- Saved recovery key offline
- Encrypted the entire drive in compatible mode

📄 Note: Both tools emphasize password strength and access control. BitLocker is faster to deploy but VeraCrypt offers more customization.

---

## 🧠 What I Learned

- How different encryption methods function and their practical applications
- That symmetric encryption is fast but needs shared key security
- That asymmetric encryption provides great key safety but is slower
- That hashing is irreversible and ideal for verifying integrity
- That disk encryption is essential for protecting offline data

This module gave me strong hands-on confidence using real-world cryptographic tools and testing basic password security theory.
