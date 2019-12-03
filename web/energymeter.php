<!DOCTYPE html>

<head>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3/jquery.min.js"></script>
</head>

<body>

<div id="bill" >
</div>

<script type="text/javascript">
function loadlink(){
    $('#bill').load('bill.php',function () {
         $(this).unwrap();
    });
}

loadlink(); // This will run on page load
setInterval(function(){
    loadlink() // this will run after every 5 seconds
}, 2000);
</script>

</body>

</html>