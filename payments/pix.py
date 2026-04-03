import uuid
import qrcode


class Pix:
    def __init__(self):
        pass

    def create_payment_pix(self):
        # Gerar um ID único para o pagamento
        bank_payment_id = uuid.uuid4()
        # Gera código QR para o pagamento
        hash_payment = f"hash_payment_{bank_payment_id}"
        # QR Code generation
        img = qrcode.make(hash_payment)
        # Salvar a imagem do QR Code
        img.save(f"static/img/qr_code_payment_{bank_payment_id}.png")

        return {
            "bank_payment_id": bank_payment_id,
            "qr_code_path": f"qr_code_payment_{bank_payment_id}",
        }
