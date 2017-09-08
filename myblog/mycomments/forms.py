from crispy_forms.helper import FormHelper
from threadedcomments.forms import ThreadedCommentForm


class MyCommentForm(ThreadedCommentForm):

    '''
        My Customized Comment Form.
        Just add some features via crispy.
    '''

    #: Helper for {% crispy %} template tag
    helper = FormHelper()
    helper.form_tag = False

