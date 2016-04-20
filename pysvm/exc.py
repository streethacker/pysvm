# -*- coding: utf-8 -*-

__all__ = ['VerifyCodeError']


from httplib import OK

MSG_MAP = {
    2101: 'Verify code not match',
    2102: 'Verify code storage error',
    2103: 'Trials more than allowed',
}


class VerifyCodeError(Exception):
    status_code = OK

    def __init__(self, error_code, error_msg=None, status_code=None):
        self.error_code = error_code
        self.error_msg = error_msg or MSG_MAP.get(error_code)
        if status_code is not None:
            self.status_code = status_code
        super(VerifyCodeError, self).__init__(self.error_msg)
