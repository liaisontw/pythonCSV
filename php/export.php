<?php

$servername = "localhost";     $username = "root";
$password = "Lc0205chang";     $db = "employeeinfo";
//echo "Connecting...."; 
try {    
    $con = mysqli_connect($servername, $username, $password, $db);
    //echo "Connected successfully"; 
} catch(exception $e) {
    echo "Connection failed: " . $e->getMessage();
}

if(isset($_POST["Export"])){
    header('Content-Type: text/csv; charset=utf-8');  
    header('Content-Disposition: attachment; filename=data.csv');  
    $output = fopen("php://output", "w");  
    
    $query = "SELECT * from reorder ORDER BY emp_id ASC";  
    $result = mysqli_query($con, $query);  
    while($row = mysqli_fetch_assoc($result))  {  
        $out_row = array($row['department'], $row['title'], $row['name'] );
        fputcsv($output, $out_row);  
        //fputcsv($output, $row);  
    }
    fclose($output);  
}

?>