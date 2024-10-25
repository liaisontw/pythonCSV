
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" crossorigin="anonymous">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" crossorigin="anonymous"></script>
</head>
<body>
    <div id="wrap">
        <div class="container">
            <div class="row">
                <form class="form-horizontal" action="functions.php" method="post" name="upload_excel" enctype="multipart/form-data">
                    <fieldset>
                        <!-- Form Name -->
                        <legend>Form Name</legend>
                        <!-- File Button -->
                        <div class="form-group">
                            <label class="col-md-4 control-label" for="filebutton">Select File</label>
                            <div class="col-md-4">
                                <input type="file" name="file" id="file" class="input-large">
                            </div>
                        </div>
                        <!-- Button -->
                        <div class="form-group">
                            <label class="col-md-4 control-label" for="singlebutton">Import data</label>
                            <div class="col-md-4">
                                <button type="submit" id="submit" name="Import" class="btn btn-primary button-loading" data-loading-text="Loading...">Import</button>
                            </div>
                        </div>
                        <!-- Button -->
                        <div class="form-group">
                            <label class="col-md-4 control-label" for="singlebutton">Re-order data</label>
                            <div class="col-md-4">
                                <button type="submit" id="submit" name="Reorder" class="btn btn-primary button-loading" data-loading-text="Re-ordering...">Re-order</button>
                            </div>
                        </div>
                    </fieldset>
                </form>
            </div>
            <div>
                <form class="form-horizontal" action="export.php" method="post" name="upload_excel"   
                        enctype="multipart/form-data">
                    <div class="form-group">
                                <div class="col-md-4 col-md-offset-4">
                                    <input type="submit" name="Export" class="btn btn-success" value="export to excel"/>
                                </div>
                    </div>                    
                </form>           
            </div>
            <?php
            
               get_all_records();
            ?>
        </div>
    </div>
</body>
</html>

<?php

function get_all_records(){
    //$con = getdb();
    $servername = "localhost";
    $username = "root";
    $password = "Lc0205chang";
    $db = "employeeinfo";
    //echo "Connecting...."; 

    try {
        
        $con = mysqli_connect($servername, $username, $password, $db);
        //echo "Connected successfully"; 
        }
    catch(exception $e)
        {
        echo "Connection failed: " . $e->getMessage();
        }
    $Sql = "SELECT * FROM employeeinfo";
    $result = mysqli_query($con, $Sql);  
    if (mysqli_num_rows($result) > 0) {
        $total_count = 0;
        echo "<div class='table-responsive'><table id='myTable' class='table table-striped table-bordered'>
                <thead><tr>  <th>部門</th>
                            <th>職稱</th>
                            <th>姓名</th>
                            </tr></thead><tbody>";
        while($row = mysqli_fetch_assoc($result)) {
            echo "<tr><td>" . $row['department']."</td>
                    <td>" . $row['title']."</td>
                    <td>" . $row['name']."</td></tr>";        
            $total_count++;
        }
        echo "</tbody></table></div>";     
        echo "<div>總計:".$total_count."人</div>";
    } else {
        echo "you have no records";
    }
}


/*

// Comment these lines to hide errors
error_reporting(E_ALL);
ini_set('display_errors', 1);

require 'includes/config.php';
require 'includes/functions.php';

init();

*/
