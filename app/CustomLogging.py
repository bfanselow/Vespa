"""
  This module provides logging filter Class for handling logger setup.
  This filter allows us to inject custom information into the log records.

  Currently we only inject source-ip-address from request

"""

import logging
##----------------------------------------------------------------------------
class CustomContextFilter(logging.Filter):

    def __init__(self, d_init_args):

      self.cname = self.__class__.__name__

      self.source_ip = 'src_ip_not_set'

      if 'source_ip' in d_init_args:
        self.source_ip = d_init_args['source_ip']

    ##-----------------------------------------------------------------
    def filter(self, record):
        record.source_ip = self.source_ip
        return True

##----------------------------------------------------------------------------
def reset_log_filter(source_ip):
    ## Reset custom formatting filter

    log_filter = CustomContextFilter({'source_ip': source_ip})
    return(log_filter)

##----------------------------------------------------------------------------
