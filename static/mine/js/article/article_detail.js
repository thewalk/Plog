$(document).ready(function(){
    $("#article-detail-previous").click(function(){
        article_id = $("#article-detail-previous").attr("tag");
        category_id = $("#base-container").attr("category_id");
        tag_id = $("#base-container").attr("tag_id");
        $("#base-container").attr("more_btn",0);
        $("#base-container").attr("article_id",article_id);
        $("#article-base-more").text("评论");
        $("#base-container").hide();
        htmlobj=$.get("/blog/article_detail/",
                        {"category_id":category_id,'tag_id':tag_id,'article_id':article_id},
                        function(result){
                            $("#article-base-container").html(result);
                            $("#base-container").slideDown();
                        }
        );
    });
    $("#article-detail-next").click(function(){
        article_id = $("#article-detail-next").attr("tag");
        category_id = $("#base-container").attr("category_id");
        tag_id = $("#base-container").attr("tag_id");
        $("#base-container").attr("article_id",article_id);
        $("#base-container").attr("more_btn",0);
        $("#article-base-more").text("评论");
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
