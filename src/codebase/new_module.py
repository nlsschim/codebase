from codebase import predict


def pass_data():
    return True


def dont_pass_data():
    predict([0, 0, 0, 0])
    return False
