/**
 * Created by python on 17-8-31.
 */


    function show_reply_form() {
        // alert(2)
        var $this = $(this);
        var comment_id = $this.data('comment-id');
        var reply_name = $(this).siblings('h4').text();
        // alert(comment_id);
        // alert(reply_name)
        $('#id_parent').val(comment_id);
        // alert($('#form-comment h4').text())

        $('#form-comment h4').text('回复：'+reply_name);
        $('.btn-primary').val('发表回复');
        $('#cancel_reply').text('取消回复');
        $('#tips').text('(*•ω•)回复不能为空哦')
        $('#form-comment').appendTo($this.parent().parent().next('.body'))
    }

    function cancel_reply_form() {
        $('#id_comment').val('');
        $('#id_parent').val('');

        $('#form-comment h4').text('评论：');
        $('.btn-primary').val('发表评论');
        $('#cancel_reply').text('取消评论');
        $('#tips').text('(*•ω•)评论不能为空哦');


        $('#form-comment').appendTo($('#wrap-form-comment'));

    }



    function submit_comment() {
        var text = $('textarea').val();
        // alert($.trim(text))
        if($.trim(text) == '') {
            // alert(text);
            $tips=$('#tips');
            var width =$('#P_tips').width();
            // alert(width)
            if (width <= 350 ){
                $tips.css('margin-left',0)
            }else {
                $tips.css('margin-left','10%')
            }
            $tips.show();
            $tips.delay(2000).hide(0);

        }else {
            $('#myform').submit()
        }

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
        $('.btn-primary').click(submit_comment);

});
