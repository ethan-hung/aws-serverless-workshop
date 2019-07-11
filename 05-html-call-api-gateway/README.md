# HTML call API Gateway
1. Open Visual Studio Code
2. Open file "index.html"
3. type some html code
```html
<div id="field1">
    <label>get</label>
    <br>
    <label id="label_get"></label>
    <br><br>
</div>
<div id="field2">
    <label>First name:</label>
    <input type="text" id="firstName">
    <label>Last name:</label>
    <input type="text" id="lastName">
</div>
<div id="field3">
    <label>Message:</label>
    <textarea id="message" rows="4"></textarea>
</div>
<div id="field4">
    <label id="label_post"></label>
</div>
<div id="field5">
    <button type="button" id="btn_submit">Submit!!</button>
</div>
```
4. Import JQuery libery
```html
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
```
5. Write some javascript for AJAX
```javascript
var click_btn_demo = function(){
    var data = {
        firstName: $("#firstName")[0].value, 
        lastName: $("#lastName")[0].value,
        message: $("#message")[0].value
    };
    $.ajax({
        method: "POST",
        url: "https://07vw22x7oj.execute-api.us-west-2.amazonaws.com/stage/shoe",
        data: JSON.stringify(data)
    }).done(function(res){
        $("#label_post").text(JSON.stringify(res));
        console.log(res);
    })
}

var auto_get_data = function(){
    $.ajax({
        method: "GET",
        url: "https://07vw22x7oj.execute-api.us-west-2.amazonaws.com/stage/shoe"
    }).done(function(res){
        $("#label_get").text(JSON.stringify(res));
        console.log(res);
    })
}

$(document).ready(function(){
    $("#btn_submit").on('click',function(){
        console.log('click');
        click_btn_demo();
    })

    auto_get_data();
})
```