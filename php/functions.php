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


<?php
    $department_list = array(
        '局長室',     '副局長室',   '秘書室',     
        '火災調查科', '災害預防科', '災害搶救科', '災害管理科',  '緊急救護科', 
        '教育訓練科', '勤務指揮科', '行政科', '人事室',  '會計室', '政風室', 
        '第一大隊', 
        '竹北分隊', '光明分隊',  '豐田分隊', '新豐分隊', '山崎分隊', 
        '第二大隊', 
        '竹東分隊', '二重分隊',  '北埔分隊', '峨眉分隊', '寶山分隊', 
        '橫山分隊', '尖石分隊',  '五峰分隊', 
        '第三大隊', 
        '湖口分隊', '新工分隊', '新埔分隊',  '關西分隊', '芎林分隊'
    );
    
    $servername = "localhost";     $username = "root";
    $password = "Lc0205chang";     $db = "employeeinfo";
    //echo "Connecting...."; 
    try {    
        $con = mysqli_connect($servername, $username, $password, $db);
        //echo "Connected successfully"; 
    } catch(exception $e) {
        echo "Connection failed: " . $e->getMessage();
    }

    if(isset($_POST["Reorder"])){ 
        /*
        echo "Reorder test"; 
        echo "<div class='table-responsive'><table id='myTable' class='table table-striped table-bordered'>
                <thead><tr>  <th>部門</th>
                            <th>職稱</th>
                            <th>姓名</th>
                            </tr></thead><tbody>";
        foreach($department_list as $department) {
            echo "<tr><td>" .$department."</td><td></td><td></td></tr>";        
        }
        echo "</tbody></table></div>";     
        */

        try {   
            $con = mysqli_connect($servername, $username, $password, $db);
            //echo "Connected successfully"; 
        } catch(exception $e) {
            echo "Connection failed: " . $e->getMessage();
        }
        $sql = "TRUNCATE TABLE `reorder` "; $result = mysqli_query($con, $sql);
        $Sql = "SELECT * FROM employeeinfo";
        $result = mysqli_query($con, $Sql);  
        if (mysqli_num_rows($result) > 0) {
            //fputcsv($output, array('部門', '職稱', '姓名'));  
            $total_count = 0;
            echo "<div class='table-responsive'><table id='myTable' class='table table-striped table-bordered'>
                    <thead><tr>  <th>部門</th>
                                <th>職稱</th>
                                <th>姓名</th>
                                </tr></thead><tbody>";
            
            $sql = "INSERT INTO `reorder` (department, title, name) VALUES"."('部門', '職稱','姓名')";
            mysqli_query($con, $sql);
            foreach($department_list as $department) {
                $Sql = "SELECT * FROM employeeinfo";
                $result = mysqli_query($con, $Sql);  
            
                while($row = mysqli_fetch_assoc($result)) {
                    if ($department == $row['department']) {
                        //fputcsv($output, $row);
                        $department = $row['department']; $title = $row['title']; $name = $row['name'];
                        $sql = "INSERT INTO `reorder` (department, title, name) VALUES"."('$department', '$title','$name')";
                        mysqli_query($con, $sql);
                        
                        $total_count++;
                        echo "<tr><td>" . $row['department']."</td>
                                <td>" . $row['title']."</td>
                                <td>" . $row['name']."</td></tr>";        
                    }
                }

            }
            echo "</tbody></table></div>";     
            echo "<div>總計:".$total_count."人</div>";
            //fclose($output);
        } else {
            echo "you have no records";
        }


        
        
    }

        if(isset($_POST["Import"])){
        $sql = "TRUNCATE TABLE `employeeinfo` "; $result = mysqli_query($con, $sql);
        $sql = "SELECT * FROM employeeinfo";     $result = mysqli_query($con, $sql);
        if (mysqli_num_rows($result) > 0) echo "you have records"; else echo "you have no records";

        $filename=$_FILES["file"]["tmp_name"];    
        if($_FILES["file"]["size"] > 0)
        {
            $file = fopen($filename, "r"); $error_count = 0; $insert_count = 0;
            while (($getData = fgetcsv($file, 10000, ",")) !== FALSE)
            {
                $department = $getData[2]; $title = $getData[5]; $name = $getData[4];

                if(('部門' != $department) && ('' != $department)) {
                    $sql = "INSERT INTO `employeeinfo` (department, title, name) VALUES"."('$department', '$title','$name')";
                    $result = mysqli_query($con, $sql);
                    if(!$result)
                    {
                        $error_count++;
                        //echo "<script type=\"text/javascript\"> alert(\"Invalid File:Please Upload CSV File.\"); window.location = \"index.php\" </script>"; 
                        echo "Invalid File:Please Upload CSV File";
                    } else {
                        $insert_count++;
                        //echo "<script type=\"text/javascript\"> alert(\"CSV File has been successfully Imported.\"); window.location = \"index.php\" </script>";
                        //echo "CSV File has been successfully Imported.".$result;
                    }
                }
            }
            if(!$error_count)  echo "CSV File has been successfully Imported.";
            fclose($file);  
        }
    }
?>

</div>
    </div>
</body>
</html>
