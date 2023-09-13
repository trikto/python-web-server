<?php   
        $number1 = $_POST['x'];  
        $number2 = $_POST['y'];  
        $sum =  $number1+$number2;  
?>  
<html>
<style>


body
{
  overflow: hidden;
  margin: 0px;
  padding: 0px;
  font-family: Arial, sans-serif;
  background: #c0c0ff;
}

#form
{
  color: #000;
  border: 0px solid #afafaf;
font-weight: bold;
  width: 30%;
  margin-left: 35%;
  margin-top: 120px;
  text-align: center;
  padding: 40px;
  padding-top: 20px;
  border-radius: 3px;
  box-shadow: 0px 0px 8px #777;
  background: rgba(255, 255, 255, 255);
}

input
{
  color: #777;
  font-weight: bold;
  width: 70%;
  padding: 10px;
  margin: 10px;
  border: 1px solid #afafaf;
  border-radius: 3px;
  background: rgba(255, 255, 255, 0.5);
  outline: none;
}



</style>
<body>
<div id="form">
  <h3>Adding Two Numbers</h3>
  <label for="num1">Number 01:</label>
  <input type="text" name="x" value="<?php echo  $_POST['x'];?>" disabled="" />
  <br>
  <label for="num1">Number 02:</label>
  <input type="text" name="y" value="<?php echo  $_POST['y'];?>" disabled=""/>
  <br>
<label for="total">Total value:</label>
<input type="text" name="total" value="<?php echo $sum ?>"disabled=""/>
    
</div>
</body>
</html>