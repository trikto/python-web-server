<?php
$x = $_POST['x'];
$y = $_POST['y'];
$x = (int) $x;
$y = (int) $y;
$out = $x + $y;
?>

<html>

<body>
    <?php
    echo "$x + $y = $out";
    ?>
</body>

</html>