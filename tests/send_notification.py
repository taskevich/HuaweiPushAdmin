import hpa
import json

from hpa import messaging
from vars import app_id, app_secret, test_device_token


notification = messaging.Notification(
    title='Wake Up',
    body='Time to die',
)

android_notification = messaging.AndroidNotification(
    click_action=messaging.AndroidClickAction(
        action_type=2,
        url="https://www.huawei.com"
    ),
    importance=messaging.AndroidNotification.PRIORITY_HIGH,
    visibility=messaging.AndroidNotification.PUBLIC,
    foreground_show=True
)

android = messaging.AndroidConfig(
    collapse_key=-1,
    urgency=messaging.AndroidConfig.HIGH_PRIORITY,
    ttl="10000s",
    bi_tag='the_sample_bi_tag_for_receipt_service',
    notification=android_notification
)


def send_push_android_notify_message():
    """
    a sample to show hwo to send web push message
    :return:
    """
    message = messaging.Message(
        notification=notification,
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
    hpa.initialize_app(app_id, app_secret)


def main():
    init_app()
    send_push_android_notify_message()


if __name__ == '__main__':
    main()
    