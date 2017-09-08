/**
 * Created by python on 17-8-31.
 */


    function show_reply_form() {
        // alert(2)
        var $this = $(this);
        var comment_id = $this.data('comment-id');
        var reply_name = $(this).siblings('h4').text()
        // alert(comment_id);
        // alert(reply_name)
        $('#id_parent').val(comment_id);
        // alert($('#form-comment h4').text())
        $('#form-comment h4').text('回复：'+reply_name)
        $('#form-comment').appendTo($this.parent().parent().next('.body'))
    }

    function cancel_reply_form() {
        $('#id_comment').val('');
        $('#id_parent').val('');

        $('#form-comment h4').text('评论：')
        $('#form-comment').appendTo($('#wrap-form-comment'))

    }

$.fn.ready(function () {
        // $('.reply-link').click(function () {
        // alert('ok');

            // alert(2)
        // var $this = $(this);
        // var comment_id = $this.data('comment-id');
        // alert(comment_id);

        // $('#id_parent').val(comment_id);
        // alert($('#id_parent').val())
        //   $(this).parent().parent().next('.body').css('background', 'red')
        // $('#form-comment').appendTo($this.parent().parent().next('.body'))

        $('.reply-link').click(show_reply_form);
        $('#cancel_reply').click(cancel_reply_form);

});
