# -*- coding: utf-8 -*-

__all__ = ['VerifyCodeError']


from httplib import OK

VERIFYCODE_ERROR = {
    2101: 'Verify code not match',
    2102: 'Verify code storage error',
}


class VerifyCodeError(Exception):
    status_code = OK

    def __init__(self, error_code, error_msg=None, status_code=None):
        super(VerifyCodeError, self).__init__(error_msg)
        self.error_code = error_code
        self.error_msg = error_msg or VERIFYCODE_ERROR.get(error_code)

        if status_code is not None:
            self.status_code = status_code
