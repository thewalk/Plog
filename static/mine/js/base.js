$(document).ready(function(){
    $("#base-nav-portrait2").hide();
    $("#base-container").hide();
    $(".base-nav-bar-link").click(function(e){
        $("#base-container").hide();
        reset();
        category_type = $(this).attr("tag");
        htmlobj=$.get("/blog/article_base/",{'category_type':category_type},function(result){
                $("#base-container").attr('category_type',category_type);
                $("#base-container").attr('page',1);
                $("#base-container").attr('more_btn',1);
                $("#base-container").html(result);
                $("#base-container").slideDown();
        });
    });
    $("#base-nav-bar-name").click(function(){
        $("#base-container").slideToggle();
    });
    function reset(){
        $("#base-container").attr("page",1);
        $("#base-container").attr("tag_id","");
        $("#base-container").attr("category_id","");
        $("#base-container").attr("more_btn",1);
        $("#base-container").attr("article_id","");
    }
});

var picObj;
var picLeftCount = 80;
var picForward = 1;
var picCollisionTimes = 0;
var picTimer;
function runpic(obj)
{
    picObj = obj;
    changepic();
}
function changepic()
{
    if(picForward == 1)
    {
        picLeftCount = picLeftCount + 15;
    }
    else if(picForward == 0)
    {
        picLeftCount = picLeftCount - 15;
    }
    else
    {
        picForward = 1;
        picLeftCount = 80;
    }
    if(picLeftCount >= 900)
    {
        picForward = 0;
        blink();
    }
    if(picLeftCount < 80)
    {
        picLeftCount = picLeftCount + 10;
        picForward = 2;
    }
    else
    {
        picObj.style.left = picLeftCount + "px";
        picTimer = setTimeout("changepic()",10);
    }
}
function blink()
{
    if(picCollisionTimes%2 == 0)
        $("#base-nav-portrait2").show(1000);
    else
        $("#base-nav-portrait2").hide(1000);
    picCollisionTimes++;
}
