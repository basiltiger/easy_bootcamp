$(function () {
  $(".publish").click(function () {
    $("input[name='status']").val("P");
    $("#article-form").submit();
  });

  $(".draft").click(function () {
    $("input[name='status']").val("D");
    $("#article-form").submit();
  });

  $(".preview").click(function () {
    $.ajax({
      url: '/articles/preview/',
      data: $("#article-form").serialize(),
      cache: false,
      type: 'post',
      beforeSend: function () {
        $("#preview .modal-body").html("<div style='text-align: center; padding-top: 1em'><img src='/static/img/loading.gif'></div>");
      },
      success: function (data) {
        $("#preview .modal-body").html(data);
      }
    });
  });

  $("#comment_m").focus(function() {
    $(this).attr('rows', "3");
    $("#comment-helper_m").fadeIn();
  });

  $("#comment_m").blur(function () {
    $(this).attr("rows", "1");
    $("#comment-helper_m").fadeOut();
  });


  $("#comment_m").keydown(function (evt) {
    var keyCode = evt.which?evt.which:evt.keyCode;
    if (evt.ctrlKey && (keyCode == 10 || keyCode == 13)) {
      $.ajax({
        url: '/multimedias/comment_m/',
        data: $("#comment-form_m").serialize(),
        cache: false,
        type: 'post',
        success: function (data) {
          $("#comment-list_m").html(data);
          var comment_count = $("#comment-list_m .comment_m").length;
          $(".comment-count_m").text(comment_count);
          $("#comment_m").val("");
          $("#comment_m").blur();
        }
      });
    }
  });


  $("#comment").focus(function () {
    $(this).attr("rows", "3");
    $("#comment-helper").fadeIn();
  });

  $("#comment").blur(function () {
    $(this).attr("rows", "1");
    $("#comment-helper").fadeOut();
  });

  $("#comment").keydown(function (evt) {
    var keyCode = evt.which?evt.which:evt.keyCode;
    if (evt.ctrlKey && (keyCode == 10 || keyCode == 13)) {
      $.ajax({
        url: '/articles/comment/',
        data: $("#comment-form").serialize(),
        cache: false,
        type: 'post',
        success: function (data) {
          $("#comment-list").html(data);
          var comment_count = $("#comment-list .comment").length;
          $(".comment-count").text(comment_count);
          $("#comment").val("");
          $("#comment").blur();
        }
      });
    }
  });

});