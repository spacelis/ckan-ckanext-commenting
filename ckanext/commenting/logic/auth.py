"""
File: auth.py
Author: Wen Li
Email: wen.li@ucl.ac.uk
Github: http://github.com/spacelis
Description: Authorization for comments
"""

import ckan.new_authz

def comment_create(context, data_dict):
    """ Whether the user have the right to add comment.

    :context: TODO
    :data_dict: TODO
    :returns: TODO

    """
    return {'sucess': True}


def comment_delete(context, data_dict):
    """ Whether the user have the right to delete comment.

    :context: TODO
    :data_dict: TODO
    :returns: TODO

    """
    # TODO compute the actual permission for deleting comments.
    return {'sucess': True}


def comment_show(context, data_dict):
    """ Whether the user have the right to see the comments.

    :context: TODO
    :data_dict: TODO
    :returns: TODO

    """
    return {'success': True}
