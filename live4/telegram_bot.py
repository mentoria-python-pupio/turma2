import requests
import argparse


def envia_msg_telegram(mensagem):
    TOKEN="6989768255:AAHRaVjAaD5aOKtq1hAULDZezUlNVbNbvtk"
    CHAT_ID = "-4169946750"

    TELEGRAM_URL = "https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}&parse_mode=HTML"

    response = requests.post(
        TELEGRAM_URL.format(
            token=TOKEN,
            chat_id=CHAT_ID,
            msg=mensagem
        )
    )

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description="Parsers dos argumentos passados no script"
    )

    parser.add_argument(
        "--mensagem", "-m", type=str, required=True, help="mensagem a ser enviada ao telegram"
    )
    
    # Força o uso dos argumentos definidos acima
    args = parser.parse_args()
    
    mensagem = args.mensagem

    envia_msg_telegram(mensagem)


