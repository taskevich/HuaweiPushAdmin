import json
import hpa

from hpa import messaging
from vars import app_id, app_secret, test_device_token


"""
[ANDROID] android
"""
android = messaging.AndroidConfig(
    collapse_key=-1,
    urgency=messaging.AndroidConfig.HIGH_PRIORITY,
    ttl="10000s",
    bi_tag='the_sample_bi_tag_for_receipt_service'
)


def send_push_android_data_message():
    """
    a sample to show hwo to send web push message
    :return:
    """
    message = messaging.Message(
        data=json.dumps({
            "id": 1,
            "command": "start",    
        }),
        android=android,
        token=[test_device_token]
    )

    try:
        response = messaging.send_message(message)
        print("response is ", json.dumps(vars(response)))
        assert (response.code == '80000000')
    except Exception as e:
        print(repr(e))


def init_app():
    """init sdk app"""
    global app_id, app_secret
    app_id = app_id
    app_secret = app_secret
    hpa.initialize_app(app_id, app_secret)


def main():
    init_app()
    send_push_android_data_message()


if __name__ == "__main__":
    main()
