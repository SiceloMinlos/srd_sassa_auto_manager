<?php

$id = $_POST['id'];
$password = $_POST['password'];

//Database Connection

$connection = new mysqli('localhost', 'root', '', 'Register');
if ($connection -> connect_error) {
    die('Connection Failed : ' . $connection -> connect_error);
} else {
    $sql = 'select * from Registration';
    $results = $connection->query($sql);

    while ($row = $results -> fetch_assoc()) {
        if ($password == $row['password'] and $id == $row['id']) {
            echo json_encode('Connected');
            break;
        } else {
            echo json_encode('Not Connected');
            break;
        }
    }

    $stmt -> close();
    $connection -> close();
}

?>