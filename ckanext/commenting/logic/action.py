"""
File: action.py
Author: Wen Li
Email: wen.li@ucl.ac.uk
Github: http://github.com/spacelis
Description: The actions available for comments.
"""

from datetime import datetime
from ckan.logic.action.get import package_show as ckan_package_show
from ckan.logic import check_access as _check_access
import ckan.plugins as p
import ckan.plugins.toolkit as tk


#FIXME remove the mock tweets
def mock_comments():
    """ mocking comments.
    :returns: TODO

    """
    return [
        {'author': {'display_name': 'Alice'}, 'message': 'This is a comment from Alice', 'timestamp': '2015-01-01'},
        {'author': {'display_name': 'Bob'}, 'message': 'This is a comment from Bob', 'timestamp': '2015-01-02'}
    ]


def comment_show(context, data_dict):
    """ Get the comment from the database.

    :context: TODO
    :data_dict: TODO
    :returns: TODO

    """
    _check_access('comment_show', context, data_dict)
    return mock_comments()



def comment_create(context, data_dict):
    """ Get the comment from the database.

    :context: TODO
    :data_dict: TODO
    :returns: TODO

    """
    pass


def comment_delete(context, data_dict):
    """ Get the comment from the database.

    :context: TODO
    :data_dict: TODO
    :returns: TODO

    """
    pass


def package_show(context, data_dict):
    """TODO: Docstring for package_show.

    :context: TODO
    :data_dict: TODO
    :returns: TODO

    """
    pkg_dict = ckan_package_show(context, data_dict)
    # TODO make actual retrieval from database for comments
    pkg_dict['comments'] = tk.get_action('comment_show')(context, data_dict)
    return pkg_dict
