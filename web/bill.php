<?php
$mysqli = new mysqli("localhost", "root", "", "energymeter");
if($mysqli->connect_error) {
  exit('Could not connect');
}

$sql = "SELECT * FROM bill";

$stmt = $mysqli->prepare($sql);
$stmt->execute();
$stmt->bind_result($unit, $charges, $meter_number, $location, $past_unit, $current_unit, $consumed_unit, $charges_per_unit , $total_charges, $tax, $bill);
echo "<table style='border: solid 1px black;'>";

echo "<tr>";
echo "<th>Unit</th>";
echo "<th>Charges</th>";
echo "<th>Meter Number</th>";
echo "<th>Location</th>";
echo "<th>Past Unit</th>";
echo "<th>Current Unit</th>";
echo "<th>Consumed Unit</th>";
echo "<th>Charges Per Unit</th>";
echo "<th>Total Charges</th>";
echo "<th>Tax</th>";
echo "<th>Bill</th>";echo "</tr>";
while($stmt->fetch())
{ 
echo "<td style='width: 150px; border: 1px solid black;'>" . $unit . "</td>";

echo "<td style='width: 150px; border: 1px solid black;'>" . $charges . "</td>";

echo "<td style='width: 150px; border: 1px solid black;'>" . $meter_number . "</td>";

echo "<td style='width: 150px; border: 1px solid black;'>" . $location . "</td>";

echo "<td style='width: 150px; border: 1px solid black;'>" . $past_unit . "</td>";

echo "<td style='width: 150px; border: 1px solid black;'>" . $current_unit . "</td>";

echo "<td style='width: 150px; border: 1px solid black;'>" . $consumed_unit . "</td>";

echo "<td style='width: 150px; border: 1px solid black;'>" . $charges_per_unit . "</td>";

echo "<td style='width: 150px; border: 1px solid black;'>" . $total_charges . "</td>";

echo "<td style='width: 150px; border: 1px solid black;'>" . $tax . "</td>";

echo "<td style='width: 150px; border: 1px solid black;'>" . $bill . "</td>";
echo "<tr>";echo "</tr>" . "\n";

}
echo "</table>";
?>
