import uuid
import os
import qrcode


class Pix:
    def __init__(self):
        pass

    def create_payment_pix(self, base_dir=""):
        # Gerar um ID único para o pagamento
        bank_payment_id = str(uuid.uuid4())
        # Gera código QR para o pagamento
        hash_payment = f"hash_payment_{bank_payment_id}"
        # QR Code generation
        img = qrcode.make(hash_payment)
        # Salvar a imagem do QR Code
        os.makedirs(f"{base_dir}static/img", exist_ok=True)
        img.save(f"{base_dir}static/img/qr_code_payment_{bank_payment_id}.png")

        return {
            "bank_payment_id": bank_payment_id,
            "qr_code_path": f"qr_code_payment_{bank_payment_id}",
        }
