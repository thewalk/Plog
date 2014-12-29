$(document).ready(function(){
    $(".article-list-article-link").click(function(){
        category_id = $("#base-container").attr("category_id");
        tag_id = $("#base-container").attr("tag_id");
        article_id = $(this).attr('tag');
        $("#base-container").attr("article_id",article_id);
        $("#article-base-more").text("评论");
        $("#base-container").attr("more_btn",0);
        $("#base-container").hide();
        htmlobj=$.get("/blog/article_detail/",
                        {"category_id":category_id,'tag_id':tag_id,'article_id':article_id},
                        function(result){
                            $("#article-base-container").html(result);
                            $("#base-container").slideDown();
                        }
        );
    });
});
