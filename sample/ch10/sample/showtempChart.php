



<!doctype html>
<html>
        <head>
                <title>Bar Chart</title>
                <script src="Chart.js-master/Chart.js"></script>
        </head>
        <body>
                <div style="width: 50%">
                        <canvas id="canvas" height="450" width="800"></canvas>
                </div>
<?php
$con=mysqli_connect("localhost","root","raspberry","raspberryDB");
if (mysqli_connect_errno()) {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
}



$result = mysqli_query($con,"SELECT * FROM temp");

echo "<table border='1'>
<tr>
<th>Date Time</th>
<th>Temperature</th>
<th>user ID </>

</tr>";

while($row = mysqli_fetch_array($result))
{
  echo "<tr>";
  echo "<td>" . $row['datetime'] . "</td>";
  echo "<td>" . $row['temp'] . "</td>";
  echo "<td>" . $row['userid'] . "</td>";
  echo "</tr>";
  $Lables=$Lables.'"'. $row['datetime'].'",';
  $temps=$temps.'"'. $row['temp'].'",';
}

echo "</table>";
mysqli_close($con);
?>


        <script>
var barChartData = {
                labels : [<?php echo  $Lables;  ?>],
                datasets : [
                        {
                                fillColor : "rgba(20,20,20,0.5)",
                                strokeColor : "rgba(220,220,220,0.8)",
                                highlightFill: "rgba(220,220,220,0.75)",
               highlightStroke: "rgba(220,220,220,1)",
                                data : [<?php echo  $temps;  ?>
                                ]
                       }
                ]
        }
        window.onload = function(){
                var ctx = document.getElementById("canvas").getContext("2d");
                window.myBar = new Chart(ctx).Bar(barChartData, {
                        responsive : true
                });
        }
        </script>
        </body>
</html>




