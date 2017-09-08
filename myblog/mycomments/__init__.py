



def get_model():
    from threadedcomments.models import ThreadedComment
    return ThreadedComment

def get_form():
    from mycomments.forms import MyCommentForm
    return MyCommentForm