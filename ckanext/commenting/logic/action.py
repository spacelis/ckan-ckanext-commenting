"""
File: action.py
Author: Wen Li
Email: wen.li@ucl.ac.uk
Github: http://github.com/spacelis
Description: The actions available for comments.
"""

from datetime import datetime


def comment_show(context, data_dict):
    """ Get the comment from the database.

    :context: TODO
    :data_dict: TODO
    :returns: TODO

    """
    return {'author': 'WL', 'message': 'Some comment on this', 'timestamp': datetime()}



def comment_create(context, data_dict):
    """ Get the comment from the database.

    :context: TODO
    :data_dict: TODO
    :returns: TODO

    """
    return {'author': 'WL', 'message': 'Some comment on this', 'timestamp': datetime()}


def comment_delete(context, data_dict):
    """ Get the comment from the database.

    :context: TODO
    :data_dict: TODO
    :returns: TODO

    """
    return {'author': 'WL', 'message': 'Some comment on this', 'timestamp': datetime()}
