from paramiko import RSAKey
import base64
import os
from cryptography.hazmat.primitives import serialization

def pem_to_ppk():
    # Ask only for PEM file path
    pem_file = input("Enter path of your .pem file: ").strip()
    
    # Output .ppk in same folder with same name
    ppk_file = os.path.splitext(pem_file)[0] + ".ppk"
    comment = "aws-key"

    try:
        # Load RSA key from PEM
        rsa_key = RSAKey(filename=pem_file)

        # Prepare PPK content
        lines = []
        lines.append("PuTTY-User-Key-File-2: ssh-rsa")
        lines.append("Encryption: none")
        lines.append(f"Comment: {comment}")

        # Public key
        public_blob = rsa_key.asbytes()
        b64_pub = base64.encodebytes(public_blob).decode("utf-8").replace("\n", "")
        lines.append("Public-Lines: 1")
        lines.append(b64_pub)

        # Private key using proper Encoding
        private_blob = rsa_key.key.private_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        b64_priv = base64.encodebytes(private_blob).decode("utf-8")
        priv_lines = [b64_priv[i:i+64] for i in range(0, len(b64_priv), 64)]
        lines.append(f"Private-Lines: {len(priv_lines)}")
        lines.extend(priv_lines)

        lines.append("Private-MAC: 00000000000000000000000000000000")

        # Save as .ppk
        with open(ppk_file, "w") as f:
            f.write("\n".join(lines))

        print(f"\n✅ Successfully converted:\n{pem_file} → {ppk_file}")

    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    pem_to_ppk()
