$(document).ready(function(){
    val = $("#base-container").attr("article_id");
    $("#comment_list_article_id").attr("value",val);
});
function validate_email(field,alerttxt)
{
    with (field)
    {
    apos=value.indexOf("@")
    dotpos=value.lastIndexOf(".")
    if (apos<1||dotpos-apos<2) 
      {alert(alerttxt);return false}
    else {return true}
    }
}
function validate_required(field,alerttxt)
{
    with (field)
    {
        if (value==null||value=="")
        {alert(alerttxt);return false}
        else {return true}
    }
}

function validate_form(thisform)
{
    with (thisform)
    {
        if (validate_required(critic_name,"没有大名么!")==false)
          {critic_name.focus();return false}
        if (validate_email(email,"你的邮箱好像不对啊!")==false)
          {email.focus();return false}
        if (validate_required(content,"多写两句能咋滴!")==false)
          {content.focus();return false}
    }
}
