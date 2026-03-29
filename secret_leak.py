import os


def get_aws_secret_key():
    key = os.getenv("AWS_SECRET_KEY")
    if not key:
        raise EnvironmentError("AWS_SECRET_KEY is not set")
    return key


def mask_secret(secret, visible=4):
    if len(secret) <= visible * 2:
        return "******"
    return f"{secret[:visible]}...{secret[-visible:]}"


def connect():
    key = get_aws_secret_key()
    print(f"Connecting with AWS key {mask_secret(key)}")


if __name__ == "__main__":
    connect()
