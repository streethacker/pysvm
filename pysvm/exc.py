# -*- coding: utf-8 -*-

__all__ = ['VerifyCodeError']


class VerifyCodeError(Exception):

    def __init__(self, message=None):
        super(VerifyCodeError, self).__init__(message)
