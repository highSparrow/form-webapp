"""
The submodule that handles form processing.
"""

def process(**kwargs):
    """
    Processes the form arguments and returns a message to display to the user.

    Keyword Arguments
    -----------------
    The keyword arguments are of the form:
        {
            'name': value
        }
    Where the name is the same key as in FORM_SPECIFICATION in app.py and the
    value is provided by the user.

    Returns
    -------
    str: The message to display to the user.
    """
    return 'You submitted: {}'.format(kwargs)