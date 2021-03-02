from functools import partial


def send_email(callback, *args, **kwargs):
    """ Assume this is rq/celery function that will go into `delay` and should run some
    callback function after email was sent
    """
    # something happening here to send the email
    # and then callback happens
    callback()


def print_what_email_was_sent(email_name):
    print(f"{email_name} was sent")


def send_first_email():
    p = partial(print_what_email_was_sent, email_name="first_email")
    send_email(p)

def send_second_email():
    p = partial(print_what_email_was_sent, email_name="second_email")
    send_email(p)


if __name__ == "__main__":
    send_first_email()
    send_second_email()
